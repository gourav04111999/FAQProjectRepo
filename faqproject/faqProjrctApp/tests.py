#test.py
import pytest
from faqproject.faqProjrctApp.views import FAQEXAMPLE

@pytest.mark.django_db
def test_get_translated_text():
    faq = FAQEXAMPLE.objects.create(
        question="What is Django?",
        answer="A Python framework",
        question_hi="डjango क्या है?",
        answer_hi="एक पाइथन फ्रेमवर्क",
    )
    assert faq.get_translation('hi') == faq.question_hi
    assert faq.get_translation('bn') == faq.question # Fallback to English if Bengali translation is missing 