# -*- coding: utf-8 -*-

from datetime import datetime
from flask.ext.admin.contrib.sqla import ModelView

from app import db
from app.models import AuthMixin
from app.models import categories


class Movie(db.Model):
    """
    Movie database model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    cover_url = db.Column(db.String)
    imdb_url = db.Column(db.String)
    allocine_url = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    pub_date = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary=categories, backref=db.backref('movies', lazy='dynamic'))
    reviews = db.relationship('Review', backref='movie', lazy='dynamic')

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

class MovieView(AuthMixin, ModelView):
    column_list = ('title', 'release_date')
    form_columns = [
        'title', 
        'categories',
        'cover_url', 
        'imdb_url', 
        'allocine_url', 
        'release_date', 
        'reviews', 
        'pub_date'
    ]

    column_descriptions = {
        'title': 'Titre du film.',
        'categories': 'Catégories du film.',
        'cover_url': "Une url qui pointe vers l'image de l'affiche du film.",
        'release_date': "La date de sortie du film",
        'pub_date': "Date de vue du film. Automatiquement remplie à ajourd'hui si laissée vide."
    }

    def after_model_change(self, form, model, is_created):
        if is_created:
            # If new movie, and not pub_date declared, then pub_date is now.
            if not model.pub_date:
                model.pub_date = datetime.now()
                model.save()

    def __init__(self, session, **kwargs):
        super(MovieView, self).__init__(Movie, session, **kwargs)