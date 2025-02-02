#models.py
from django.db import models
from googletrans import Translator
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

translator = Translator()


def sync_translate(text, dest):
    return translator.translate(text, dest=dest).text

class FAQEXAMPLE(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer"))
    question_hi = models.TextField(blank=True, null=True, verbose_name=_("Question in Hindi"))
    question_bn = models.TextField(blank=True, null=True, verbose_name=_("Question in Bengali"))
    # Add more language fields as needed

    def get_translation(self, lang='en'):
        cache_key = f'faq_{self.id}_lang_{lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        
        if lang == 'hi' and self.question_hi:
            translation = self.question_hi
        elif lang == 'bn' and self.question_bn:
            translation = self.question_bn
        else:
            translation = translator.translate(self.question, dest=lang).text if lang != 'en' else self.question
        
        cache.set(cache_key, translation, timeout=86400)  # Cache for 1 day

        return translation

    def __str__(self):
        return self.question
  
    # db changes
    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = sync_translate(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = sync_translate(self.question, 'bn')
        super().save(*args, **kwargs)