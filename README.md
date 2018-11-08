Tracked with Travis! [![Build Status](https://travis-ci.org/Willgrussell/unicorn-attractor.svg?branch=master)](https://travis-ci.org/Willgrussell/unicorn-attractor)

# Unicorn Attractor Web Application
This web app is part of a larger application called Unicorn Attractor. This app is a built issue tracker for users to request bug fixes or new existing features they would like added.

## Features
### Existing Features
- Accounts app: A new user will be able to register, login, logout and password authentication.
- Search app: User will have ability to search for a ticket using a search box in footer.
- Home app: Static pages that will hold index, contact and about pages.
- Cart app: User can specify a ticket they want to hold in the cart before payment.
- Checkout app: User will have ability to pay for features by filling out a form and paying via a stripe.api
- Promotions app: This will display chart information showcasing the success of the issue tracker.
- Tickets app: User will complete a "Ticket" request form and specify a bug or feature. They will also have the ability to edit a ticket and update.

### New Features
- Coming soon!

## UX
- As an EXPERT user who wants to gain access to the site using authentication and creating a ticket and potential purchase of feature development or bug fixes.
- As a MODERATE user who would want bugs raised and fixed with a deadline.
- As a LOW user, i have searched your web application and interested in the productivity / speed of fixes. Interest in the promotions page.

### Wireframes
Images of design / layout of application, with drawings of project layout.

## Technologies Used
* [Django](https://www.djangoproject.com) - The main project boilerplate
* [Bootstrap](http://getbootstrap.com) - Template layout and responsiveness with different devices
* [FontAwesome](https://fontawesome.com/?from=io) - Added icons to help users spot functions on webpage.
* [FusionCharts](https://www.fusioncharts.com) - Third party software to assist database information to deply charts to template / browser.
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
* The local project

### Hosting - web application has been hosted on **Heroku**.
* Environmental variables have been used to ensure security across site.

## Credits
### Contents
* Payment Form on checkout page was copied from codeinstitute tutorial.

### Media
* Photos used on site were obtained from google.

### Acknowledges
* Codeinstitute - Inspiration from work completed on codeinstitute.

## Author
William Russell