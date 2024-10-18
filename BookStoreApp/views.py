from django.shortcuts import render , get_object_or_404
from .models import BookStore, Address, Author
from django.db.models import Avg

# Create your views here.

def index(request):
    return render(request, 'BookStoreApp/index.html')

from django.db.models import Avg

def books(request):
    books = BookStore.objects.all().order_by('title')  # Get all books
    total_books = books.count()  # Get the total number of books
    average_rating = books.aggregate(Avg('rating'))  # Calculate the average rating across all books
    # Passing the correct context key 'books_list' 
    return render(request, 'BookStoreApp/books.html', context={
        'books_list': books,
        'total_books': total_books,
        'avg_rating': round(average_rating['rating__avg'],2)  # Get the average rating from the aggregate result
    })



def book_details(request, slug):
    # Using get_object_or_404 to handle cases where the book is not found
    book = get_object_or_404(BookStore, slug=slug)
    address = book.author.address
    
    return render(request, 'BookStoreApp/book_details.html', context={
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling,
        'author_address': address.full_address()
    })


