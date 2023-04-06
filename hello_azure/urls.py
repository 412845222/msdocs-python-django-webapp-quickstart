from django.urls import path
from . import views
from hello_azure import api
urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('chatgpt/',api.chatgpt)
]