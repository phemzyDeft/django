from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def counter(request):
    words = request.POST['words']
    amt_of_words = len(words.split())
    return render(request, 'counter.html', {'text': amt_of_words})
