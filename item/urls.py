from django.urls import path
from . import views
app_name = 'item'
urlpatterns = [
    path('', views.items, name='items'),
    path('search/',views.search_form, name='search'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]
