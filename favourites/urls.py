from django.urls import path
from favourites import views

urlpatterns = [
    path('favourite/', views.FavouriteList.as_view()),
    path('favourite/<int:pk>/', views.FavouriteDetail.as_view()),
]
