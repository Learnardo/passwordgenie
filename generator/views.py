from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRQRSTXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@#£,!?()%$'))

    if request.GET.get('numbers'):
        characters.extend(list('12345678890'))

    test_password = "oijfdzJDJF7!!53"
    length = int(request.GET.get('length',12))
    generated_password = ""
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'generated_password': generated_password})
