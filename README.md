# Django-Neighbourhood
A Django web application that allows registered users to know about everything happening in their current neighborhoods. Registered user must be a member to a given neighbourhood to post or see news related.

![](https://github.com/steve-njuguna-k/Django-Neighbourhood/blob/master/Screenshot.PNG)

## Presented By
- [Pervez Nagi](https://github.com/ismailPervez)
- [Steve Njuguna](https://github.com/steve-njuguna-k)

## Requirements
The user can perform the following functions:

- A user can sign in with the application to start using.
- A user can set up a profile about me and a general location and my neighborhood name.
- A user can find a list of different businesses in my neighborhood.
- A user can create posts that will be visible to everyone in my neighborhood.
- A user can change their neighborhood when I decide to move out.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.9.6

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Neighbourhood.git
```
2. cd into Django-Neighbourhood
```
cd Django-Neighbourhood
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

© 2022 Steve Njuguna & Pervez Nagi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
