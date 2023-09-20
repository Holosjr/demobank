
app_name='wikkiapp'
from django.urls import  path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('user-form/', views.user_form_view, name='user_form'),
]
