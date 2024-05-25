# book_orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_order, name='book_order'),
    path('load-books/', views.load_books, name='load_books'),
    path('success/', views.success, name='success'),  # Ensure you have a success view
]
