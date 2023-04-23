from django.db import models
from ..models.user import User
from django import forms


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'active', 'admin', 'staff']