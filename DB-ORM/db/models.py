from django.db import models

# models.Model 내부 클래스를 상속 받아 
# 내가 원하는 DB구조의 Director, Genre 클래스 생성
class Directors(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genres(models.Model):
    genre = models.TextField()

# $ python manage.py makemigrations
# Migrations for 'db':
#   db\migrations\0001_initial.py 이 경로에 파이썬 파일 생성하고 
#     - Create model Directors 이 클래스들 만듦   
#     - Create model Genres

# $ python manage.py migrate
# Operations to perform:
#   Apply all migrations: db ->db.sqlite3에 테이블이 생겼다. 
# Running migrations:
#   Applying db.0001_initial... OK

# python manage.py shell_plus ->장고 쉘 진입

# Directors.objects.create(name = '봉준호', debut = '1993-01-01', country = 'KOR')

# genres = Genres()
# genres.genre = '재난'
# genres.save()

