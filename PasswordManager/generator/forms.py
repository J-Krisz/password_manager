from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.bootstrap import InlineRadios

class PasswordGeneratorForm(forms.Form):

    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'value': '{{ password }}'
            }
        ),)

    OPTIONS = (('lc_letters', 'a-z'), ('uc_letters', 'A-Z'),
            ('numbers', '0-9'), ('symbols', '@%^!...'))
    
    # TODO flattecn checkboxes
    characters = forms.MultipleChoiceField(
            choices=OPTIONS,
            widget=forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-check form-check-inline'
                }),
            initial='lc_letters',
            )

    length = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type': 'number',
            'value': '12',
        }
    ))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'

    #     self.helper.layout = Layout(
    #         InlineRadios('characters'),

    #     )
