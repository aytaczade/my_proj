from modeltranslation.translator import translator, TranslationOptions

from .models import About, Store


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'footer_description')


class StoreTranslationOptions(TranslationOptions):
    fields = ('name', 'address', )


translator.register(About, AboutTranslationOptions)
translator.register(Store, StoreTranslationOptions)