from django.contrib import admin

from . import models


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)