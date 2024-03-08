from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks, Labels


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def clean_password2(self):
        # Проверка соответствия паролей
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return password2

class TaskCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['labels'].empty_label = 'Метки не выбраны'
    
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'state', 'labels']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'labels': 'Метки',  # Если вы хотите изменить подпись, можно использовать этот параметр
        }

    # Поле labels делаем необязательным
    labels = forms.ModelMultipleChoiceField(
        queryset=Labels.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )