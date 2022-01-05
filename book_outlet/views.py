from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book


def index(request):

    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    # this method creates a dictionary with aggregated data
    avg_rating = books.aggregate(Avg("rating"), Min("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        'total_number_of_books': num_books,
        'average_rating':avg_rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        'is_selling': book.is_selling,
    })
