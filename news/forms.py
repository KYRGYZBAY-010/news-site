from .models import Articles
from django.forms import ModelForm, TextInput, DateInput , Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']


        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Текст статьи'
            }),
            "date": DateInput(attrs={
                'class':'form-control',
                'placeholder': 'Дата публикации'
            })
        }