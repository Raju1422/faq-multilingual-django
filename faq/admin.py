from django.contrib import admin
from .models import FAQ

# Register your models here.

class FAQadmin(admin.ModelAdmin):
    list_display=('question','answer', 'created_at')
    readonly_fields = ['translations']
    search_fields = ['question', 'answer']
    list_filter = ('translations',) 
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Translations', {
            'fields': ('translations',),
            'classes': ('collapse',),
        }),
    )
   

admin.site.register(FAQ,FAQadmin)