from django import forms

class PasswordGeneratorForm(forms.Form):

    password = forms.CharField()

    OPTIONS = (('lc_letters', 'a-z'), ('uc_letters', 'A-Z'),
            ('numbers', '0-9'), ('symbols', '@%^!...'))

    characters = forms.MultipleChoiceField(
            choices=OPTIONS,
            widget=forms.CheckboxSelectMultiple,
            initial='lc_letters',
            )

    length = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'id': '',
            'type': 'number',
            'value': '12',
        }
    ))

