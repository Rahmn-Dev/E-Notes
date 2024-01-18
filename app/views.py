from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Workspace
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
import requests
from django.utils import timezone
from .forms import NoteForm, WorkspaceForm


def index(request):
    workspaces = Workspace.objects.all()
    noteid = Note.objects.all()
    notes = Note.objects.filter(trashed=False, ).order_by('-updated_at')
    return render(request, 'base.html', {'workspace': workspaces, 'noteid': noteid, 'listnotes': notes} )

@login_required
def note_list(request, pk):
    workspaces = Workspace.objects.all()
    notes = Note.objects.filter(trashed=False, workspace=pk ).order_by('-updated_at')
    getname = [list.workspace.name for list in notes]
    getid = [list.workspace.id for list in notes]
    noteworkspace = getname[0]
    noteworkspaceid = getid[0]
    # print(noteworkspace)
    # if notes:
    #     data = [{'title': note.title, 'content': note.content} for note in notes]
    #     JsonResponse({'data': data})
    
    return render(request, 'base.html', {'listnotes': notes,'workspace': workspaces, 'noteworkspace': noteworkspace, 'noteworkspaceid': noteworkspaceid})

@login_required
def note_edit(request, pk):
    workspaces = Workspace.objects.all()
    note = get_object_or_404(Note, pk=pk)
    notes = Note.objects.filter(trashed=False, ).order_by('-updated_at')
    lastupdate = Note.objects.filter(trashed=False, id = pk)
    lastupdatefirst = [last.updated_at.strftime("%b. %d, %Y, %I:%M %p") for last in lastupdate]
    resultlastupdated = lastupdatefirst[0]
    getid = [list.workspace.name for list in notes]
    noteworkspace = getid[0]
    print(noteworkspace)
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

    return render(request, 'note/note_edit.html', {'form': form, 'note': note, 'listnotes': notes, 'noteworkspace': noteworkspace, 'lastupdate': resultlastupdated, 'workspace': workspaces,})
@login_required
def note_trash(request, pk):
    note = get_object_or_404(Note, pk=pk)
    notes = Note.objects.filter(trashed=True, ).order_by('-updated_at')
    lastupdate = Note.objects.filter(trashed=True, id = pk)
    lastupdatefirst = [last.updated_at.strftime("%b. %d, %Y, %I:%M %p") for last in lastupdate]
    resultlastupdated = lastupdatefirst[0]
    getid = [list.workspace.name for list in notes]
    noteworkspace = getid[0]
    print(noteworkspace)
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

    return render(request, 'base.html', {'form': form, 'note': note, 'listnotes': notes, 'noteworkspace': noteworkspace, 'lastupdate': resultlastupdated})
@login_required
def note_trashlist(request):
    notes = Note.objects.filter(trashed=True, ).order_by('-updated_at')
    workspaces = Workspace.objects.all()
    return render(request, 'base.html', { 'listnotes': notes,  'workspace': workspaces,})

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

def note_create(request, pk):
    workspaces = Workspace.objects.all()
    notes = Note.objects.filter(trashed=False, workspace=pk ).order_by('-updated_at')
    form = NoteForm()
    getname = [list.workspace.name for list in notes]
    getid = [list.workspace.id for list in notes]
    noteworkspace = getname[0]
    noteworkspaceid = getid[0]
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.instance.workspace_id = pk
        form.instance.author = request.user
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
    return render(request, 'base.html', {'form': form, 'workspace': workspaces, 'listnotes': notes,  'noteworkspace': noteworkspace, 'noteworkspaceid': noteworkspaceid})