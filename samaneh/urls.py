from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('details/<int:pk>', views.work_detail, name='work_detail'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
