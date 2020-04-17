from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from users.models import User


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    code = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()
    tags =  TaggableManager()
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField(blank=True)
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
