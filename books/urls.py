from django.urls import path
from django.views.generic import TemplateView
from .views import home, BookListView, BookView

urlpatterns = [

    path('',BookListView.as_view()),
    path('<int:pk>/',BookView.as_view())
]