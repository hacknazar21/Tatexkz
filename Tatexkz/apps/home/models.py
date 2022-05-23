from django.db import models

# Create your models here.


class Main_Slider(models.Model):
    main_slider_title = models.CharField(
        max_length=50, verbose_name='Заголовок слайда')
    main_slider_text = models.CharField(
        max_length=50, verbose_name='Текст слайда')
    main_slider_image = models.ImageField(
        verbose_name='Картинка слайда', upload_to='static/img/first-screen')

    def __str__(self):
        return self.main_slider_title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class About(models.Model):
    about_title = models.CharField(
        max_length=50, verbose_name='Заголовок О нас')
    about_text = models.TextField(
        max_length=10000, verbose_name='Текст О нас')
    about_image = models.ImageField(
        verbose_name='Картинка О нас', upload_to='static/img/about')

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Pref_Slider(models.Model):
    pref_slider_title = models.CharField(
        max_length=50, verbose_name='Заголовок слайда')
    pref_slider_text = models.TextField(
        max_length=10000, verbose_name='Текст слайда')
    pref_slider_image = models.ImageField(
        verbose_name='Картинка слайда', upload_to='static/img/our-benefits')

    def __str__(self):
        return self.pref_slider_title

    class Meta:
        verbose_name = "Слайд преимущества"
        verbose_name_plural = "Слайды преимущества"


class Questions(models.Model):
    q_cat = models.CharField(
        max_length=50, verbose_name='Категория вопроса')
    q_title = models.TextField(
        max_length=50, verbose_name='Заголовок вопроса')
    q_text = models.TextField(
        max_length=5000, verbose_name='Текст вопроса')

    def __str__(self):
        return self.q_title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Reviews(models.Model):
    reviews_name = models.CharField(
        max_length=50, verbose_name='Должность и имя')
    reviews_text = models.TextField(
        max_length=10000, verbose_name='Текст отзыва')
    reviews_where = models.TextField(
        max_length=10000, verbose_name='Откуда сделан отзыв')
    reviews_image = models.ImageField(
        verbose_name='Картинка отзыва', upload_to='static/img/reviews')

    def __str__(self):
        return self.reviews_name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
