# -*- coding: utf-8 -*-

from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import AuthMixin


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name


categories = db.Table('categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)


class CategoryView(AuthMixin, ModelView):
    
    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)
