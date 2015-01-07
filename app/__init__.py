# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView, expose
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

from app.decorators import superuser_required

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated():
            if current_user.is_superuser():
                return super(MyAdminIndexView, self).index()
        return redirect(url_for('index'))

admin = Admin(app, 'We Rate Movies', index_view=MyAdminIndexView())

from app.models import CategoryView, UserView, ReviewView, MovieView

admin.add_view(CategoryView(db.session, endpoint='category'))
admin.add_view(MovieView(db.session, endpoint='movie'))
admin.add_view(ReviewView(db.session, endpoint='review'))

from app import views, models
