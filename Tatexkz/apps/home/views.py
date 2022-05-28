from unicodedata import name
from django.shortcuts import render
from .models import About, Main_Slider, Pref, Pref_Slider, Questions, Questions_Title, Reviews, Reviews_Title, Settings

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
    
    pref_title = Pref.objects.all()[0].pref_title
    q_title = Questions_Title.objects.all()[0].title
    rev_title = Reviews_Title.objects.all()[0].title

    settings = {
        'tel': Settings.objects.all()[0].tel,
        'tel_href': Settings.objects.all()[0].tel_href,
        'insta_name': Settings.objects.all()[0].insta_name,
        'insta_link': Settings.objects.all()[0].insta_link,
        'telegram_name': Settings.objects.all()[0].telegram_name,
        'telegram_link': Settings.objects.all()[0].telegram_link,
        'whatsapp_name': Settings.objects.all()[0].whatsapp_name,
    }
    

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
                                     'pref_title': pref_title,
                                     'pref_slides': slides_pref_for_temp,
                                     'reviews': slides_reviews_for_temp,
                                     'rev_title': rev_title,
                                     'questions': questions_for_temp,
                                     'q_title':q_title,
                                     'first_q': first_question_cat,
                                     'settings': settings}
    )
