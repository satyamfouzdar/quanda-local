from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm
from . import models


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('homepage')

    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {'form': form})

def profile(request):
    user = request.user
    profile = get_object_or_404(models.Profile, user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)
