from django.shortcuts import render
from .models import Poll, Choice


def new_poll(request):
    return render(request, 'poll/new_poll.html', {})


def create_poll(request):
    if request.method == 'POST':
        question = request.POST.get('question', None)
        choices = [request.POST[k] for k in request.POST
                   if k.startswith('choice')]
        raise NotImplementedError()
