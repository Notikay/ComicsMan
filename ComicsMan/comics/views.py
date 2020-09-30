from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics, Slide


class ComicsView(View):
    """Список комиксов."""

    def get(self, request):
        comics = Comics.objects.all()
        slider = Slide.objects.all()
        return render(request, "comics/index.html",
                      {"comics_list": comics, "header_slide_list": slider})
