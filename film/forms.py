from .models import Comment,SeriesComment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body','stars']


class SeriesCommentForm(forms.ModelForm):
    class Meta:
        model = SeriesComment
        fields = ['body','stars']