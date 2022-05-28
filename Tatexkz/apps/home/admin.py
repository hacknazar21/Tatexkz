from django.contrib import admin

from .models import Main_Slider, About, Pref, Pref_Slider, Questions, Questions_Title, Reviews, Reviews_Title, Settings
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Main_Slider)
class Main_Slider_Admin(TranslationAdmin):
    pass
@admin.register(About)
class AboutAdmin(TranslationAdmin):
    pass
@admin.register(Pref)
class PrefAdmin(TranslationAdmin):
    pass
@admin.register(Pref_Slider)
class Pref_SliderAdmin(TranslationAdmin):
    pass
@admin.register(Questions)
class QuestionsAdmin(TranslationAdmin):
    pass
@admin.register(Questions_Title)
class Questions_TitleAdmin(TranslationAdmin):
    pass
@admin.register(Reviews_Title)
class Reviews_TitleAdmin(TranslationAdmin):
    pass

admin.site.register(Reviews)
admin.site.register(Settings)