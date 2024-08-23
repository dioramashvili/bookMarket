from django.shortcuts import render, get_object_or_404

from market.models import Book


# Create your views here.
def market(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context)