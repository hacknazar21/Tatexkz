from unicodedata import name
from django.shortcuts import render
from .models import About, Main_Slider, Pref_Slider, Questions, Reviews

# Create your views here.


def home(request):
    slides = Main_Slider.objects.all()
    slides_pref = Pref_Slider.objects.all()
    slides_reviews = Reviews.objects.all()
    questions = Questions.objects.all()
    about = About.objects.all()
    slides_for_temp = []
    slides_pref_for_temp = []
    slides_reviews_for_temp = []
    questions_for_temp = {}
    about_for_temp = {
        'title': about[0].about_title,
        'text': about[0].about_text,
        'img': about[0].about_image
    }
    for slide in slides:
        slides_for_temp.append(
            {
                'id': slide.id,
                'title': slide.main_slider_title,
                'text': slide.main_slider_text,
                'img': slide.main_slider_image
            }
        )
    for slide in slides_pref:
        slides_pref_for_temp.append(
            {
                'id': slide.id,
                'title': slide.pref_slider_title,
                'text': slide.pref_slider_text,
                'img': slide.pref_slider_image
            }
        )
    for slide in slides_reviews:
        slides_reviews_for_temp.append(
            {
                'id': slide.id,
                'name': slide.reviews_name,
                'text': slide.reviews_text,
                'where': slide.reviews_where,
                'img': slide.reviews_image
            }
        )

    for question in questions:
        questions_for_temp[question.q_cat] = []

    for question in questions:
        questions_for_temp[question.q_cat].append(
            {
                'index': '0' + str(len(questions_for_temp[question.q_cat]) + 1),
                'title': question.q_title,
                'text': question.q_text
            }
        )

    first_question_cat = list(questions_for_temp.keys())[0]

    return render(
        request, 'home/index.html', {'main_slides': slides_for_temp,
                                     'about': about_for_temp,
                                     'pref_slides': slides_pref_for_temp,
                                     'reviews': slides_reviews_for_temp,
                                     'questions': questions_for_temp,
                                     'first_q': first_question_cat}
    )
