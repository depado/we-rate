# -*- coding: utf-8 -*-

from app import app

from app.models import Movie

from .generic import GenericPublicView


class MovieView(GenericPublicView):

    def fill_context(self, context):
        context.update(
            reviews=Movie.all_ordered()
        )
        return context

    def get_template_name(self):
        return "movie_list.html"

app.add_url_rule('/movies/', view_func=MovieView.as_view('movies'), endpoint="movies")
