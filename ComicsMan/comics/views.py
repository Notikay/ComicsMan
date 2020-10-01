from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics, Slide


class ComicsView(View):
    """Список комиксов."""

    def get(self, request):
        slider = []
        comics = Comics.objects.all()
        slider_list = list(Slide.objects.all())
        length = len(slider_list)
        for i in range(0, length, 2):
            if length % 2 != 0 and i == length - 1:
                slider.append([slider_list[i]])
            else:
                slider.append([slider_list[i], slider_list[i + 1]])
        return render(request, "comics/index.html",
                      {"comics_list": comics, "header_slide_list": slider})
