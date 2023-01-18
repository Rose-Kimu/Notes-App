from django.shortcuts import render
from .models import *

def home(request):
    entries = Entry.objects.all()
    context ={'entries':entries}
    return render(request, 'myapp/home.html', context)
