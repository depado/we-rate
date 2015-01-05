# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request
from flask.ext import admin, login
from flask.ext.login import LoginManager
from flask.ext.admin import Admin, expose, helpers
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

from app.decorators import superuser_required

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if login.current_user.is_authenticated():
            if login.current_user.is_superuser():
                return super(MyAdminIndexView, self).index()
        return redirect(url_for('index'))

admin = Admin(app, 'We Rate Movies', index_view=MyAdminIndexView())

from app.models import CategoryView, UserView, ReviewView, MovieView

admin.add_view(CategoryView(db.session, endpoint='category'))
admin.add_view(MovieView(db.session, endpoint='movie'))
admin.add_view(ReviewView(db.session, endpoint='review'))

from app import views, models