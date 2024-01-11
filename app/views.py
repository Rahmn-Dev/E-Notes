from django.shortcuts import render, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
import requests
from .forms import NoteForm, WorkspaceForm


@login_required
def note_list(request):
    
    notes = Note.objects.filter(trashed=False)

    return render(request, 'index.html', {'listnotes': notes})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()

            # if request.is_ajax():
            #     return JsonResponse({'success': True})
            # else:
            #     return HttpResponseRedirect('/')
    else:
        form = NoteForm(instance=note, user=request.user)

    return render(request, 'note/note_edit.html', {'form': form, 'note': note})

def workspace_create(request):
    if request.method == "POST":
        form = WorkspaceForm(request.POST, user=request.user)
        if form.is_valid():
            workspace = form.save()
            workspace.members.add(request.user)
            return HttpResponseRedirect('/')
    else:
        form = WorkspaceForm(user=request.user)
    return render(request, 'workspace/workspace_create.html', {'form': form})