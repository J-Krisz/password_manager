from django import forms

class PasswordGeneratorForm(forms.Form):


    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'id': '',
            'type': 'number',
            'value': '12',

        }
    ),)

    OPTIONS = (('a-z', 'a-z'), ('A-Z', 'A-Z'), ('0-9', '0-9'), ('@%^!...', '@%^!...'))

    characters = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
            choices=OPTIONS)
