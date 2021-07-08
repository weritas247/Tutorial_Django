from django.urls import path
from django.urls.resolvers import URLPattern
from catalog import views

urlpatterns =[
  path("", views.index, name="index"),
]


