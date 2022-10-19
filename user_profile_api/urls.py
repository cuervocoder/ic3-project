from django.urls import path
from user_profile_api import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('user-profile/', views.UserProfileApiView.as_view()),
    path('user-profile/<int:pk>', views.UserProfileApiViewDetail.as_view()),
]