from django import forms

class PasswordGeneratorForm(forms.Form):

    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'id': '',
            'type': 'number',
            'value': '',

        }
    ))
