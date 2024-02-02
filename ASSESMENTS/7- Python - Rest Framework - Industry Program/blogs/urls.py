from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListAPI, name='BlogListAPI'),
    path('BlogDetailAPI/<int:blog_id>', BlogDetailAPI, name='BlogDetailAPI'),
]
