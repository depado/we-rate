# -*- coding: utf-8 -*-

from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from app import db
from .category import serie_categories
from .mixins import AuthMixin


class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    cover_url = db.Column(db.String)
    imdb_url = db.Column(db.String)
    allocine_url = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    view_date = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary=serie_categories, backref=db.backref('series', lazy='dynamic'))
    reviews = db.relationship('Review', backref='serie', lazy='dynamic')

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class SerieView(AuthMixin, ModelView):
    column_list = ('title', 'release_date', 'view_date')
    form_columns = [
        'title',
        'categories',
        'cover_url',
        'imdb_url',
        'allocine_url',
        'release_date',
        'view_date',
        'reviews',
    ]

    column_descriptions = {
        'title': "Titre du film.",
        'categories': "Catégorie(s) du film.",
        'cover_url': "Une url qui pointe vers une image de l'affiche.",
        'release_date': "La date de sortie du film.",
        'view_date': "Date de vue du film. Automatiquement remplie à ajourd'hui si laissée vide."
    }

    def after_model_change(self, form, model, is_created):
        if is_created:
            if not model.view_date:
                model.view_date = datetime.now()
                model.save()

    def __init__(self, session, **kwargs):
        super(SerieView, self).__init__(Serie, session, **kwargs)
