from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from taggit.models import Tag

@login_required
def questions(request):
    questions = models.Question.objects.filter(author=request.user).all()
    query_count = models.Question.objects.filter(author=request.user).all().count()
    common_tags =  models.Question.tags.most_common()[:5]
    context = {
        'questions': questions,
        'common_tags':common_tags,
        'query_count': query_count,
        'yourquestions': True,
    }
    return render(request, 'qna/questions.html', context)


@login_required
def latestquestions(request):
    questions = models.Question.objects.all().order_by('-created_at')
    query_count = models.Question.objects.filter(author=request.user).all().count()
    common_tags =  models.Question.tags.most_common()[:5]
    context = {
        'questions': questions,
        'common_tags':common_tags,
        'query_count': query_count,
        'latestquestions': True,
    }
    return render(request, 'qna/latest-questions.html', context)


@login_required
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = models.Question.objects.filter(tags=tag).order_by('-created_at')
    common_tags =  models.Question.tags.most_common()[:5]
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'questions': questions,
    }
    return render(request, 'qna/questions.html', context)


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


@login_required
def question_detail(request, pk):

    question = get_object_or_404(models.Question, id=pk)
    context = {
        'question': question,
    }
    return render(request, "qna/question-detail.html", context)