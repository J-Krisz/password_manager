import string
import secrets

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PasswordGeneratorForm


class GeneratorFormView(LoginRequiredMixin, FormView):
    template_name = 'generator/generator.html'

    form_class = PasswordGeneratorForm
    

def password_generator(request):

    lc_letters = string.ascii_lowercase
    uc_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    length = int(request.GET.get('length', '12'))

    use_chars = lc_letters

    if request.GET.get('uc_letters'):
        use_chars += uc_letters

    if request.GET.get('numbers'):
        use_chars += numbers

    if request.GET.get('symbols'):
        use_chars += symbols

    password = ''.join(secrets.choice(use_chars) for _ in range(length))

    return 

