from django.contrib import admin

from . import models

class AnswerSnippet(admin.StackedInline):
    model = models.AnswerSnippet


class AnswerInline(admin.StackedInline):
    model = models.Answer
    inlines = [AnswerSnippet]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)

    inlines = [
        AnswerSnippet,
    ]

class QuestionSnippetInline(admin.StackedInline):
    model = models.QuestionSnippet


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)

    inlines = [
        QuestionSnippetInline,
        AnswerInline,
    ]


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.QuestionSnippet)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.AnswerSnippet)