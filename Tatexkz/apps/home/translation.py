from modeltranslation.translator import register, TranslationOptions
from .models import Main_Slider, About, Pref, Pref_Slider, Questions, Questions_Title, Reviews, Reviews_Title

@register(Main_Slider)
class Main_SliderTranslationOptions(TranslationOptions):
    fields = ('main_slider_title', 'main_slider_text','main_slider_image')
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('about_title', 'about_text','about_image')
@register(Pref)
class PrefTranslationOptions(TranslationOptions):
    fields = ('pref_title',)
@register(Pref_Slider)
class Pref_SliderTranslationOptions(TranslationOptions):
    fields = ('pref_slider_title','pref_slider_text', 'pref_slider_image')
@register(Questions_Title)
class Questions_TitleTranslationOptions(TranslationOptions):
    fields = ('title',)
@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('q_cat','q_title', 'q_text')
@register(Reviews_Title)
class Reviews_TitleTranslationOptions(TranslationOptions):
    fields = ('title',)
