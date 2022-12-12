from django.shortcuts import render

from core.models import Book
from core.forms import BookForm

def index(request):
    context = {'form': BookForm()}
    return render(request, 'index.html', context)