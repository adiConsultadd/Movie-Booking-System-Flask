from extensions import db

# Movie Model
class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(50), nullable=False)