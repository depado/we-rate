# -*- coding: utf-8 -*-

from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from app import db
from .category import movie_categories
from .mixins import AuthMixin
from .review import Review


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    cover_url = db.Column(db.String)
    imdb_url = db.Column(db.String)
    allocine_url = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    view_date = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary=movie_categories, backref=db.backref('movies', lazy='dynamic'))
    reviews = db.relationship('Review', backref='movie', lazy='dynamic')

    def __repr__(self):
        return "<Movie Object> {id}, {title}".format(id=self.id, title=self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def last_reviews(limit):
        return Review.query.order_by(Review.date).filter(Review.movie_id.isnot(None)).limit(limit).all()


class MovieView(AuthMixin, ModelView):
    column_list = ('title', 'release_date', 'view_date')
    form_columns = [
        'title',
        'categories',
        'cover_url',
        'imdb_url',
        'allocine_url',
        'release_date',
        'view_date'
    ]

    column_descriptions = {
        'title': "Titre du film.",
        'categories': "Catégorie(s) du film.",
        'cover_url': "Une url qui pointe vers une image de l'affiche.",
        'imdb_url': "Url qui pointe vers la fiche IMDB du film.",
        'allocine_url': "Url qui pointe vers la fiche Allocine du film.",
        'release_date': "La date de sortie du film.",
        'view_date': "Date de vue du film. Automatiquement remplie à ajourd'hui si laissée vide."
    }

    def after_model_change(self, form, model, is_created):
        if is_created:
            if not model.view_date:
                model.view_date = datetime.now()
                model.save()

    def __init__(self, session, **kwargs):
        super(MovieView, self).__init__(Movie, session, **kwargs)
