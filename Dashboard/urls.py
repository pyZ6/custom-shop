
from django.urls import path
from Dashboard import views
from .forms import DashForm

urlpatterns = [
    path('', views.validation_form, name="validationform"),
]

