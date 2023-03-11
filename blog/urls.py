from django.urls import path
from .views import*

urlpatterns = [
    path('', Home.as_view()),
    path('<int:id>/', PostDetail.as_view()),
    path('addcomment/<int:id>/', AddComment.as_view()),
]