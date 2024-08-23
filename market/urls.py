from django.urls import path
from market import views

urlpatterns = [
    path('<int:pk>/', views.market, name='book_detail'),
]