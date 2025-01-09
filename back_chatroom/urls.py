from django.urls import path
from back_chatroom import views

urlpatterns = [
    path('chatroom/', views.ChatroomList.as_view()),
    path('chatroom/<int:pk>/', views.ChatroomDetail.as_view()),
]