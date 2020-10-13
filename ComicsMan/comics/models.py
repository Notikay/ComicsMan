# TODO Модель для новостей.

from datetime import date

from django.db import models


class AuthorAndPainter(models.Model):
    """Авторы и художники."""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="img/author_painter/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Авторы и художники"
        verbose_name_plural = "Авторы и художники"


class Personage(models.Model):
    """Персонаж."""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="img/personage/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"


class Genre(models.Model):
    """Жанр."""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Publisher(models.Model):
    """Издатель."""
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


class Comics(models.Model):
    """Комикс."""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=200, null=True)
    description = models.TextField("Описание")
    image = models.ImageField("Обложка", upload_to="img/cover/")
    date = models.DateField("Дата выхода", default=date.today())
    country = models.CharField("Страна", max_length=70)
    publisher = models.ManyToManyField(Publisher, verbose_name="Издатель",
                                       related_name="comics_publisher")
    author = models.ManyToManyField(AuthorAndPainter, verbose_name="Автор",
                                    related_name="comics_author")
    painter = models.ManyToManyField(AuthorAndPainter, verbose_name="Художник",
                                     related_name="comics_painter")
    personages = models.ManyToManyField(Personage, verbose_name="Персонаж(и)",
                                        related_name="comics_personage")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комикс"
        verbose_name_plural = "Комиксы"


class Star(models.Model):
    """Звезда рейтинга."""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звёзды рейтинга"


class Raiting(models.Model):
    """Рейтинг."""
    ip = models.CharField("IP", max_length=15)
    star = models.ForeignKey(Star, on_delete=models.CASCADE,
                             verbose_name="Звезда")
    comics = models.ForeignKey(Comics, on_delete=models.CASCADE,
                               verbose_name="Комикс")

    def __str__(self):
        return f"{self.comics} - {self.star}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзыв."""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Отзыв", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель",
                               on_delete=models.SET_NULL, blank=True,
                               null=True)
    comics = models.ForeignKey(Comics, verbose_name="Комикс",
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.comics}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
