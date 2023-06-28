from django.urls import path
from comments import views

# CREDIT: Adapted from the Code Institute DRF Tutorial Project
# URL:    https://github.com/Code-Institute-Solutions/drf-api

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view())
]