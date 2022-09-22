"""firstpjt URL Configuration

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
from django.urls import path
from articles import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 어떤 파일의 어떤 함수에서 활용?
    path('welcome/<name>/', views.welcome), # <> 이게 변화하는 변수 =, 뭐가 들어오든 name으로 활용할거야  
]
