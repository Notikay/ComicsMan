from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('all_comics/', views.AllComicsView.as_view(), name="all_comics")
]