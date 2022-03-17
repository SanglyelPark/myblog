from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']
        labels = {
            'tetle': '제목',
            'content': '내용',
            'photo': '사진',
            'category': '카테고리',
        }