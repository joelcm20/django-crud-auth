from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important", "completed"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write a title", "autofocus": ""}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write a description"}),
            "important": forms.CheckboxInput(attrs={"class": "my-2 form-check-input"}),
            "completed": forms.CheckboxInput(attrs={"class": "my-2 form-check-input"})
        }
