from django.shortcuts import render

from .models import Post

def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # return render(request,'blog/post_list.html')
    # posts변수에 ORM을 이용해서 전체 post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.all().order_by('-created_date')
    print(posts)

    context = {
        'title': 'PostList from post_list view',
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context=context)

def post_detail(request,pk):
    posts = Post.objects.get(pk=pk)

    context = {
        'post' : posts

    }

    return render(request,'blog/post_detail.html',context)