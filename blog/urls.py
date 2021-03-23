from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<slug:post>/', views.post_single, name='post_single'),
]