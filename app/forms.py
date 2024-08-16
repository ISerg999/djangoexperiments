from django import forms


class UserForm(forms.Form):

    name = forms.CharField(label="Имя", min_length=2, max_length=20)
    age = forms.IntegerField(label="Возраст", required=False, min_value=1, max_value=100)
    email = forms.EmailField(label="Электронная почта", required=False, min_length=7)
    required_css_class = "field"
    # error_css_class = "error"
    # field_order = ["age", "name", "comment"]