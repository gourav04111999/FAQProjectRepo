# admin.py
from django.contrib import admin
from faqproject.faqProjrctApp.models import FAQEXAMPLE


@admin.register(FAQEXAMPLE)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'question_bn')
