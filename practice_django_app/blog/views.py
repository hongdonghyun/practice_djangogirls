from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())

    context = {
        'title' :'PostList from Post_list view',
        'post' : posts
    }

    return render(request,'blog/post_list.html',context=context)
