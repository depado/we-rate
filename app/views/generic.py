# -*- coding: utf-8 -*-

from flask import render_template
from flask.views import View

from flask_login import current_user


class GenericPublicView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def generate_standard_context(self):
        context = dict()
        if current_user.is_authenticated():
            context.update(user=current_user.login)
        return context

    def fill_context(self, context):
        raise NotImplementedError()

    def dispatch_request(self):
        context = self.generate_standard_context()
        context = self.fill_context(context)
        return self.render_template(context)

