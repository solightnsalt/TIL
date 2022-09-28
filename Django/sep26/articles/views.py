from django.shortcuts import render
from sep26pjt.settings import BASE_DIR
from .models import Article

# 현재폴더 모델스 파일에 아티클을 가져와서 쓴다
# DB에서 가져오기 때문에 리스트도 필요 없음.
# guestbook = []

# Create your views here.
def index(request):
    # DB에서 가져오기
    guestbook = Article.objects.all()
    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # guestbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)
    return render(request, "articles/create.html", {"content": content})
