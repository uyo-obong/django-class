from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    duration = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'duration'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'content...', 'size': 20}))

    class Meta:
        model = Todo
        fields = ('title',  'duration', 'description')