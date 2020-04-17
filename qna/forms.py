from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ('title', 'description', 'code','tags')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ('description', 'code')

