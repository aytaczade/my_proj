from modeltranslation.translator import translator, TranslationOptions

from .models import Category, Product, Campaign


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


class CampaignTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Campaign, CampaignTranslationOptions)