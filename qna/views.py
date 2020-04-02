from django.shortcuts import render
from . import models


def questions(request):
    questions = models.Question.objects.filter(author=request.user).all()

    context = {
        'questions': questions,
        'yourquestions': True,
    }

    return render(request, 'qna/questions.html', context)


def latestquestions(request):
    questions = models.Question.objects.all().order_by('-created_at')

    context = {
        'questions': questions,
        'latestquestions': True,
    }

    return render(request, 'qna/latest-questions.html', context)