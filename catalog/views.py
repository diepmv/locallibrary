from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):

  model = BookInstance
  template_name = 'catalog/bookinstance_list_borrowed_user.html'
  paginate_by = 10

  def get_queryset(self):
    return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@login_required
def index(request):
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.count()

  return render(request, 'index.html', context={'num_books':num_books,
                                                'num_instances':num_instances,
                                                'num_instances_available':num_instances_available,
                                                'num_authors':num_authors},)

class BookListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Book
    paginate_by = 2

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

    # def dispatch(self, request, *args, **kwargs):
    #   raise PermissionDenied
    #   print(self.http_method_names)
    #   if request.method.lower() == 'get':
    #     try:
    #       handler = getattr(self, 'c')
    #     except AttributeError:
    #       print("Method not allowed")
    #       raise Http404("Poll does not exist")
    #     return handler(request, *args, **kwargs)
    #
    #
    #
    # def get(self, request, *args, **kwargs):
    #
    #   a = request.session.get('myname')
    #   print(request.session.items())
    #   return HttpResponse("asdadw")

