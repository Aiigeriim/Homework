from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Task, TaskType


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # 'type': forms.ModelChoiceField(queryset=TaskType.objects.all())
            'type': forms.Select(attrs={'class': 'form-control'})
            # 'type': forms.FormChoiceField(queryset=TaskType.objects.all(), attrs={'class': 'form-control'})
            # 'type' : forms.ModelMultipleChoiceField(
            #     queryset=TaskType.objects.all(),
            #     required=False,
            #     widget=forms.CheckboxSelectMultiple(),
            #     label='Типы'
        # )
        }
        error_messages = {'summary': {"required": "Пожалуйста, введите название"}}

    def clean(self):
        summary = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        if summary and description and  summary == description:
            raise ValidationError("Название и описание не могут быть одинаковыми")
        return super(TaskForm, self).clean()
