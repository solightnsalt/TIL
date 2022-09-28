from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    name = request.GET.get("ball")
    context = {
        "name": name,
    }
    return render(request, "pong.html", context)
    # 사이에꺼 없이 렌더 뒤에 그냥 바로 {'name' : request.GET.get('ball')} 이렇게 써줘도 됨
