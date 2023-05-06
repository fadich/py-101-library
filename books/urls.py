from django.urls import path
from django.views.generic import TemplateView
from .views import home, BookListView, BookView, user_login, user_logout, user_registration

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:pk>/', BookView.as_view()),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('registration/', user_registration, name='user_registration'),
]