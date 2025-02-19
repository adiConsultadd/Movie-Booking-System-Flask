from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from models.movieModel import Movie
from extensions import db
from datetime import datetime 

movies = Blueprint('movies', __name__)

# See All Movies
@movies.route('/movies', methods=['GET'])
@login_required
def view_movies():
    movies_list = Movie.query.all()
    return render_template('movies/view_movies.html', movies=movies_list)


# Add A New Movie
@movies.route('/movies/add', methods=["GET", "POST"])
@login_required
def add_movie():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        release_date = request.form.get("release_date")
        genre = request.form.get("genre")  
           
        if not title or not description or not release_date or not genre:
            flash("All fields are required!", "danger")
            return redirect(url_for("movies.add_movie"))

        try:
            release_date = datetime.strptime(release_date, "%Y-%m-%d").date()
        except Exception as e:
            flash("Invalid date format! Use YYYY-MM-DD.", "danger")
            return redirect(url_for("movies.add_movie"))
        
        new_movie = Movie(
            title=title,
            description=description,
            release_date=release_date,
            genre=genre
        )
        db.session.add(new_movie)
        db.session.commit()
        flash('Movie added successfully!', 'success')
        return redirect(url_for('movies.view_movies'))
    return render_template("movies/add_movie.html")

# Edit An Existing Movie
@movies.route('/movies/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movies/edit_movie.html', movie=movie)


# Update An Existing Movie
@movies.route('/movies/update/<int:movie_id>', methods=['POST'])
@login_required
def update_movie(movie_id):
    if request.method == "POST":
        movie = Movie.query.get_or_404(movie_id)
        movie.title = request.form.get('title')
        movie.description = request.form.get('description')
        movie.genre = request.form.get('genre')
        movie.release_date = datetime.strptime(request.form.get('release_date'), "%Y-%m-%d").date()
        db.session.commit()
        flash('Movie updated successfully!', 'success')
        return redirect(url_for('movies.view_movies'))

# Delete An Existing Movie
@movies.route('/movies/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Movie deleted successfully!', 'success')
    return redirect(url_for('movies.view_movies'))



