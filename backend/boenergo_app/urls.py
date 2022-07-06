from django.urls import path

from . import views


urlpatterns = [
        path("square_roots/", views.square_roots, name="square_roots"),
        path("probability/", views.probability, name="probability"),
        path("", views.index, name="index"),
]
