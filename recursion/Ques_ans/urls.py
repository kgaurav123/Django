from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('question', views.question, name='question'),
    path('questionslist',views.questionslist,name='questionslist'),
]
