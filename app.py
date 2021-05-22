import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/get/cases")
def get_cases():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    # If you are hard coding the number of items per page then uncomment the two lines below
    # per_page = 6
    # offset = page * per_page

    # Gets all the values
    cases = mongo.db.cases.find()

    # Gets the total values to be used later
    total = mongo.db.cases.count_documents({})

    # Paginates the values
    paginatedCases = cases[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap5')

    return render_template("cases.html", 
                            cases=paginatedCases,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )


@app.route("/search", methods=["GET", "POST"])
def search():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    # If you are hard coding the number of items per page then uncomment the two lines below
    # per_page = 6
    # offset = page * per_page

    # Gets all the values
    query = request.form.get("query")
    cases = mongo.db.cases.find({"$text": {"$search": query}})

    # Gets the total values to be used later
    total = mongo.db.cases.count_documents({"$text": {"$search": query}})

    # Paginates the values
    paginatedCases = cases[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap5')
    return render_template("cases.html", 
                            cases=paginatedCases,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "full-name": request.form.get("full-name").title(),
            "phone": request.form.get("phone")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            session["user"]))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if request.method == "POST":
        submit = {
            "full-name": request.form.get("name"),
            "phone": request.form.get("phone"),
            }
        mongo.db.users.update_one({"username": session["user"]}, { "$set": submit})
        flash("Contact Details Successfully Updated")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    fullname = mongo.db.users.find_one(
        {"username": session["user"]})["full-name"]
    phone = mongo.db.users.find_one(
        {"username": session["user"]})["phone"]
    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            fullname=fullname,
            phone=phone
        )

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add/case", methods=["GET", "POST"])
def add_case():
    if request.method == "POST":
        # this generates a new unique case number
        caseno = mongo.db.casenumbers.find_one_and_update(
            {"_id": ObjectId("60a145f44eb297c0b8512ea5")},
            {"$inc": {"sequence_value": 1}})
        case = {
            "date": request.form.get("date"),
            "location": request.form.get("location"),
            "reason": request.form.get("reason"),
            "criminal": request.form.get("criminal"),
            "species": request.form.get("species"),
            "image_url": request.form.get("image_url"),
            "notes": request.form.get("notes"),
            "status": "Pending",
            "case_number": caseno["sequence_value"],
            "created_by": session["user"]
        }
        mongo.db.cases.insert_one(case)
        flash("Case is Successfully Added")
        return redirect(url_for("get_cases"))

    reasons = mongo.db.reason.find().sort("status", 1)
    speciess = mongo.db.species.find().sort("species", 1)
    return render_template("add-case.html", reasons=reasons, speciess=speciess)


@app.route("/edit/case/<case_id>", methods=["GET", "POST"])
def edit_case(case_id):
    if request.method == "POST":
        submit = {
            "date": request.form.get("date"),
            "location": request.form.get("location"),
            "reason": request.form.get("reason"),
            "criminal": request.form.get("criminal"),
            "species": request.form.get("species"),
            "image_url": request.form.get("image_url"),
            "notes": request.form.get("notes"),
            "status": request.form.get("status")
        }
        mongo.db.cases.update_one({"_id": ObjectId(case_id)}, {"$set": submit})
        flash("Case Successfully Updated")

    case = mongo.db.cases.find_one({"_id": ObjectId(case_id)})
    reasons = mongo.db.reason.find().sort("Reason", 1)
    speciess = mongo.db.species.find().sort("species", 1)
    statuses = mongo.db.status.find().sort("status", 1)
    return render_template(
        "edit-case.html",
        case=case,
        reasons=reasons,
        speciess=speciess,
        statuses=statuses
    )

@app.route("/delete/case/<case_id>")
def delete_case(case_id):
    mongo.db.cases.delete_one({"_id": ObjectId(case_id)})
    flash("Case Successfully Deleted")
    return redirect(url_for("get_cases"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
