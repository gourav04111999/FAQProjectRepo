from django.db import models
from googletrans import Translator
from ckeditor.fields import RichTextField

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

        
        if lang == 'hi' and self.question_hi:
            translation = self.question_hi
        elif lang == 'bn' and self.question_bn:
            translation = self.question_bn
        else:
            translation = translator.translate(self.question, dest=lang).text if lang != 'en' else self.question
            
        return translation

    def __str__(self):
        return self.question