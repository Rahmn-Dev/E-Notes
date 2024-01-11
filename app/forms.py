from django import forms
from .models import Note, Workspace

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'workspace', 'trashed']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NoteForm, self).__init__(*args, **kwargs)
        # if user:
            # self.fields['workspace'].queryset = Workspace.objects.filter(members=user)

    # id = forms.IntegerField(widget=forms.HiddenInput())

class WorkspaceForm(forms.ModelForm):
    class Meta:
        model = Workspace
        fields = ['name', 'members']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(WorkspaceForm, self).__init__(*args, **kwargs)
        # if user:

        #     self.fields['members'].queryset = user.friends.all()