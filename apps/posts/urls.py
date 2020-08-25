from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_page, name='posts'),
    path('<int:posts_id>/', views.posts_text, name='post_detail'),
]
