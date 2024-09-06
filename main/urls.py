from django.urls import path
from .views import *

urlpatterns = [
    path('post/',PostList.as_view(),name='post-list'),
    path('post/<int:pk>',PostDetail.as_view(),name='post-detail'),
    path('category/',CategoryList.as_view(),name='category-list'),
]