from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('home/', views.home, name='home2'),
    path('words_list/', views.words_list, name='words_list'),
    path('add_word/', views.add_word, name='add_word'),
]
