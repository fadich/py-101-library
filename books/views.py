from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView, DetailView


def home(request):
    books = Book.objects.all()
    return render(request,'home.html',{'books':books})

class BookListView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()

        return context

class BookView(DetailView):
    template_name = 'book_details.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = self.object.authors.all()

        return context
