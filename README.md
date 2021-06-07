# Wildlife Rescue Dublin

This is a Data Centric web app for a fictional wildlife animal rescue charity.

There are various wildlife charities that rescue or rehabilitate animals whom have been involved in accidents or become ill. Sometimes members of the public find these animals and become their carers.

A part of taking care of the animals is completing paperwork as the animal's care may requires licensing. The aim of this app is to make the process easier. Members of the public can register incident cases and the charity or Governing body can follow up.

## UX

### Scope

This is a fictional charity page, so there are no limitations on the content. The site will be made to an MVP first, and if there is additional time, content/features can be added.

#### User Stories

##### Visitor goals

As a user of this database , I want to be able to register myself a login easily.

As a user of this database , I want to be able to easily capture information on any mobile device.

As a user of this database , I want to edit case records I submitted.

As a user of this database , I want to be able to delete any information I created.

As a user of this database , I want to be able to search and filter results easily.

As a user of this database , I want to be able to edit my contact details.

As a user of this database , I want to be able to upload an image as part of my case.

##### Owner goals

As an owner of this database site, I want each case incident to have a unique case number.

As an owner of this database site, I want to be able to have a user with superuser read/write access , this user can have read/write access to all records.

As an owner of this database site, I want to be able to search and filter results easily.

### Structure

This Data centric site is put together with HTML, using the bootstrap framework along with some CSS.

The Database will be done using Python and Flask fronted onto a MongoDB backend.

### Skeleton

The page content is dynamic and composed of Jinja templates which are put together using Python Flask, JavaScript DOM methods are also used to make pages versatile.

#### Website page line up / Flask templates

- Home/index

- Login / Logout

- Register new user

- Profile / My details / Edit my Contact details

- All Cases / My Cases / Search screen / pending cases filter / open Cases filter.

- New Case

- View / Edit / Delete Case

#### Non relational Database tables schema

##### cases table	

```
_ID: (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
case_number: (auto-generated and used as reference for the case) INTEGER (INDEXED FIELD) (Not changeable)
created_by: (username from logged in session) STRING
date: date
Status: STRING
location: STRING (INDEXED FIELD)
image_url: STRING
species: STRING (INDEXED FIELD)
reason: STRING (INDEXED FIELD)
criminal: (yes/No)
Note and comments: ARRAY of ObjectId (linked to notes table _id field )
```

##### User details table

```
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
full-name : STRING
username :  STRING (Not changeable)
password : STRING (Not changeable)
Phone: STRING
```

##### notes  table

```
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
case_id: ObjectId INDEXED (linked to cases table _id field )
date_time : datetimestamp
note: STRING
```
##### reason  table

```
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
reason: STRING
```
##### species table

```
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
species: STRING
```
##### status table

```
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
status: STRING
```

#### Wireframes

![wireframe 1 homepage](wireframe/wireframe1-homepage.png)
![wireframe 2 all cases view](wireframe/wireframe2-all-cases-view.png)
![wireframe 3 case view](wireframe\wireframe3-case-view.png)


### Surface

#### Colours

Colour are natural and sourced from a nature photo.

#FFFFFD Black White - taken from the colour of the feathers of a Grey Heron bird 

#ADCE4B Turmeric - taken from Green river reeds on the River Liffey 

#6C6666 Dove Gray - taken from the colour of the feathers of a Grey Heron bird

#FEE579 Kournikova  - taken from the colour of the beak of a Grey Heron bird

#### Icons

Bootstrap is used for icons

#### Images

images are sourced from here and here https://diygarden.co.uk/wildlife/rescue-guide/

#### Fonts

Font used is Rubik from Google fonts.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.


### Existing Features

- Pagination on cases page.
- autocomplete on certain fields in the new case and edit case screen.
- filtered views on cases
- Visitor can register , login and update their contact details
- Visitor has full CRUD access to the case they create. 
- Google places integration
- Unique case Id generated for each case
- Cloudinary image upload integration

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- Refactor homepage layout?

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### Frontend

#### Languages

- HTML
- CSS
- JavaScript
- Python

#### Libraries and Frameworks

- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- Fonts : [Google Fonts](https://fonts.google.com/)
- Icons : [Bootstrap](https://icons.getbootstrap.com/)

#### Tools

- JSfiddle : I used this online IDE to build and play with [Cloudinary API](https://jsfiddle.net/kenwals/8ze3u4ok/33/) and [Google places API](https://jsfiddle.net/kenwals/gv2oe4dp/8/) before i added them to this project confidently
- Wireframe: [Balsamiq](https://balsamiq.com/)
- IDE: Visual Studio Code (VS Code).
- Version control: Git
- Browser Developer tools : [Google Chrome](https://www.google.com/chrome) for console.logging everything.
- Kanban planner : [Github projects](https://github.com/kenwals/Wildlife-Rescue/projects/1).
- Markdown editor: [Typora](https://typora.io/) was used when appropriate, VS code editor was used for most updates.
- File renaming utility: PowerRename from [PowerToys on Windows 10](https://www.windowscentral.com/how-bulk-rename-your-files-windows-10-powertoys)
- Pomodoro timer : [Tomato Clock](https://chrome.google.com/webstore/detail/tomato-clock/enemipdanmallpjakiehedcgjmibjihj)
- Favicon creator : [favicon.io](https://favicon.io/favicon-generator/)
- Autoprefixer CSS : [Autoprefixer](https://autoprefixer.github.io/)
- Auto formatter for HTML, CSS and JS:  [webformatter](https://webformatter.com/html)
- px to rem convertor : [nekoCalc](https://nekocalc.com/px-to-rem-converter)
- JavaScript linter : [jshint](https://jshint.com/)
- Python linter :  [Pep8 online](http://pep8online.com/)
- markdown linter : markdownlint extension on VS Code.
- Colour names : [Name that color ](https://chir.ag/projects/name-that-color/#6195ED)
- [markdown table of contents creator](https://ecotrust-canada.github.io/markdown-toc/)
- [site preview tool](http://ami.responsivedesign.is/)
- [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

### Performance Testing

### Bugs encountered on the way



depreciated code ( count, update, ) exanple : DeprecationWarning: update is deprecated. Use replace_one, update_one or 
update_many instead. mongo.db.cases.update({"_id": ObjectId(case_id)}, { "$set": submit})



### Known issues

Pagination orientation problem

For Pagination , I am using flask-paginate. At the time this project was being developed , this module didn't appear to support Bootstrap5 . So I have had to configure it to Bootstrap4. Still a problem placing 

Favicon

Favicons doesn't work on Android devices . 

### Project barriers and solutions

MongoDB verses PyMongo 

When making the case number increment based on code i read in the MongoDB manual , i couldn't get it working in my Python code. But then i read [this article](https://stackoverflow.com/questions/17054494/pymongo-inc-having-issues/17054663). Hereby learning that PyMongo is slightly different from MongoDB!.

### Version control

For version control, I used the UI on VS Code for making git commits or the GitHub desktop app, Merging was done on the GitHub site. I used branches when I was working on new features or bundles of changes.

### Functionality Testing

### Responsiveness Testing

### CSS3 validator

### HTML5 validator

### JavaScript validator

### Usability Testing

### Compatibility Testing

### Testing User Stories

#### Visitor Stories

#### Owner Story

## Deployment

For easy deployment on Heruko.com , you will need a GitHub user account and possibly a Gitpod user account. If you wish to make changes to this repository, please follow the GitHub steps first.

### GitHub

GitHub is a code hosting platform for version control and collaboration. It's free to enrol for a user account and I would recommend you have one if you wish to deploy this repository and make changes.

When you have a GitHub account you can simply click on the Fork button on the top right corner. This will clone the Wildlife-Rescue repository for your GitHub account, then you can make any changes you like.

### Gitpod

The site can be edited easily on a Gitpod online workspace, you first register a free user account on <http://gitpod.io/>, then download the Gitpod extension on your preferred internet browser. On signing up you will be expected to have a GitHub user account.

Once you have the extension on your browser, a green Gitpod button will appear beside this repository in GitHub. For best results fork the repository in your personal account before you open it in Gitpod.

### Heruko 

Heruko is a cloud platform that can hosts dynamic web applications.Once you have the completed site in your own repository, you can deploy it to Heruko by the following steps.

1. Before you setup Heruko , you first need to create some files that are necessary for it to run on the Heruko server.
2. Open a terminal window in your IDE on the root folder of the project, run the command below, this will create a new file called procfile.

    `` echo web: python run.py > Procfile ``

3. Now run the command line below. this will create a new file called requirements.txt

    `` pip3 freeze --local > requirements.txt ``

4. Create a [Heruko user account](https://signup.heroku.com/login)
5. Click on the New button and choose Create a new app.
6. Input an app name and choose a region that is closest to you.
7. To input the necessary environmental variables, simply go to Settings tab, and under Config Vars, Click on Reveal Config Vars
8. Now you can deploy, the simplest way is to deploy from github, Click on the Deploy tab, Under Deployment method click on Github. A search window will prompt you to connect to the appropriate repository. You can then choose to do a manual or automatic deployment. 

### Local Deployment

If you prefer working on the repository locally on your preferred Desktop IDE, you can clone the repository to your desktop by the following steps.

1. Go to [the wildlife-rescue github page](https://github.com/kenwals/Wildlife-Rescue).
2. Above the list of files, click on the **code** button.
3. To clone the repository using **HTTPS,** under "Clone with HTTPS", click the paste icon.
   To clone the repository using an **SSH key**, click Use SSH, then click the paste icon.
   To clone a repository using **GitHub CLI,** click Use GitHub CLI, then click the paste icon.
4. Open your preferred Terminal interface.
5. Change the current working directory to the location where you want the cloned directory.
6. Type **git clone**, then paste the URL you copied earlier above.
7. Press Enter to create your local clone.
8. To run the app.py locally you will need to have a mongoDB account, with the supporting variables inputted in the env.py file,
 you may also need to install the packages listed Python app file.

more detailed instructions available [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Forking

You may wish to contribute to this website and have your contribution published, if so, you are welcome to follow these steps below.

1. Go to the GitHub website and log in.
2. Open <https://github.com/kenwals/Wildlife-Rescue>
3. In the top right-hand corner you will see a fork button, click on this **Fork button**.
4. This will create a copy of the Wildlife-Rescue repository in your Github account.
5. Once you're finished making changes you can locate the **New Pull Request** button just above the file listing in the original repository (<https://github.com/kenwals/wildlife-rescue>).
6. If your pull request is approved, it will be merged into the master version of the Wildlife-rescue repository at a future date.

more detailed instructions available [here](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)


## Credits

### Content

- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
        https://wildlife-incidents.com/ 
        http://irishwildlifematters.ie/animals/
- images are sourced from here https://diygarden.co.uk/wildlife/rescue-guide/ 
- The foundation of this site is sourced from Code Institute Educational material - Tim Nelson's Task Manager project.
 



### Resources

- Method for getting autocomplete working on the forms was based on [this article](https://gomakethings.com/how-to-create-a-form-input-autocomplete-without-a-library-or-framework/)

- The pagination code is taken and refactored from [here](https://github.com/smoodydev/flaskpaginate), it had been mentioned on slack by Ed.

- The method i used for making Case and profile pages read only was based on [this article](https://stackoverflow.com/questions/3507958/how-can-i-make-an-entire-html-form-readonly)

- [Cloudinary Widget info](https://cloudinary.com/documentation/upload_widget#api_events)

- [Bootstrap components](https://getbootstrap.com/)

- [W3schools](https://www.w3schools.com/)

- [Code institute's Slack workspace channels](https://slack.com)

- [Stack Exchange](https://stackexchange.com/)

- [MDN Web Docs](https://developer.mozilla.org/en-US/)

### Media

- images on front page are sourced from [here](https://diygarden.co.uk/wildlife/rescue-guide/)

### Acknowledgements

- I received inspiration for this project from Feargal Timon at https://wildlife-incidents.com/ and Galway swan rescue.
- Kudos to Ed Bradly for his excellent advice and tips on #data-centric-dev Slack channel and on the recorded zoom call from March.
