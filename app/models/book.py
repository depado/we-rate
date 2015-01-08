# -*- coding: utf-8 -*-

from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from app import db
from .category import book_categories
from .mixins import AuthMixin
from .review import Review


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    cover_url = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    read_date = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary=book_categories, backref=db.backref('books', lazy='dynamic'))
    reviews = db.relationship('Review', backref='book', lazy='dynamic')

    def __repr__(self):
        return "<Book Object> {id}, {title}".format(id=self.id, title=self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def last_reviews(limit, by_date=True):
        return Review.query.order_by(Review.date).filter(Review.book_id.isnot(None)).limit(limit).all()


class BookView(AuthMixin, ModelView):
    column_list = ('title', 'release_date', 'read_date')
    form_columns = [
        'title',
        'cover_url',
        'release_date',
        'read_date',
        'reviews',
        'categories',
    ]

    column_descriptions = {
        'title': "Titre du livre.",
        'categories': "Catégorie(s) du livre.",
        'cover_url': "Une url qui pointe vers une image de la couverture.",
        'release_date': "La date de sortie du livre.",
        'view_date': "Date de lecture du livre. Automatiquement remplie à ajourd'hui si laissée vide."
    }

    def after_model_change(self, form, model, is_created):
        if is_created:
            if not model.view_date:
                model.view_date = datetime.now()
                model.save()

    def __init__(self, session, **kwargs):
        super(BookView, self).__init__(Book, session, **kwargs)
