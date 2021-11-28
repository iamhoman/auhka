from django import forms
from .models import Post, Post_isLike, Post_comment

class post_create_form (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'status',
                  'pic01', 'pic02', 'pic03', 'pic04')

class post_like_form (forms.ModelForm):
    class Meta:
        model = Post_isLike
        fields = ()

class post_comment_form (forms.ModelForm):
    class Meta:
        model = Post_comment
        fields = ('comment',)
