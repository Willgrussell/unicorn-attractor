Tracked with Travis! [![Build Status](https://travis-ci.org/Willgrussell/unicorn-attractor.svg?branch=master)](https://travis-ci.org/Willgrussell/unicorn-attractor)

# Unicorn Attractor Web Application
This web app is part of a larger application called Unicorn Attractor. The app is a built issue tracker for users to request bug fixes or new features they would like added.
Once a "Ticket" is raised, the user has the ability to review the ticket and pay for any work required. Bugs will be worked on for free, where as features will be chargable by time required.

## UX
- As an EXPERT user who wants to gain access to this site using authentication, creating a ticket with potential purchase of either feature development or bug fix.
- As a MODERATE user who would want bugs raised and fixed with a deadline.
- As a LOW user, i have searched your web application and interested in the productivity / speed of fixes. Interest in the promotions page.

### Wireframes
Please see [Wireframes](wireframes/) directory for images of screen layout plan and feel for site information. 

## Features
### Existing Features
- [Accounts app](accounts/): A new user will be able to register, login, logout and password authentication.
- [Search app](search/): User will have ability to search for a ticket using a search box in footer.
- [Home app](home/): Static pages that will hold index, contact and about pages.
- [Cart app](cart/): User can specify a ticket they want to hold in the cart before payment.
- [Checkout app](checkout/): User will have ability to pay for features by filling out a form and paying via a stripe.api
- [Promotions app](promotions/): This will display chart information showcasing the success of the issue tracker.
- [Tickets app](tickets/): User will complete a "Ticket" request form and specify a bug or feature. They will also have the ability to edit a ticket and update.

### New Features
- Coming soon!

## Technologies Used
* [Django](https://www.djangoproject.com) - The main project boilerplate
* [Bootstrap](http://getbootstrap.com) - Template layout and responsiveness with different devices
* [FontAwesome](https://fontawesome.com/?from=io) - Added icons to help users spot functions on webpage.
* [HighCharts](https://www.highcharts.com) - Third party software to assist database information to deply charts to template / browser.
* [SQL3lite](https://www.sqlite.org/index.html) - Backend Database for ticket information.
* [Pillow](https://pillow.readthedocs.io/en/5.3.x/) - Python library to assist with images used.
* [Django-forms-bootstrap]() - Python library to format layout for forms.
* [PycURL](http://pycurl.io) - Python library to assist fetch objects in python.
* [Travis](https://travis-ci.org) - Constant testing of web application
* [Heroku](https://www.heroku.com) - Hosting of web application

## Testing
Testing has been completed across this web app using the below methods.
- Responsiveness and browser testing
- Testing forms for errors manually. for example the contact form that is displayed on contact page.
1. Click contact URL.
2. Click submit on empty form and verify error. A message of about required fields should will appear.
3. Fill in form but with an invalid email address, an error will appear.
4. Fill in form with correct data, click submit and form will be posted.
- Travis, which will continously test the code for errors.

## Deployment
### Local - How to run this site locally.
- Open CLI and `pip3 install django==1.11` this will install the boilerplate.
- Download files from respository with requirements.txt which will have libraries used on project.
- From CLI `python3 manage.py runserver`.

### Hosting - web application has been hosted on **Heroku** and use of **AWS**
- Created app using Heroku on web and add Herokupostgres database
- Changes to config vars on Heroku, include environmental variables have been used to secure application.
- Install on CLI `dj-database-url` and `psycopg2` update requirements.txt
- Create Procfile to allow `Heroku` know this is a django application

## Demo
- A demo of this project is [stream-three-project](https://will-unicorn-attractor.herokuapp.com/)

## Credits
### Contents
* Payment Form on checkout page was copied from codeinstitute tutorial.

### Media
* Photos used on site were obtained from google.

### Acknowledges
* Codeinstitute - Inspiration from work completed on codeinstitute.

## Author
William Russell