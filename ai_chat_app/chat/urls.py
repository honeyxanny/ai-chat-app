from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_new_chat),
    path('<str:chat_uuid>/', views.chat),
    path('', views.start_page),
]
