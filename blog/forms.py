from django import forms
from django.forms import ModelForm, TextInput

from blog.models import Post, Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputClass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputClass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
    }
