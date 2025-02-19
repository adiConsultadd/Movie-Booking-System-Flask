# Movie Ticket Booking System
This movie booking system is a web application built with Flask that allows users to register, log in, view available movies, and perform CRUD operations on movie entries.

## Features
- User authentication (registration, login, logout)
- Movie management (create, view, update, delete movies)
- Database integration using SQLAlchemy and MySQL
- Migration support with Flask-Migrate

## Technologies and Libraries
- Backend Framework: Flask
- Templating Engine: Jinja2
- Database: MySQL
- ORM: SQLAlchemy
- User Authentication: Flask-Login
- Database Migrations: Flask-Migrate

## Steps to Set Up Locally

#### Create and activate a virtual environment:
``` bash
python -m .venv venv
. .venv/bin/activate
```

#### Install dependencies:
```bash
pip install -r requirements.txt
```

#### Configure Config File: 
```bash
import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
```
#### Create .env File
```bash
'DATABASE_URL' = '************************'
'SECRET_KEY' = '*******************'
```

#### Running the Application
```bash
python app.py
```
## Project Structure
``` bash
movie-booking-system/
│
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── userModel.py
│   └── movieModel.py
├── routes/
│   ├── authRoutes.py
│   └── movieRoutes.py
├── templates/
│   ├── home.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   └── movies/
│       ├── add_movie.html
│       ├── edit_movie.html
│       └── view_movie.html
├── static/
│   └── styles/
│       ├── home.css
│       ├── login.css
│       ├── register.css
│       ├── add_movie.css
│       ├── edit_movie.css
│       └── view_movie.css
├── migrations
├── requirements.txt
└── README.md
```