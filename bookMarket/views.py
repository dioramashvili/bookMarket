from django.core.paginator import Paginator
from django.shortcuts import render
from market.models import Book


# def home(request):
#     books = Book.objects.all()
#     paginator = Paginator(books, 3)
#     context = {'books': books}
#     return render(request, 'home.html', context)

def home(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 3)  # Show 3 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})
