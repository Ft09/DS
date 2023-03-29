
from django.urls import path, include
from . import views 

app_name = 'gall'

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('detail/<int:pk>/', views.FlowerDetailView.as_view(), name='flower-detail'),
]
