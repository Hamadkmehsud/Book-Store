from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,  name= 'home_page'),
    path('books/', views.books, name = 'all_books'),
    path('books/<slug:slug>/', views.book_details, name='book_details' )

]