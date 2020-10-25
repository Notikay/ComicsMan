from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('new_releases/', views.NewReleasesView.as_view(), name="new_releases")
]