from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.toAdd, name="toAdd"),
    path("add/", views.add, name="add"),
]
