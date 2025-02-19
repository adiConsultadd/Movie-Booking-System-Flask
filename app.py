from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager
from extensions import db
from routes.authRoutes import auth
from routes.movieRoutes import movies
from config import Config
from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()

def create_app():
    # Creating the app
    app = Flask(__name__)
    
    # Database Configurations
    app.config.from_object(Config)

    # Connect Database
    db.init_app(app)
    
    # Flask-Migrate Configuration
    migrate = Migrate(app, db)

    # Login Manager Setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Custom message for unauthorized access
    @login_manager.unauthorized_handler
    def unauthorized():
        flash("You need to log in to access this page.", "warning")
        return redirect(url_for("auth.login"))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Create All Database Tables
    with app.app_context():
        from models.userModel import User
        db.create_all()

    # Base Route
    @app.route('/')
    def home():
        return render_template('home.html')
    
    # Auth Routes (Login/Register/Logout->Users)
    app.register_blueprint(auth)

    # Movie Routes (View/Create/Update/Delete->Movies)
    app.register_blueprint(movies)
        
    return app

# Running this Flask Project
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
