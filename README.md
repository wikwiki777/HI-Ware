[![Build Status](https://travis-ci.org/wickyakloe/HI-Ware.svg?branch=master)](https://travis-ci.org/wickyakloe/HI-Ware)

# HI-Ware
### <i>Webshop for High-End Computer Hardware</i>

![ResponsiveView](https://raw.githubusercontent.com/wickyakloe/HI-Ware/master/assets/previewimage.png "Mobile and Desktop preview")

## Goal:
Use Django3 to create a website for anyone who is<br>
interested in purchasing High-End computer hardware.

Table of Contents:

- [Features](#features)
- [UX/UI](#ux)
- [Database](#database)
  - [Postgresql](#mongodb)
    - [Creating the Database](#creating-the-database)
    - [ER Diagram](#er-diagram)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Local](#local-deployment)
- [Credits](#credits)
- [Media](#media)

## User stories

The following user stories follow the template:<br>

```userstory
As a <type of user>, i want <some goal> so that <some reason>
```

Site users:

| Type of user  | Definition |
| ------------- | ---------- |
|Visitor        | Anonymous user browsing/using the site |
|Customer       | Registered user who wants to buy the products on the site |
|Admin          | Registered user who maintains/owns the site  |


Stories:

DONE:
- As a Visitor, i want to browse all products<br>
so that i can get information on what i'm looking for.

- As a Visitor, i want to search in all products<br>
so that i only get what i'm looking for.

- As a Visitor, i want to filter on products<br>
so that i only see the products i'm looking for.

- As a Visitor, i want to see detailed information on a product<br>
so that i can decide if thats the product i want.

- As a Visitor, i want to add products to a cart<br>
so that i'm able to view or purchase them.

- As a Customer, i want to add products to a cart<br>
so that i can view or purchase them now or later.

- As a Customer, i want to view my profile page <br>
so that i can see if my information is correct, if its not correct
i should be able to amend it.

- As a Admin, i want to add products<br>
so that i can add new products the customer is able to buy.

- As a Admin, i want to amend products<br>
so that i can add/remove or update product information.

TODO:
- As a Customer, i want to rate and review a product<br>
so that the site owner and other potential customers know how satisfied i am
or not.

- As a Customer, i want my shipping details prefilled if they
are set in my profile.

## UX

### [Mockup](https://wickyakloe.github.io/HI-Ware/assets/mockup/)

## Technologies Used

- HTML
- CSS
- Javascript
- Python3
- Postgresql
- AmazonS3

Modules/Frameworks:

- Django3
- Bootstrap4
- Stripe

## Database
### Postgresql

Tables in db:
- User
- Profile
- Category
- Product
- BaseProduct
- Order


![ResponsiveView](https://raw.githubusercontent.com/wickyakloe/HI-Ware/master/assets/djappmodels.png "HI-Ware Database ERM")

Generated using
[django-extensions](https://github.com/django-extensions/django-extensions)

## Testing

View the test coverage [here](https://wickyakloe.github.io/HI-Ware/assets/htmlcov/)

## Deployment

### Heroku
This application is deployed to heroku here [https://wickz-hiware.herokuapp.com/](https://wickz-hiware.herokuapp.com/).

When deploying to heroku use the following config vars

| Variable        |
| --------------- |
|AWS_SECRET_ACCESS_KEY|
|AWS_SECRET_KEY_ID|
|DATABASE_URL| 
|DISABLE_COLLECTSTATIC| 
|EMAIL_ADDRESS| 
|EMAIL_PASSWORD|
|SECRET_KEY|
|STRIPE_PUBLISHABLE|
|STRIPE_SECRET|

### Local

- Clone this repo `git clone https://github.com/wickyakloe/HI-Ware.git`
or [download](https://github.com/wickyakloe/HI-Ware/archive/master.zip) and unzip into a directory or python3 virtualenv

- Install the project dependancies with `pip install -r requirements.txt`
Note u may encounter errors with psycopg2 make sure u install the dependencies of these packages and then reinstall with the above command.

- Create the following `.env` file in the root directory

```.env
# Environment variables used by python-dotenv
# Put variables here and use with os.getenv()

# Comment DEVELOPEMENT out or set to empty for DEBUG = False
DEVELOPMENT=1

# settings.py - Secret key
# generate one here https://miniwebtool.com/django-secret-key-generator/
SECRET_KEY=""

# settings.py
# Dev DB
DEV_DATABASE_URL="postgres://"
# Prod DB
DATABASE_URL="postgres://"

# Stripe api secret key - Copy from your account
STRIPE_SECRET=""
STRIPE_PUBLISHABLE =""

# AWS S3 - - Copy from your account
AWS_SECRET_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""

# Email - - Copy from your account
EMAIL_ADDRESS=""
EMAIL_PASSWORD=""
```

- Migrate with `./manage.py migrate`

- Run the server locally  `./manage.py runserserver`

## Credits
- Thanks to uxwing.com for providing the free [icon](https://uxwing.com/microchip-icon/)
- codeinstitute.net
## Media
- Media and prices are related to products are fictional and the content
you see is from the manufacturer site.