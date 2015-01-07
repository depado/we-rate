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


class CategoryView(AuthMixin, ModelView):
    
    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)
