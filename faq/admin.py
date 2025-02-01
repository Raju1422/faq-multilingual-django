from django.contrib import admin
from .models import FAQ

# Register your models here.

class FAQadmin(admin.ModelAdmin):
    list_display=('question',)
    readonly_fields = ['translations']
   

admin.site.register(FAQ,FAQadmin)