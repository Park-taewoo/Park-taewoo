from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content','image',)

class CommentForm(forms.ModelForm):
    content= forms.CharField(widget=forms.Textarea)#글씨크기
    class Meta:
        model = Comment
        fields =('content',)