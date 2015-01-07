# -*- coding: utf-8 -*-

from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def superuser_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated():
            if current_user.is_superuser():
                return f(*args, **kwargs)
        return redirect(url_for('index'))
    return decorated_function
