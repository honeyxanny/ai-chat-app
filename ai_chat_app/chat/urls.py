from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:chat_uuid>/', views.chat),
    path('start/', views.start_new_chat),
]
