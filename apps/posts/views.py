from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
def posts_page(request):
    posts = Post.objects.all()[:6]
    return render(request, 'posts/posts.html', {'posts': posts})


def posts_text(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)
    return render(request, 'posts/posts_text.html', {'post': post})
