from django import forms
# from .models import Question
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# class QForm(form.ModelForm):
#     class Meta:
#         model = Question
#
