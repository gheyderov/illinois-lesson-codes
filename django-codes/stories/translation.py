from modeltranslation.translator import translator, TranslationOptions
from stories.models import Recipe

class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Recipe, RecipeTranslationOptions)