from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    translations = models.JSONField(default=dict, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Automatically generate translations if missing for other languages."""
        translator = Translator()
        languages = ['hi', 'bn', 'te'] 
        for lang in languages:
            if lang not in self.translations:
                translated_question = translator.translate(self.question, dest=lang).text
                translated_answer = translator.translate(self.answer, dest=lang).text
                
                self.translations[lang] = {
                    'question': translated_question,
                    'answer': translated_answer
                }

        super().save(*args, **kwargs)

    def get_translation(self, lang="en"):
        """Retrieve the question and answer in the requested language."""
        return self.translations.get(lang, self.translations.get('en'))

    def __str__(self):
        """Return the English question as the string representation of the FAQ."""
        return self.question
