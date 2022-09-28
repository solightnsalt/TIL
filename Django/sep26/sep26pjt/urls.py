"""sep26pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import practices.views
# from articles import views as articles_views
import practice2.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # # app : practices 앱 폴더 안으로 옮김
    # path("index/", practices.views.index),
    # path("ping/", practices.views.ping),
    # path("pong/", practices.views.pong),
    # app : practice2
    path("", practice2.views.index),
    path("number/<int:_number>/", practice2.views.print_number),
    path("print-text/", practice2.views.print_text),
    # app : articles 앱 폴더 안으로 옮김
    # path("", articles_views.index),
    # sub 문지기
    path("articles/", include("articles.urls")),
    path("practices/", include("practices.urls")),
]
