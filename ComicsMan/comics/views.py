from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics

class AppIndexView(View):
    """Для главной станицы."""

    def __init__(self):
        self.slider = []

        self.comics = Comics.objects.all()
        self.comics_list = list(self.comics)
        self.comics_length = len(self.comics_list)

        self.new_releases_length = 8

        self.current_datetime = datetime.now()
        self.date = f"{self.current_datetime.strftime('%B')} {self.current_datetime.day}: "

    def get(self, request):

        if self.comics_length < self.new_releases_length:
            new_releases = self.comics_list[:self.comics_length]
        else:
            new_releases = self.comics_list[:self.new_releases_length]

        for i in range(0, self.comics_length, 2):
            if self.comics_length % 2 != 0 and i == self.comics_length - 1:
                self.slider.append([self.comics_list[i]])
            else:
                self.slider.append([self.comics_list[i], self.comics_list[i + 1]])

        return render(request, "comics/apps/app_index.html",
                      {
                          "header_slide_list": self.slider,
                          "comics_length": range(self.comics_length),
                          "comics_list": self.comics,
                          "date": self.date,
                          "new_releases": new_releases,
                      })