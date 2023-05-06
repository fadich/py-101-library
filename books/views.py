from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/books/')
        else:
            return render(request, 'user_login.html', context={
                'error': 'invalid credentials'
            })
    else:
        return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/books/')


def user_registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return HttpResponseRedirect('/books/')
    return render(request, 'registration.html', context={
        "form": form
    })


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


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
