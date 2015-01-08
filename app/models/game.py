# -*- coding: utf-8 -*-

from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from app import db
from .category import game_categories
from .platform import game_platforms
from .mixins import AuthMixin
from .review import Review


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    cover_url = db.Column(db.String)
    jeuxvideo_url = db.Column(db.String)
    ign_url = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    play_date = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary=game_categories, backref=db.backref('games', lazy='dynamic'))
    platforms = db.relationship('Platform', secondary=game_platforms, backref=db.backref('games', lazy='dynamic'))
    reviews = db.relationship('Review', backref='game', lazy='dynamic')

    def __repr__(self):
        return "<Game Object> {id}, {title}".format(id=self.id, title=self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def last_reviews(limit):
        return Review.query.order_by(Review.date).filter(Review.game_id.isnot(None)).limit(limit).all()

    @staticmethod
    def all_ordered():
        return Review.query.order_by(Review.date).filter(Review.game_id.isnot(None)).all()


class GameView(AuthMixin, ModelView):
    column_list = ('title', 'release_date', 'play_date')
    form_columns = [
        'title',
        'cover_url',
        'jeuxvideo_url',
        'ign_url',
        'release_date',
        'play_date',
        'categories',
    ]

    column_descriptions = {
        'title': "Titre du jeu.",
        'categories': "Catégorie(s) du jeu.",
        'cover_url': "Une url qui pointe vers une image de la jaquette.",
        'jeuxvideo_url': "Url qui pointe vers la fiche Jeuxvideo.com du film.",
        'ign_url': "Url qui pointe vers la fiche IGN du jeu.",
        'release_date': "La date de sortie du jeu.",
        'view_date': "Date de dernière partie sur le jeu. Automatiquement remplie à ajourd'hui si laissée vide."
    }

    def after_model_change(self, form, model, is_created):
        if is_created:
            if not model.view_date:
                model.view_date = datetime.now()
                model.save()

    def __init__(self, session, **kwargs):
        super(GameView, self).__init__(Game, session, **kwargs)
