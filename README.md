# Wildlife Rescue Dublin

This is a [Data Centric web app](https://wildlife-rescue.herokuapp.com/) for a fictional wildlife animal rescue charity.

There are various wildlife charities that rescue or rehabilitate animals whom have been involved in accidents or become ill. Sometimes members of the public find these animals and become their carers.

A part of taking care of the animals is completing paperwork as the animal's care may requires licensing. The aim of this app is to make the process easier. Members of the public can register incident cases and the charity or Governing body can follow up.

![wildlife rescue page preview image](wireframe/wildlife-rescue-preview-image.png)

---

## Table of contents

- [UX](#ux)
  - [Scope](#scope)
    - [User Stories](#user-stories)
      - [Visitor goals](#visitor-goals)
      - [Owner goals](#owner-goals)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [Website page line up / Flask templates](#website-page-line-up---flask-templates)
    - [Non relational Database tables schema](#non-relational-database-tables-schema)
      - [cases table](#cases-table)
      - [User details table](#user-details-table)
      - [notes  table](#notes--table)
      - [reason  table](#reason--table)
      - [species table](#species-table)
      - [status table](#status-table)
      - [casenumbers table](#casenumbers-table)
    - [Wireframes](#wireframes)
  - [Surface](#surface)
    - [Colours](#colours)
    - [Icons](#icons)
    - [Images](#images)
    - [Fonts](#fonts)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Frontend](#frontend)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Tools](#tools)
- [Testing](#testing)
  - [Performance Testing](#performance-testing)
  - [Bugs encountered on the way](#bugs-encountered-on-the-way)
    - [Depreciated code warnings](#depreciated-code-warnings)
    - [Favicon handling in Python Flask](#favicon-handling-in-python-flask)
  - [Known issues](#known-issues)
    - [Pagination orientation problem](#pagination-orientation-problem)
  - [Project barriers and solutions](#project-barriers-and-solutions)
  - [Version control](#version-control)
  - [Functionality Testing](#functionality-testing)
  - [Responsiveness Testing](#responsiveness-testing)
  - [CSS3 validator](#css3-validator)
  - [HTML5 validator](#html5-validator)
  - [Python validator](#python-validator)
  - [JavaScript validator](#javascript-validator)
  - [Usability Testing](#usability-testing)
  - [Compatibility Testing](#compatibility-testing)
  - [Testing User Stories](#testing-user-stories)
    - [Visitor Stories](#visitor-stories)
    - [Owner Story](#owner-story)
- [Deployment](#deployment)
  - [GitHub](#github)
  - [Gitpod](#gitpod)
  - [Heruko](#heruko)
  - [Local Deployment](#local-deployment)
  - [Forking](#forking)
- [Credits](#credits)
  - [Content](#content)
  - [Resources](#resources)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## UX

### Scope

This is a fictional charity page, so there are no limitations on the content. The site will be made to an MVP first, and if there is additional time, content/features can be added.

#### User Stories

##### Visitor goals

1. As a user of this database , I want to be able to register myself a login easily.

2. As a user of this database , I want to be able to easily capture information on any mobile device.

3. As a user of this database , I want to edit case records I submitted.

4. As a user of this database , I want to be able to delete any information I created.

5. As a user of this database , I want to be able to search and filter results easily.

6. As a user of this database , I want to be able to edit my contact details.

7. As a user of this database , I want to be able to upload an image as part of my case.

8. As a user of this database , I want some of the form fields to autocomplete or auto suggest while i type.

##### Owner goals

1. As an owner of this database site, I want each case incident to have a unique case number.

2. As an owner of this database site, I want to be able to have a user with superuser read/write access , this user can have read/write access to all records.

3. As an owner of this database site, I want to be able to search and filter results easily.

### Structure

This Data centric site is put together with HTML, using the bootstrap framework along with some CSS.

The Database is done using Python and Flask fronted onto a MongoDB backend.

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

![DB schema chart](wireframe/db-flowchart.png)

The above diagram is just a visual guide of the database. The tables do not have forced relationships, as MongoDB is a non relational database. But some values in the cases table can linked to other tables which are used for dropdown lists on the cases input form.

I should mention the user is allowed to input species or reasons that doesn't appear on lists. Other fields are locked in to the list values in the associated tables. But can be over-riden by the MongoDB administrator in the background if needed.

##### cases table

```bash
_ID: (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
case_number: (auto-generated and used as reference for the case) STRING (INDEXED FIELD) (Not changeable) Value taken from casenumbers table sequence_value
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

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
full-name : STRING
username :  STRING (Not changeable)
password : STRING (Not changeable)
Phone: STRING
```

##### notes  table

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
case_id: ObjectId INDEXED (linked to cases table _id field )
date_time : datetimestamp
note: STRING
```

##### reason  table

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
reason: STRING
```

##### species table

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
species: STRING
```

##### status table

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
status: STRING
```

##### casenumbers table

```bash
_ID (auto-generated by MongoDB) ObjectId PRIMARY KEY (Not changeable)
sequence_value: INTEGER
```

#### Wireframes

![wireframe 1 homepage](wireframe/wireframe1-homepage.png)
![wireframe 2 all cases view](wireframe/wireframe2-all-cases-view.png)
![wireframe 3 case view](wireframe/wireframe3-case-view.png)

### Surface

#### Colours

![Colours referance](wireframe/wildlife-rescue-colour-referance.png)

Colour are natural and sourced from [a nature photo](https://photos.app.goo.gl/3nmoGsiUrAF82Fns5).

- #FFFFFD Black White - taken from the colour of the feathers of a Grey Heron bird
- #ADCE4B Turmeric - taken from Green river reeds on the River Liffey
- #6C6666 Dove Gray - taken from the colour of the feathers of a Grey Heron bird
- #FEE579 Kournikova  - taken from the colour of the beak of a Grey Heron bird
- #829B38 Sushi - a shade variation of Tumeric

![Colour swatches](wireframe/colour-swatch.png)
#### Icons

Bootstrap is used for icons

#### Images

images are sourced from here and here <https://diygarden.co.uk/wildlife/rescue-guide/>

#### Fonts

Font used is Rubik from Google fonts.

  ![font sample](wireframe/font-sample.png)

back to [contents](#table-of-contents)

---

## Features

### Existing Features

- Pagination on cases results page.
- Autocomplete on species and reason fields in the new case and edit case screen.
- Google places Autocomplete API integration on the case location field
- Security checks are made in the page routing code to ensure visitor is logged in, preventing brute force attacks.
- Filtered views on cases results cases such as my cases, pending cases and all open cases.
- Visitor can register , login and update their contact details
- Visitor has full CRUD access to each case they create.
- Unique case number is generated for each case
- Cloudinary image upload API integration case image field
- Each case has a notes journal , so case notes history can be audited.

### Features Left to Implement

- Refactor homepage layout , colours and images
- Change password functionality
- Portal to edit user access
- Firebase Authentication API

back to [contents](#table-of-contents)

---

## Technologies Used

### Frontend

#### Languages

- HTML
- CSS
- Python
- JavaScript

#### Libraries and Frameworks

- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- Fonts : [Google Fonts](https://fonts.google.com/)
- Icons : [Bootstrap](https://icons.getbootstrap.com/)

#### Tools

- JSfiddle : I used this online IDE to build and play with [Cloudinary API](https://jsfiddle.net/kenwals/8ze3u4ok/33/) and [Google places API](https://jsfiddle.net/kenwals/gv2oe4dp/8/) before i added them to this project confidently
- [Python Tutor](http://pythontutor.com/): I used this very handy virtual IDE for experimenting with Python code before applying to this project.
- [MongoDB compass](https://www.mongodb.com/products/compass): Really handy desktop application for viewing and easily maintaining my database configuration.
- Wireframe: [Balsamiq](https://balsamiq.com/)
- DB Schema diagram : [quick database diagrams](https://app.quickdatabasediagrams.com/#/d/myq6qw)
- IDE: Visual Studio Code (VS Code).
- Version control: Git
- Browser Developer tools : [Google Chrome](https://www.google.com/chrome) for console.logging everything.
- Kanban planner : [Github projects](https://github.com/kenwals/Wildlife-Rescue/projects/1).
- Markdown editor: [Typora](https://typora.io/) was used when appropriate, VS code editor was used for most updates.
- Markdown Preview Github Styling : this brilliant vscode extension helps me read my markdown in Github format.
- File renaming utility: PowerRename from [PowerToys on Windows 10](https://www.windowscentral.com/how-bulk-rename-your-files-windows-10-powertoys)
- Pomodoro timer : [Tomato Clock](https://chrome.google.com/webstore/detail/tomato-clock/enemipdanmallpjakiehedcgjmibjihj)
- Favicon creator : [favicon.io](https://favicon.io/favicon-generator/)
- Autoprefixer CSS : [Autoprefixer](https://autoprefixer.github.io/)
- Auto formatter for HTML, CSS and JS:  [webformatter](https://webformatter.com/html)
- px to rem convertor : [nekoCalc](https://nekocalc.com/px-to-rem-converter)
- JavaScript linter : [jshint](https://jshint.com/)
- Python linter :  [Pep8 online](http://pep8online.com/)
- markdown linter : markdownlint extension on VS Code.
- Colour names : [Name that color](https://chir.ag/projects/name-that-color/#6195ED)
- Colour swatches : [Coolors](https://coolors.co/)
- [markdown table of contents creator](https://ecotrust-canada.github.io/markdown-toc/)
- [site preview tool](http://ami.responsivedesign.is/)
- [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)
- [Microsoft Excel](https://www.microsoft.com/en-ww/microsoft-365/excel) : used for slicing and dicing wildlife species list.

back to [contents](#table-of-contents)

---

## Testing

I tested the site as I went along, manually testing or using automated online testing tools. I focused on getting the site working on a small mobile phone screen first (iPhone 5 simulation on the Chrome Developer tools), and then subsequently all other screen sizes. Print values to terminal was used a lot when working with Python. Consoling to log when working with JavaScript.

### Performance Testing

Page 1 - Home page

![page 1](wireframe/lighthouse-p1-home.png)

Page 2 - Case List Page

![page 2](wireframe/lighthouse-p2-cases.png)

Page 3 - New Case Page

![page 3](wireframe/lighthouse-p3-new-case.png)

Page 4 - View/Edit Case Page

![page 4](wireframe/lighthouse-p4-view-case.png)

Page 5 - Profile Page

![page 5](wireframe/lighthouse-p5-profile.png)

Page 6 - Login Page

![page 6](wireframe/lighthouse-p6-login.png)

Page 7 - Register Page

![page 7](wireframe/lighthouse-p7-register.png)

### Bugs encountered on the way

#### Depreciated code warnings

While i was developing this web app. I was seeing DeprecationWarning messages coming up in the terminal log. These warnings were coming up for commands such as count and update.  So all MongoDB commands you see in my app now are using the correct and current PyMongo syntax.

Example warning message:

```bash
DeprecationWarning: update is deprecated. Use replace_one, update_one or 
update_many instead. mongo.db.cases.update({"_id": ObjectId(case_id)}, { "$set": submit})
```

#### Google Places API warning

For a while during development I had an error message appearing occasionally in the console log for google places API, I thought it was some little glitch that wasn't important. But while refactoring the JavaScript to combine them in one script (if possible!), I realised I had the google API scripts loading backwards. I also had to abandon combining the scripts as they need to be loaded in a sequence that I can only achieve from the page load.

#### Favicon handling in Python Flask

Favicons was causing errors with flask in the early stages, but i eventually got them working for all devices by experimenting with the format I think Flask expected it to be.

### Known issues

#### Pagination orientation problem

For Pagination , I am using flask-paginate. At the time this project was being developed , this module didn't appear to support Bootstrap5. So I have had to configure it to Bootstrap4. I use CSS to hide a "Current Page" label section that was looking off. A Bootstrap offset container is also used as i was unable to center align the pagination otherwise.

#### Linting False warning messages that can be ignored

When Linting the Python code on PyLint a warning message appears stating "Possible unbalanced tuple". I believe this can be safely ignored, it's been discussed on the Slack Channels as being a standard message for Flask Pagination.

![pylint error message ](wireframe/lint-message-3.png)

For HTML linting, "Doctype must be declared first" can be ignored as the files are template blocks that join together with other blocks which have the Doctype info.

![HTML error message ](wireframe/lint-message-1.png)

On New case and view case pages, a tag must be paired warning is showing. Complying with this warning would result in all the dropdown list values appearing in duplicate. So this warning has to be ignored! .

![HTML error message ](wireframe/lint-message-2.png)

On the view case page, the warning below believes that there is a duplicate #id tag on the page , but only one #id tag shows on the rendered page as the image is displayed dynamically based on a If / ELSE statement in the Python / Jinja template code block.

![HTML error message ](wireframe/lint-message-4.png)

For the Google places API script , an "unused variable" linting error comes up for initAutocomplete . But the function is called by the other Google places script embedded on the page.

#### Case number verses Case _id

It might be worth flagging that case number and case _id are two seperate fields , which could get mixed up when being talked about in coversation with others, as they do have a one to one relationship. The difference is Case number is visible to the user and is in a human friendly format and is searchable for the user. case _id is unknown to the user, but the developer needs to use it when working with case and notes creation, editing and deletion.

### Project barriers and solutions

MongoDB verses PyMongo

When trying to make the case number increment based on code i read in the MongoDB manual, i couldn't get it working in my Python code. Googling the answer wasn't always leading me to the bottom of the problem, as I didn't realise PyMongo has a different syntax then MongoDB. But then i read [this article](https://stackoverflow.com/questions/17054494/pymongo-inc-having-issues/17054663). Hereby learning that PyMongo is slightly different from MongoDB!. So after this , i was back and forth between the two documentation sites , any useful MongoDB commands i needed to use i had to translate to PyMongo .

### Version control

For version control, I used the UI on VS Code for making git commits or the GitHub desktop app, Merging was done on the GitHub site. I used branches when I was working on new features or bundles of changes.

### Functionality Testing

Page 1 - Home page

Page 2 - Case List Page

Page 3 - New Case Page

Page 4 - View/Edit Case Page

Page 5 - Profile Page

Page 6 - Login Page

Page 7 - Register Page

Page 8 - 404 error Page

### Responsiveness Testing

For this test, I got a list of [15 most common screen sizes](https://www.designrush.com/trends/website-dimensions) and used [http://responsivetesttool.com/](http://responsivetesttool.com/) to check responsiveness for each screen size.

The results are below. 15 Passes.

| Device category | Model                 | Size Px (%popularity) | Result |
| --------------- | --------------------- | ------------------ | ------ |
| Desktop/Laptop  | NA                    | 1366x768 (22.98%)  | Pass   |
| Desktop/Laptop  | NA                    | 1920x1080 (20.7%)  | Pass   |
| Desktop/Laptop  | NA                    | 1536x864 (7.92%)   | Pass   |
| Desktop/Laptop  | NA                    | 1440x900 (7.23%)   | Pass   |
| Desktop/Laptop  | NA                    | 1280x720 (4.46%)   | Pass   |
| Mobile Phone    | Samsung Galaxy Note 4 | 360x640 (18.7%)    | Pass   |
| Mobile Phone    | Apple iPhone 6        | 375x667 (7.34%)    | Pass   |
| Mobile Phone    | Apple iPhone XR       | 414x896 (6.76%)    | Pass   |
| Mobile Phone    | Samsung Galaxy S8     | 360x780 (5.31%)    | Pass   |
| Mobile Phone    | Apple iPhone X        | 375x812 (5.01%)    | Pass   |
| Tablet          | Apple iPad            | 768x1024 (51.43%)  | Pass   |
| Tablet          | unknown               | 1280x800 (7.28%)   | Pass   |
| Tablet          | Samsung Galaxy Tab    | 800x1280 (5.26%)   | Pass   |
| Tablet          | Google Nexus 7        | 601x962 (4.32%)    | Pass   |
| Tablet          | unknown               | 962x601 (2.99%)    | Pass   |

### CSS3 validator

No errors.  Resource: <https://jigsaw.w3.org/css-validator/>

![CSS3 validation](wireframe/css-validation.png)

### HTML5 validator

No errors for pages listed below . Resource: <https://validator.w3.org/>

Page 1 - Home page

![Home page](wireframe/w3-html-checker-home.png)

Page 2 - Case List Page

![Cases list page](wireframe/w3-html-checker-cases.png)

Page 3 - New Case Page

![New case page](wireframe/w3-html-add-cases.png)

Page 4 - View/Edit Case Page

![View Edit case page](wireframe/w3-html-view-case.png)

Page 5 - Profile Page

![Profile page](wireframe/w3-html-profile.png)

Page 6 - Login Page

![Login page ](wireframe/w3-html-checker-login.png)

Page 7 - Register Page

![Register page](wireframe/w3-html-register.png)

Page 8 - 404 error Page

![404 error page](wireframe/w3-html-404.png)

### Python validator

no issues. results below. Resource:  <https://pep8online.com//>

![pep8 validation results](wireframe/pep8-python-check.png)

### JavaScript validator

no issues. results below. Resource:  <https://jshint.com/>

static\js\case-date-cut-off.js

```js

Metrics
There is only one function in this file.

It takes one argument.

This function contains 4 statements.

Cyclomatic complexity number for this function is 3.

```

static\js\case-edit.js

```js

Metrics
There are 2 functions in this file.

Function with the largest signature take 0 arguments, while the median is 0.

Largest function has 7 statements in it, while the median is 4.5.

The most complex function has a cyclomatic complexity value of 1 while the median is 1.

```

static\js\cloudinary.js

```js

Metrics
There are 2 functions in this file.

Function with the largest signature take 2 arguments, while the median is 1.

Largest function has 3 statements in it, while the median is 2.

The most complex function has a cyclomatic complexity value of 4 while the median is 2.5.

```

static\js\google-places.js

```js

There are 2 functions in this file.

Function with the largest signature take 0 arguments, while the median is 0.

Largest function has 3 statements in it, while the median is 2.5.

The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.

One unused variable
3 initAutocomplete

```

static\js\profile-edit.js

```js

Metrics
There are 2 functions in this file.

Function with the largest signature take 0 arguments, while the median is 0.

Largest function has 3 statements in it, while the median is 2.5.

The most complex function has a cyclomatic complexity value of 1 while the median is 1.
```

### Usability Testing

I shared the project on the peer-review channel on slack, and also with friends/family.

I tested and improved accessibility with lighthouse and Firefox developer tools.

### Compatibility Testing

| Screen size\Browser                          | Chrome | Firefox | Edge |
| -------------------------------------------- | ------ | ------- | ---- |
| Android Mobile phone (Screen width 412px) xs | Pass | Pass | Pass |
| Android Tablet (Screen width 600px) sm       | Pass | Pass | Pass |
| Windows laptop (Screen width 2560px)         |   Pass |  Pass |  Pass    |

### Testing User Stories

#### Visitor Stories

1. As a user of this database , I want to be able to register myself a login easily.

2. As a user of this database , I want to be able to easily capture information on any mobile device.

3. As a user of this database , I want to edit case records I submitted.

4. As a user of this database , I want to be able to delete any information I created.

5. As a user of this database , I want to be able to search and filter results easily.

6. As a user of this database , I want to be able to edit my contact details.

7. As a user of this database , I want to be able to upload an image as part of my case.

8. As a user of this database , I want some of the form fields to autocomplete or auto suggest while i type.

#### Owner Story

1. As an owner of this database site, I want each case incident to have a unique case number.

2. As an owner of this database site, I want to be able to have a user with superuser read/write access , this user can have read/write access to all records.

3. As an owner of this database site, I want to be able to search and filter results easily.

back to [contents](#table-of-contents)

---

## Deployment

For easy deployment on Heruko.com , you will need a GitHub user account and possibly a Gitpod user account. If you wish to make changes to this repository, please follow the GitHub steps first.

**Please note** this project contains several restricted APIs that will not work outside of this project without you refactoring in your own keys. Please check the current documentation for each API listed below.

- [MongoDB](https://www.mongodb.com/)
- [Google Places](https://developers.google.com/maps/documentation/places/web-service/overview)
- [Cloudinary](https://cloudinary.com/)

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

    ``` echo web: python run.py > Procfile ```

3. Now run the command line below. this will create a new file called requirements.txt

    ``` pip3 freeze --local > requirements.txt ```

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

back to [contents](#table-of-contents)

---

## Credits

### Content

- The foundation of this site is sourced from Code Institute Educational material - [Tim Nelson's Task Manager project (recently updated)](https://github.com/TravelTimN/flask-task-manager-project/tree/demo).
- Homepage text was sourced from [DIY Garden rescue guide](https://diygarden.co.uk/wildlife/rescue-guide/)
- Homepage text, lists of species, reasons, and statuses were sourced from the [wildlife incidents app](https://wildlife-incidents.com/)

### Resources

- Method used for getting autocomplete working on the forms was based on [this article](https://gomakethings.com/how-to-create-a-form-input-autocomplete-without-a-library-or-framework/)

- The pagination code is taken and refactored from Code Insitute tutor Stephen's repo [here](https://github.com/smoodydev/flaskpaginate), it had been mentioned on slack by Ed.

- The method i used for making Case and profile pages read only was based on [this article](https://stackoverflow.com/questions/3507958/how-can-i-make-an-entire-html-form-readonly)

- [Cloudinary Widget info](https://cloudinary.com/documentation/upload_widget#api_events) and [Cloudinary Academy - Introduction for API Users & Developers (One-Hour Course)](https://training.cloudinary.com/).

- [Google places autocomplet API info](https://developers.google.com/maps/documentation/javascript/places-autocomplete#add-autocomplete)

- Filters were created based on [this Stack Overflow post](https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes)

- [Bootstrap components](https://getbootstrap.com/)

- [W3schools](https://www.w3schools.com/)

- [Code institute's Slack workspace channels](https://slack.com)

- [Stack Exchange](https://stackexchange.com/)

- [MDN Web Docs](https://developer.mozilla.org/en-US/)

### Media

- Images on front page are sourced from [here](https://diygarden.co.uk/wildlife/rescue-guide/) and [here](https://unsplash.com/photos/b027q9eF3Yo)

### Acknowledgements

- I received inspiration for this project from Feargal Timon at the [wildlife incidents app](https://wildlife-incidents.com/) and Galway swan rescue.
- Kudos to Ed Bradly for his excellent advice and tips on #data-centric-dev Slack channel and on the recorded zoom call from March.
- My Mentor [Maranatha Ilesanmi](https://github.com/mbilesanmi) for helpful guidance and laser sharp attention to detail.
- Code Institute's [Tim Nelson](https://github.com/TravelTimN/) who gave me some useful pointers with this project.

back to [contents](#table-of-contents)
