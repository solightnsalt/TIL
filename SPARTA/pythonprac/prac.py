# requests == js fetch처럼 서버에서 데이터를 가져오는 라이브러리
import requests
from bs4 import BeautifulSoup

URL = "https://movie.daum.net/ranking/reservation"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, "html.parser")

movie_list = soup.select('#mainContent > div > div.box_ranking > ol > li')
for movie in movie_list:
    title = movie.select_one('.link_txt').text
    summary = movie.select_one('.link_story').text
    rank = movie.select_one('.rank_num').text
    poster = movie.select_one('.img_thumb')['src']


