from django.urls import path
from back_posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
]