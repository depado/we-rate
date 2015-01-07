# -*- coding: utf-8 -*-

from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash

from flask.ext.admin.contrib.sqla import ModelView

from app.models import AuthMixin
from app import db, login_manager


class User(db.Model):
    """
    Simple User model. Integrates with Flask-Login.
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(54))
    is_superuser = db.Column(db.Boolean())
    is_active = db.Column(db.Boolean())

    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    def __init__(self, login, password, is_active=True, is_superuser=False):
        self.login = login
        self.is_superuser = is_superuser
        self.is_active = is_active
        self.set_password(password)

    def save(self):
        db.session.add(self)
        db.session.commit() 

    def is_superuser(self):
        return self.is_superuser

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return self.login

    def __unicode__(self):
        return self.login


class UserView(AuthMixin, ModelView):

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
