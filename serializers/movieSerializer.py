from extensions import ma
from models.movieModel import Movie

class MovieSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Movie
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
    release_date = ma.auto_field()
    genre = ma.auto_field()