# -*- coding: utf-8 -*-

# Make the AuthMixin available
from .mixins import AuthMixin

# Make the models available
from .user import User, UserView
from .movie import Movie, MovieView
from .serie import Serie, SerieView
from .book import Book, BookView
from .category import Category, CategoryView, movie_categories, serie_categories
from .review import Review, ReviewView
