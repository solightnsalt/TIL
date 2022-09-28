from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다
    #  디비에서 불러와서 템플릿에 보내준다.
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):

    return render(request, "posts/new.html")


def create(request):
    # parameter로 날아온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")
    # db 에 저장
    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }
    return render(request, "posts/create.html", context)
    # return redirect("")


def delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")
