from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListMovie.as_view()),
    path('<int:pk>/', views.GetMovie.as_view()),
]
