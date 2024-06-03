from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Form-list/<int:pk>/', views.forum_cat, name='forum-category'),
    path('Form-detail/<int:pk>/', views.forum_detail, name='forum-detail'),
]