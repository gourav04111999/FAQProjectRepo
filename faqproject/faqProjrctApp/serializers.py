# # serializers.py
# from rest_framework import serializers
# from .models import FAQ

# class FAQSerializer(serializers.ModelSerializer):
#     """
#     Serializer for FAQ model, includes dynamic translation based on the language.
#     """
#     question = serializers.SerializerMethodField()

#     def get_question(self, obj):
#         """
#         Return the question in the selected language.
#         """
#         lang = self.context.get('lang', 'en')  # Get language from context
#         return obj.get_translated_text(lang)  # Fetch translated text for the selected language

#     class Meta:
#         model = FAQ
#         fields = ['question', 'answer']
