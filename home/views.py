from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    context = {}

    return render(request, 'home/index.html', context)
