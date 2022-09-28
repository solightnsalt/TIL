from django.urls import path
from . import views

# 현재 폴더 '.' 안의 views에서 불러와서 쓸래~ 라는 뜻

urlpatterns = [
    # app : practices
    # 프로젝트 폴더 안에 있었을때는 경로 필요했지만 이젠 필요 없음
    # path("index/", practices.views.index),
    path("index/", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
]
