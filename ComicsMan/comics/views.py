# TODO Проверить slider_list на нечётность.

from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics, Slide


class ComicsView(View):
    """Список комиксов."""

    def get(self, request):
        slider = []
        comics = Comics.objects.all()
        slider_list = list(Slide.objects.all())
        for i in range(0, len(slider_list), 2):
            slider.append([slider_list[i], slider_list[i + 1]])
        print(slider)
        return render(request, "comics/index.html",
                      {"comics_list": comics, "header_slide_list": slider})
