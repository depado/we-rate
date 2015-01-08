# -*- coding: utf-8 -*-

from datetime import datetime

from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app.models import AuthMixin
from app import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer)
    critic = db.Column(db.UnicodeText)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    serie_id = db.Column(db.Integer, db.ForeignKey('serie.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return "{}".format(self.user)

    def save(self):
        db.session.add(self)
        db.session.commit()


class ReviewView(AuthMixin, ModelView):

    column_list = [
        'grade', 'user', 'movie', 'serie', 'book', 'date'
    ]

    form_columns = [
        'grade',
        'critic',
        'movie',
        'serie',
        'book',
    ]

    def after_model_change(self, form, model, is_created):
        """
        On modification or creation, set the date and the user
        """
        model.date = datetime.now()
        model.user_id = current_user.id
        model.save()

    def __init__(self, session, **kwargs):
        super(ReviewView, self).__init__(Review, session, **kwargs)
