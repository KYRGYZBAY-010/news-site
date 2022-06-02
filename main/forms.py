from .models import HomeNews
from django.forms import ModelForm, TextInput, DateInput, Textarea, ImageField


class HomeNewsForm(ModelForm):
    class Meta:
        model = HomeNews
        fields = ['img', 'title', 'description', 'date']


        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи'
            }),
            "description": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Текст статьи'
            }),
            "date": DateInput(attrs={
                'class':'form-control',
                'placeholder': 'Дата публикации'
            })
        }