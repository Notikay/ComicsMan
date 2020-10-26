from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Comics, News, Reviews, Rating, Favorites

comics = Comics.objects.all()
comics_list = list(comics)
comics_len = len(comics_list)

stars_len = 5

rating = Rating.objects.all()
rating_dict = {key.title: [0, 0, 0] for key in comics}
for comics_ in rating:
    rating_dict[comics_.comics.title][0] += comics_.star.value
    rating_dict[comics_.comics.title][1] += 1
    rating_dict[comics_.comics.title][2] = round(
        rating_dict[comics_.comics.title][0] /
        rating_dict[comics_.comics.title][1]
    )

class HomeView(View):
    """Главная"""

    def __init__(self):
        self.reviews = Reviews.objects.all()
        self.favorites = Favorites.objects.all()
        self.news = News.objects.last()

        self.reviews_len = len(self.reviews)

        self.header_slider_len = 8
        self.new_rel_len = 8
        self.reviews_slider_len = 6

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
        header_slider_list, self.header_slider_len = self.checkObject(comics_list, comics_len, self.header_slider_len)
        new_rel, self.new_rel_len = self.checkObject(comics_list, comics_len, self.new_rel_len)
        reviews_list, self.reviews_slider_len = self.checkObject(self.reviews, self.reviews_len, self.reviews_slider_len)

        header_slider = self.distribution(header_slider_list, self.header_slider_len)
        reviews_slider = self.distribution(reviews_list, self.reviews_slider_len)

        return render(request, "comics/pages/home.html",
                      {
                          "header_slider_len": range(self.header_slider_len),
                          "header_slider": header_slider,

                          "reviews_slider_len": range(self.reviews_slider_len),
                          "reviews_slider": reviews_slider,

                          "comics_len": range(comics_len),
                          "comics_list": comics,

                          "new_rel": new_rel,
                          "favor_rel": self.favorites,

                          "rating_dict": rating_dict,
                          "stars": range(stars_len),

                          "date": self.date,
                          "news": self.news,
                      })

class AllComicsView(View):
    """Все комиксы"""

    def __init__(self):
        self.comics_page_len = 3

        self.current_datetime = datetime.now()
        self.date = f"{self.current_datetime.strftime('%B')} {self.current_datetime.day}: "

    def get(self, request):
        paginator = Paginator(comics, self.comics_page_len)
        page = request.GET.get('page')

        try:
            comics_page = paginator.page(page)
        except PageNotAnInteger:
            comics_page = paginator.page(1)
        except EmptyPage:
            comics_page = paginator.page(paginator.num_pages)

        return render(request, "comics/pages/all_comics.html",
                      {
                          "page": page,
                          "comics_page": comics_page,

                          "rating_dict": rating_dict,
                          "stars": range(stars_len),

                          "date": self.date
                      })