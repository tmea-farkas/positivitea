from django.urls import path
from back_profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]