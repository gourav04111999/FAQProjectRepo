# views.py

# Admin Panel API Views
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from faqproject.faqProjrctApp.models import FAQEXAMPLE


@csrf_exempt
def admin_faq_view(request):
    if request.method == 'GET':
        faqs = list(FAQEXAMPLE.objects.values())
        return JsonResponse({'faqs': faqs})
    elif request.method == 'POST':
        data = json.loads(request.body)
        faq = FAQEXAMPLE.objects.create(question=data['question'], answer=data['answer'])
        return JsonResponse({'message': 'FAQ created', 'faq_id': faq.id})
