from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('works/', views.listing, name='work_list'),
    path('works/<int:pk>', views.work_detail, name='work_detail'),
]
