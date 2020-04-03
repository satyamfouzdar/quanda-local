from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required


@login_required
def questions(request):
    questions = models.Question.objects.filter(author=request.user).all()

    context = {
        'questions': questions,
        'yourquestions': True,
    }

    return render(request, 'qna/questions.html', context)


@login_required
def latestquestions(request):
    questions = models.Question.objects.all().order_by('-created_at')

    context = {
        'questions': questions,
        'latestquestions': True,
    }

    return render(request, 'qna/latest-questions.html', context)