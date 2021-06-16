import os
import datetime
from functools import wraps
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


# @login_required decorator
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
# Sourced from Tim Nelson's updated task manager repo
# https://github.com/TravelTimN/flask-task-manager-project/tree/demo
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/cases")
@login_required
def get_cases():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    # grabs the keyword from the url that is equal to filter
    filter = request.args.get("filter")

    if filter == "pending":
        query = {"status": "Pending"}
    elif filter == "user":
        query = {"created_by": session["user"]}
    elif filter == "open":
        query = {"status": {"$ne": "Closed"}}
    else:
        query = {}

    # Gets all the case values that match the above query
    cases = list(mongo.db.cases.find(query))

    # Gets the count total of results needed for pagination
    total = len(cases)

    # Paginates the values
    paginatedCases = cases[offset: offset + per_page]

    # please note boostrap4 is used here as bootstrap5 doesn't
    # seem to be supported
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4',
                            record_name='cases')

    return render_template("cases.html",
                           cases=paginatedCases,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/search", methods=["GET", "POST"])
def search():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    # Gets all the values that match the user entered in search box
    query = request.form.get("query")
    cases = list(mongo.db.cases.find({"$text": {"$search": query}}))

    # Gets the count total of results needed for pagination
    total = len(cases)

    # Paginates the values
    paginatedCases = cases[offset: offset + per_page]

    # Please note boostrap4 is used here as bootstrap5 doesn't
    # seem to be supported
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4',
                            record_name='cases')
    return render_template("cases.html",
                           cases=paginatedCases,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username already exists in db
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
    if "user" not in session:
        # here user is not currently logged in
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(
                        existing_user["password"],
                        request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            session["user"]))
                        return redirect(url_for(
                            "profile", username=session["user"]))
                else:
                    # invalid password match
                    flash("Incorrect Password, Please try again")
                    return redirect(url_for("login"))

            else:
                # username doesn't exist
                flash("Incorrect Username, Please try again")
                return redirect(url_for("login"))

        return render_template("login.html")

    # user is already logged-in, direct them to their profile
    return redirect(url_for("profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    if request.method == "POST":
        # Here user is updating their contact details
        submit = {
            "full-name": request.form.get("name"),
            "phone": request.form.get("phone"),
            }
        mongo.db.users.update_one({"username": session["user"]},
                                  {"$set": submit})
        flash("Contact Details Successfully Updated")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    fullname = mongo.db.users.find_one(
        {"username": session["user"]})["full-name"]
    phone = mongo.db.users.find_one(
        {"username": session["user"]})["phone"]
    if "user" in session:
        return render_template(
            "profile.html",
            username=username,
            fullname=fullname,
            phone=phone
        )

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add/case", methods=["GET", "POST"])
@login_required
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
            "notes": [],  # notes is an array variable
            "status": "Pending",
            "case_number": str(caseno["sequence_value"]),
            "created_by": session["user"]
        }
        # case is added to DB, and case ObjectID is returned
        _id = mongo.db.cases.insert_one(case)
        # Case id to isolated from the ObjectID
        case_id = _id.inserted_id
        if request.form.get("notes"):
            # if user enters a note:
            note = {
                "case_id": ObjectId(case_id),
                "date_time": datetime.datetime.now().strftime("%d %b %Y  %X"),
                "note": request.form.get("notes")
            }
            # Notes is added to the notes table in DB,
            # The note ObjectID is returned
            note_id = mongo.db.notes.insert_one(note)
            # case document notes array field is then
            # pushed the linked note ID
            mongo.db.cases.update_one(
                {"_id": ObjectId(case_id)},
                {"$push": {"notes": ObjectId(note_id.inserted_id)}}
                )

        message = f"Case is now created under case #{caseno['sequence_value']}"
        flash(message)
        return redirect(url_for("get_cases"))

    reasons = mongo.db.reason.find().sort("status", 1)
    speciess = mongo.db.species.find().sort("species", 1)
    return render_template("add-case.html", reasons=reasons, speciess=speciess)


@app.route("/view/case/<case_id>", methods=["GET", "POST"])
@login_required
def edit_case(case_id):
    if request.method == "POST":
        # here the updated form values is gathered for DB later
        submit = {
            "date": request.form.get("date"),
            "location": request.form.get("location"),
            "reason": request.form.get("reason"),
            "criminal": request.form.get("criminal"),
            "species": request.form.get("species"),
            "image_url": request.form.get("image_url"),
            "status": request.form.get("status")
        }
        # if user enters a note:
        if request.form.get("notes"):
            # makes notes array value in submit dict
            submit["notes"] = []
            note = {
                "case_id": ObjectId(case_id),
                "date_time": datetime.datetime.now().strftime("%d %b %Y  %X"),
                "note": request.form.get("notes")
            }
            # Notes is added to the notes table in DB,
            # The note ObjectID is returned
            note_id = mongo.db.notes.insert_one(note)
            # case document notes array is appended with the above note_id
            submit["notes"].append(ObjectId(note_id.inserted_id))

        # case values sent to DB
        mongo.db.cases.update_one({"_id": ObjectId(case_id)}, {"$set": submit})
        flash("Case Successfully Updated")

    # here the values for the case form are pulled from the DB
    case = mongo.db.cases.find_one({"_id": ObjectId(case_id)})
    notes_array = mongo.db.notes.find(
        {"case_id": ObjectId(case_id)}).sort("date_time", -1)
    reasons = mongo.db.reason.find().sort("Reason", 1)
    speciess = mongo.db.species.find().sort("species", 1)
    statuses = mongo.db.status.find().sort("status", 1)
    return render_template(
        "view-case.html",
        case=case,
        reasons=reasons,
        speciess=speciess,
        notes_array=notes_array,
        statuses=statuses
    )


@app.route("/delete/case/<case_id>")
@login_required
def delete_case(case_id):
    # case is deleted from case table
    mongo.db.cases.delete_one({"_id": ObjectId(case_id)})
    # linked notes is deleted from notes table
    mongo.db.notes.delete_many({"case_id": ObjectId(case_id)})
    flash("Case Successfully Deleted")
    return redirect(url_for("get_cases"))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
