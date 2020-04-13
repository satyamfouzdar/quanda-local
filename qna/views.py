from django.shortcuts import render, redirect
from . import models
from . import forms
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


@login_required
def addquestion(request):

    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('questions')
    else:
        form = forms.QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'qna/addquestion.html', context)