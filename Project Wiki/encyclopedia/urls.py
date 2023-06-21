from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entryPageUrl"),
    path("search/", views.searchPage, name="searchPageUrl"),
    path("new/", views.newPage, name="newPageUrl"),
    path("edit/", views.editPage, name="editPageUrl" ),
    path("save/", views.saveEdit, name="saveEditUrl" ),
    path("random/", views.randomPage, name="randomPageUrl"),
]