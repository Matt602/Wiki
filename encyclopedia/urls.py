from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("entry_edit/", views.entry_edit, name="entry_edit"),
    path("search/", views.search, name="search"),
    path("create/", views.toAdd, name="toAdd"),
    path("add/", views.add, name="add"),
    path("randomPage/", views.randomPage, name="randomPage"),
    path("<str:name>/", views.entry, name="entry"),
    path("wiki/<str:name>/", views.entry, name="entry"),
    path("<str:title>/toEdit/", views.toEdit, name="toEdit"),
    
]
