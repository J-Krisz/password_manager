from django.urls import path
from .views import GeneratorFormView


urlpatterns = [
        path('', GeneratorFormView.as_view(), name='generator'),
    ]
