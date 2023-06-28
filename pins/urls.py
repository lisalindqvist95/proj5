from django.urls import path
from pins import views

# CREDIT: Adapted from the Code Institute DRF Tutorial Project
# URL:    https://github.com/Code-Institute-Solutions/drf-api


urlpatterns = [
    path('pins/', views.PinList.as_view()),
    path('pins/<int:pk>/', views.PinDetail.as_view()),
]