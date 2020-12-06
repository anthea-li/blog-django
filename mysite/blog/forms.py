from django.forms import ModelForm, TextInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'author', 'content']
        widgets = {
            'title': TextInput(),
            'subtitle': TextInput(),
            'author': TextInput(),
        }