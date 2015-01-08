# -*- coding: utf-8 -*-

from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import AuthMixin


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


movie_categories = db.Table(
    'movie_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

serie_categories = db.Table(
    'serie_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('serie_id', db.Integer, db.ForeignKey('serie.id'))
)

book_categories = db.Table(
    'book_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

game_categories = db.Table(
    'game_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)


class CategoryView(AuthMixin, ModelView):

    column_descriptions = {
        'series': "Les séries associées à cette catégorie.",
        'movies': "Les films associées à cette catégorie.",
        'games': "Les jeux associés à cette catégorie",
    }

    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)
