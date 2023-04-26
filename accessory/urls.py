from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_accessory, name='viewaccessory'),
    path('<int:accessory_id>/', views.view_special_accessory, name='specialaccessory'),
]
