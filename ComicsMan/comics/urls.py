from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppIndexView.as_view())
]