from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import PostCreateForm
from .models import Post

User = get_user_model()

def post_list(request):

    posts = Post.objects.all().order_by('-created_date')
    print(posts)

    context = {
        'title': 'PostList from post_list view',
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context=context)

def post_detail(request,pk):
    try:
        posts = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Question does not exist!!!")

    context = {
        'post' : posts

    }

    return render(request,'blog/post_detail.html',context)

def post_create(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form' : form,
        }
        return render(request,'blog/post_create.html',context)
    elif request.method =='POST':
        form = PostCreateForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            user = User.objects.first()
            post = Post.objects.create(
                title = title,
                text = text,
                author = user,
            )
            return redirect('post_list')
            # return redirect('post_detail',pk=post.pk)
        else:
            context = {
                'form' : form,
            }
            return render(request,'blog/post_create.html',context)

def post_modify(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # POST요청(request)가 올 경우 전달받은 데이터의 title,Text값을 사용해서
        # 해당하는 Post인스턴스 (post)의 title, text속성값에 덮어씌우고
        # DB에 업데이트하는 save()메서드 실행
        data = request.POST
        title = data['title']
        text = data['text']
        post.title = title
        post.text = text
        post.save()
        # 기존 post인스턴스를 업데이트 한 후 다시 글 상세화면으로 이동
        return redirect('post_detail', pk=post.pk)
    elif request.method == 'GET':
        # pk에 해당하는 Post인스턴스를 전달
        context = {
            'post': post,

        }
        return render(request, 'blog/post_modify.html', context)

def post_delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')
