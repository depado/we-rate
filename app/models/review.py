# -*- coding: utf-8 -*-

from flask.ext.admin.contrib.sqla import ModelView

from app.models import AuthMixin
from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer)
    critic = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __repr__(self):
        return "{}".format(self.user)


class ReviewView(AuthMixin, ModelView):
    
    def __init__(self, session, **kwargs):
        super(ReviewView, self).__init__(Review, session, **kwargs)
