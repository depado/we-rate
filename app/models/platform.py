# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import AuthMixin


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Platform Object> {id}, {name}".format(id=self.id, title=self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()


game_platforms = db.Table(
    'game_platforms',
    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)


class PlatformView(AuthMixin, ModelView):

    column_descriptions = {
        'games': "Les jeux associés à la plateforme.",
    }

    def __init__(self, session, **kwargs):
        super(PlatformView, self).__init__(Platform, session, **kwargs)
