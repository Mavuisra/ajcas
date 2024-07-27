from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
class CreationUserForm(BootstrapMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class MemberForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user','date_created','name']

  
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'commenter...',
                'rows': 3,
            }),
        }