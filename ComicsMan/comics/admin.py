from django.contrib import admin

from .models import AuthorAndPainter, Personage, Genre, Publisher, Comics, \
    Star, Rating, Reviews, News, Favorites

admin.site.register(AuthorAndPainter)
admin.site.register(Personage)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Comics)
admin.site.register(Star)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(News)
admin.site.register(Favorites)
