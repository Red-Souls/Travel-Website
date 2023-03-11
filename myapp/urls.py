from django.urls import path
from . import views
from django.contrib.auth import views as authView

urlpatterns = [
    path('register/', views.register),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
    path('', views.home),
    path('login/', authView.LoginView.as_view(template_name = 'login.html')),
    path('logout/', authView.LogoutView.as_view(next_page = '/')),
    path('gallery/<int:id>/', views.detailGallery),
    path('book/<int:id>/', views.book),
    path('search/', views.search),
    path('booked-tour/', views.bookedTour),
]