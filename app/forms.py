from django import forms


class UserForm(forms.Form):

    name = forms.CharField(label="Имя", initial="Безымянный", help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст", initial=16, help_text="Введите свой возраст")
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
    field_order = ["age", "name", "comment"]