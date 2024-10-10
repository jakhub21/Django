from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min, Sum
# Create your views here.

def index(request):
    books = Book.objects.all().order_by('title')
    num_books = books.count()
    avg_books = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_num_books': num_books,
        'average_rating': avg_books,
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_bestseller': book.is_bestseller,
    })