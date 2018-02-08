from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
# Create your views here.



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


def __add__(self, other):
      if isinstance(other, timedelta):
          # for CPython compatibility, we cannot use
          # our __class__ here, but need a real timedelta
          return timedelta(self._days + other._days,
                           self._seconds + other._seconds,
                           self._microseconds + other._microseconds)
      return NotImplemented


def __add__(self, other):
    "Add a date to a timedelta."
    if isinstance(other, timedelta):
        o = self.toordinal() + other.days
        if 0 < o <= _MAXORDINAL:
            return date.fromordinal(o)
        raise OverflowError("result out of range")
    return NotImplemented

def __add__(self, other):
  "Add a datetime and a timedelta."

  if not isinstance(other, timedelta):
    return NotImplemented
  delta = timedelta(self.toordinal(),
                    hours=self._hour,
                    minutes=self._minute,
                    seconds=self._second,
                    microseconds=self._microsecond)
  delta += other
  hour, rem = divmod(delta.seconds, 3600)
  minute, second = divmod(rem, 60)
  if 0 < delta.days <= _MAXORDINAL:
    return datetime.combine(date.fromordinal(delta.days),
                            time(hour, minute, second,
                                 delta.microseconds,
                                 tzinfo=self._tzinfo))
  raise OverflowError("result out of range")
