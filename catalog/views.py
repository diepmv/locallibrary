from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import HttpResponse
# Create your views here.

def index(request):
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.count()

  return render(request, 'index.html', context={'num_books':num_books,
                                                'num_instances':num_instances,
                                                'num_instances_available':num_instances_available,
                                                'num_authors':num_authors},)

class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

    def get(self, request, *args, **kwargs):
      a = request.session.get('myname')
      print(a)
      return HttpResponse("asdadw")