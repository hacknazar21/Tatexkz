from modeltranslation.translator import register, TranslationOptions
from .models import CoopSettings

@register(CoopSettings)
class CoopSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
