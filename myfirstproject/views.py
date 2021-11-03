# git remote add origin https://github.com/vitlilg/myfirstproject-root-1.git
# git branch -M main
# git push -u origin main

from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hello!'})