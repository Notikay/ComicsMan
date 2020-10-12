# TODO Отдельный список для популярного.

from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics

class AppIndexView(View):
    """Для главной станицы."""

    def __init__(self):
        self.comics = Comics.objects.all()
        self.comics_list = list(self.comics)
        self.comics_len = len(self.comics_list)

        self.header_slider_len = 8
        self.new_rel_len = 8
        self.favor_rel_len = 7

        self.current_datetime = datetime.now()
        self.date = f"{self.current_datetime.strftime('%B')} {self.current_datetime.day}: "

    def checkComics(self, element_len):
        if self.comics_len < element_len:
            result = self.comics_list[:self.comics_len]
            element_len = self.comics_len
        else:
            result = self.comics_list[:element_len]
        return [result, element_len]

    def get(self, request):
        header_slider = []
        header_slider_list, self.header_slider_len = self.checkComics(self.header_slider_len)
        new_rel, self.new_rel_len = self.checkComics(self.new_rel_len)
        favor_rel, self.favor_rel_len = self.checkComics(self.favor_rel_len)

        for i in range(0, self.header_slider_len, 2):
            if self.header_slider_len % 2 != 0 and i == self.header_slider_len - 1:
                header_slider.append([header_slider_list[i]])
            else:
                header_slider.append([header_slider_list[i], header_slider_list[i + 1]])

        return render(request, "comics/apps/app_index.html",
                      {
                          "header_slider_len": range(self.header_slider_len),
                          "header_slider": header_slider,

                          "comics_len": range(self.comics_len),
                          "comics_list": self.comics,

                          "new_rel": new_rel,
                          "favor_rel": favor_rel,

                          "date": self.date,
                      })