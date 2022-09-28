from django.shortcuts import render
import random
# Create your views here.
# view -> templates 파일 지정 
def index(request):

    return render(request, "index.html")

def today_beer(request):
    beer_list = [
        {"name": "에델바이스", "src":""},
        {"name": "테라", "src":""}
    ]

    beer = random.choice(beer)

    context = {
        "beer" : beer
    }
    return render(request, "today_dinner.html")

def lotto(request):

    return render(request, "lotto.html")