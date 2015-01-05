from wtforms import validators
from wtforms.fields import TextField, PasswordField, SubmitField

from flask.ext.wtf import Form

from app.models import User
from app import db

class LoginForm(Form):
    login = TextField(validators=[validators.required()])
    password = PasswordField(validators=[validators.required()])
    submit = SubmitField('submit')

    def validate_login(self, field):
        user = db.session.query(User).filter_by(login=self.login.data).first()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not user.check_password(self.password.data):
            raise validators.ValidationError('Invalid password')