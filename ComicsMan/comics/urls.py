from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComicsView.as_view())
]