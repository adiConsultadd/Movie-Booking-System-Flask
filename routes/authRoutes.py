from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from extensions import db
from models.userModel import User

bcrypt = Bcrypt()

auth = Blueprint('auth', __name__)

# Login Route
@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('movies.view_movies'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('auth/login.html')

# Register Route
@auth.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.register'))
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

# Logout Route
@auth.route('/auth/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
