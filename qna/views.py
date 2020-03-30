from django.shortcuts import render, redirect
from django.utils import timezone
from . import models, forms


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


def askaquestion(request):
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modified_at = timezone.now()
            question.save()
            return redirect(questions)

    else:
        form = forms.QuestionForm()
    context = {
        'form': form,
        'askaquestion': True,
    }

    return render(request, 'qna/ask-a-question.html', context)