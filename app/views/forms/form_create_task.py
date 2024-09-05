from django import forms

class TasksCreateForm(forms.Form):
    code = forms.CharField(max_length=20, strip=True, initial='', label='Код заявки')
    description = forms.CharField(strip=True, widget=forms.Textarea, initial='', label='Описание заявки')
    selected_periodic = forms.BooleanField(initial=False, label='Использовать предполагаемое время выполнения?')
    approximate_date = forms.DateTimeField(label='Предполагаемое время выполнения')
    is_periodic = forms.BooleanField(initial=False, label='Периодическая заявка?')