from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class QuestionSnippet(models.Model):
    filename = models.CharField(max_length=100)
    code = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        self.modified_at = timezone.now()
        return super(QuestionSnippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.question.title

class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        return super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return self.question.title

class AnswerSnippet(models.Model):
    filename = models.CharField(max_length=100)
    code = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        self.modified_at = timezone.now()
        return super(QuestionSnippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.answer.question.title