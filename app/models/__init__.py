# -*- coding: utf-8 -*-

# Make the AuthMixin available
from .mixins import AuthMixin

# Make the models available
from .user import User, UserView
from .category import Category, CategoryView, categories
from .movie import Movie, MovieView
from .review import Review, ReviewView
