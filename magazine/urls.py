from django.urls import path
from .views import MagazineUpdateView

urlpatterns = [
    path("<pk>/update", MagazineUpdateView.as_view()),
]
