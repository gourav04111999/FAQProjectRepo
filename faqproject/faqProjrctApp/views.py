# views.py

# Admin Panel API Views
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import FAQEXAMPLE

@csrf_exempt
def admin_faq_view(request):
    if request.method == 'GET':
        faqs = list(FAQEXAMPLE.objects.values())
        lang = request.GET.get('lang', 'en') 
        print(lang)
        if(lang == 'hi'):
         faq_hi = [{'question': faq['question_hi'], 'answer': faq['answer']} for faq in faqs]
         return JsonResponse({'faqs': faq_hi})
        elif(lang == 'bn'):
         faq_bn = [{'question': faq['question_bn'], 'answer': faq['answer']} for faq in faqs]
         return JsonResponse({'faqs': faq_bn})
        else:
         faq_def = [{'question': faq['question'], 'answer': faq['answer']} for faq in faqs]
         return JsonResponse({'faqs': faq_def})
    elif request.method == 'POST':
        data = json.loads(request.body)
        faq = FAQEXAMPLE.objects.create(question=data['question'], answer=data['answer'])
        return JsonResponse({'message': 'FAQ created', 'faq_id': faq.id})
    
# JavaScript & HTML template for the Admin Panel
admin_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin FAQ Panel</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { text-align: center; }
        .faq-container { width: 80%; margin: 0 auto; }
        .faq-item { border: 1px solid #ccc; border-radius: 8px; padding: 10px; margin: 10px 0; background: #f9f9f9; }
        .faq-item h3 { margin: 0; color: #333; }
        .faq-item p { margin: 5px 0; }
        .form-container { margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 8px; background: #f1f1f1; }
        input, textarea, button { display: block; width: 100%; margin-top: 10px; padding: 8px; }
        button { background-color: #28a745; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #218838; }
    </style>
    <script>
        async function fetchFAQs() {
            const response = await fetch('/faqs/');
            const data = await response.json();
            let faqList = document.getElementById('faq-list');
            faqList.innerHTML = '';
            data.faqs.forEach(faq => {
                let faqItem = document.createElement('div');
                faqItem.classList.add('faq-item');
                faqItem.innerHTML = `
                    <h3>${faq.question}</h3>
                    <p><strong>Answer:</strong> ${faq.answer}</p>
                    <p><strong>Hindi:</strong> ${faq.question_hi || 'Not available'}</p>
                    <p><strong>Bengali:</strong> ${faq.question_bn || 'Not available'}</p>
                `;
                faqList.appendChild(faqItem);
            });
        }
        
        async function addFAQ() {
            const question = document.getElementById('question').value;
            const answer = document.getElementById('answer').value;
            await fetch('/faqs/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question, answer })
            });
            fetchFAQs();
        }
        
        document.addEventListener("DOMContentLoaded", fetchFAQs);
    </script>
</head>
<body>
    <h1>Admin FAQ Panel</h1>
    <div class="faq-container" id="faq-list"></div>
    
    <div class="form-container">
        <h2>Add New FAQ</h2>
        <input type="text" id="question" placeholder="Enter question">
        <textarea id="answer" placeholder="Enter answer"></textarea>
        <button onclick="addFAQ()">Add FAQ</button>
    </div>
</body>
</html>
'''

from django.http import HttpResponse

def admin_faq_page(request):
    return HttpResponse(admin_template)

