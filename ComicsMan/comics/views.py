from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Comics, News, Reviews, Rating, Favorites

class HomeView(View):
    """Главная"""

    def __init__(self):
        self.reviews = Reviews.objects.all()
        self.comics = Comics.objects.all()
        self.favorites = Favorites.objects.all()
        self.news = News.objects.last()
        self.rating = Rating.objects.all()

        self.comics_list = list(self.comics)
        self.comics_len = len(self.comics_list)

        self.reviews = list(self.reviews)
        self.reviews_len = len(self.reviews)

        self.header_slider_len = 8
        self.new_rel_len = 8
        self.reviews_slider_len = 6
        self.stars_len = 5

        self.current_datetime = datetime.now()
        self.date = f"{self.current_datetime.strftime('%B')} {self.current_datetime.day}: "

    def checkObject(self, parent, parent_len, child_len):
        if parent_len < child_len:
            result = parent[:parent_len]
            child_len = parent_len
        else:
            result = parent[:child_len]
        return [result, child_len]

    def distribution(self, obj_list, obj_len):
        result = []
        for i in range(0, obj_len, 2):
            if obj_len % 2 != 0 and i == obj_len - 1:
                result.append([obj_list[i]])
            else:
                result.append([obj_list[i], obj_list[i + 1]])
        return result

    def get(self, request):
        rating_dict = {key.title:[0, 0, 0] for key in self.comics}
        for comics_ in self.rating:
            rating_dict[comics_.comics.title][0] += comics_.star.value
            rating_dict[comics_.comics.title][1] += 1
            rating_dict[comics_.comics.title][2] = round(rating_dict[comics_.comics.title][0]/rating_dict[comics_.comics.title][1])

        header_slider_list, self.header_slider_len = self.checkObject( self.comics_list, self.comics_len, self.header_slider_len)
        new_rel, self.new_rel_len = self.checkObject( self.comics_list, self.comics_len, self.new_rel_len)
        reviews_list, self.reviews_slider_len = self.checkObject(self.reviews, self.reviews_len, self.reviews_slider_len)

        header_slider = self.distribution(header_slider_list, self.header_slider_len)
        reviews_slider = self.distribution(reviews_list, self.reviews_slider_len)

        return render(request, "comics/pages/home.html",
                      {
                          "header_slider_len": range(self.header_slider_len),
                          "header_slider": header_slider,

                          "reviews_slider_len": range(self.reviews_slider_len),
                          "reviews_slider": reviews_slider,

                          "comics_len": range(self.comics_len),
                          "comics_list": self.comics,

                          "new_rel": new_rel,
                          "favor_rel": self.favorites,

                          "rating_dict": rating_dict,
                          "stars": range(self.stars_len),

                          "date": self.date,
                          "news": self.news,
                      })

class NewReleasesView(View):
    """Новые релизы"""

    def __init__(self):
        self.current_datetime = datetime.now()
        self.date = f"{self.current_datetime.strftime('%B')} {self.current_datetime.day}: "

    def get(self, request):
        return render(request, "comics/pages/new_releases.html",
                      { "date": self.date })