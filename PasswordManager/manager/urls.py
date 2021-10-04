from manager.models import Account
from django.urls import path
from .views import LandingPageView, SignUpView, UserLoginView, AccountListView, EditAccountView, AccountDeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),

    path('SignUp/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('accounts/', AccountListView.as_view(), name='accounts'),
    path('edit/<str:pk>/', EditAccountView.as_view(), name='edit'), 
    path('delete/<str:pk>', AccountDeleteView.as_view(), name='delete'),
]
