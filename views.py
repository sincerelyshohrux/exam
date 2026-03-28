from django.shortcuts import render

# Create your views here.
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']

        Book.objects.create(
            title=title,
            author=author, 
            price=price
            )
        return render(request, 'books/book_create.html')
