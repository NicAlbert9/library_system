from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # /books/
    path('add/', views.book_create, name='book_create'),
    path('<int:id>/edit/', views.book_update, name='book_update'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
]

