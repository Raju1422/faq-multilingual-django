from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields =["id","question","answer","translations","created_at"]
        read_only_fields = ["translations"]

    def to_representation(self, instance):
        lang = self.context.get('lang','en')
        data = super().to_representation(instance)
        data.pop('translations',None)
        data.pop('question',None)
        data.pop('answer',None)
        if lang == "en":
            data['en']={
                'question': instance.question,
                'answer': instance.answer
            }
        else:
            translated_data = instance.translations.get(lang, {})
            data[lang] = translated_data
            
        return data