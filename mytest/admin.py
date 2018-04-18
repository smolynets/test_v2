from django.contrib import admin

from .models import *

class Version_questionInline(admin.TabularInline):
    model = Version_question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        Version_questionInline,
    ]    

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Version_question)
