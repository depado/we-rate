# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_user, logout_user, current_user

from app.decorators import superuser_required
from app.forms import LoginForm
from app.models import User
from app import app, db

@app.route('/', methods=['GET', 'POST'])
def index():
    context = {}
    if current_user.is_authenticated():
        context.update(user=current_user.login)
    return render_template('index.html', context=context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.session.query(User).filter_by(login=form.login.data).first()
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Wrong Login/Password.')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))
