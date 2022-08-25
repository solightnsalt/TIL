from this import d
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()
    
class Genre(models.Model):
    title = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()
 

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]    


# movie = ["봉준호", "드라마", "괴물", "2006-07-27", 119, False]
# director = Director.objects.get(name=movie[0])
# director.name

# for movie_ in movies:
#     movie = Movie()
#     movie.director = Director.objects.get(name=movie_[0])
#     movie.genre = Genre.objects.get(title=movie_[1])
#     movie.title = movie_[2]
#     movie.opening_date = movie_[3]
#     movie.running_time = movie_[4]
#     movie.screening = movie_[5]
#     movie.save()

# Ms = Movie.objects.all()
# for m in Ms:
#     print(m.director, m.genre, m.title, m.opening_date, m.running_time, m.screening)

# Ms = Movie.objects.all()
# for m in Ms:
#     print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

# movie = Movie.objects.order_by('opening_date')[0]
# print(
#     movie.director.name, 
#     movie.genre.title,
#     movie.title,
#     movie.opening_date, 
#     movie.running_time,
#     movie.screening
#     )

# movies = Movie.objects.filter(screening = True).order_by('opening_date')
# for movie in movies:
#     print(
#     movie.director.name, 
#     movie.genre.title,
#     movie.title,
#     movie.opening_date, 
#     movie.running_time,
#     movie.screening
#     )

# bong = Director.objects.get(name='봉준호')
# movies = Movie.objects.filter(director=bong).order_by('opening_date')
# for movie in movies:
#     print(
#     movie.director.name, 
#     movie.genre.title,
#     movie.title,
#     movie.opening_date, 
#     movie.running_time,
#     movie.screening
#     )
    
# movies = Movie.objects.order_by('-opening_date')
# for movie in movies:
#     print(
#     movie.director.name, 
#     movie.genre.title,
#     movie.title,
#     movie.opening_date, 
#     movie.running_time,
#     movie.screening
#     )

# bong = Director.objects.get(name='봉준호')
# movie = Movie.objects.filter(director=bong).order_by('opening_date')[0:1]
# print(
#     movie.director.name, 
#     movie.genre.title,
#     movie.title,
#     movie.opening_date, 
#     movie.running_time,
#     movie.screening
#     )

# movies = Movie.objects.filter(running_time__gte=119).order_by('running_time')
# for movie in movies:
#     print(
#         movie.director.name,
#         movie.genre.title,
#         movie.title,
#         movie.opening_date,
#         movie.running_time,
#         movie.screening
#         )

# movies = Movie.objects.filter(opening_date__startswith='2022').order_by('opening_date')
# for movie in movies:
#     print(
#         movie.director.name,
#         movie.genre.title,
#         movie.title,
#         movie.opening_date,
#         movie.running_time,
#         movie.screening
#         )

# bong = Director.objects.get(name='봉준호')
# drm = Genre.objects.get(title='드라마')
# movies = Movie.objects.filter(director=bong, genre=drm).order_by('opening_date')
# for movie in movies:
#     print(
#         movie.director.name,
#         movie.genre.title,
#         movie.title,
#         movie.opening_date,
#         movie.running_time,
#         movie.screening
#         )

# bong = Director.objects.get(name='봉준호')
# movies = Movie.objects.exclude(director=bong).order_by('opening_date')
# for movie in movies:
#     print(
#         movie.director.name,
#         movie.genre.title,
#         movie.title,
#         movie.opening_date,
#         movie.running_time,
#         movie.screening
#         )