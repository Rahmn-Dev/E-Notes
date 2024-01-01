from django.shortcuts import render, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests
# from .forms import NoteForm


@login_required
def note_list(request):
    
    notes = Note.objects.filter(trashed=False)

    return render(request, 'index.html', {'listnotes': notes})