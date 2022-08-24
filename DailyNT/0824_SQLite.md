# 파이썬 용어정리

## 객체

+ 객체(object)는 **사전적인 정의로 실제 존재하는 것을 말한다**. 객체지향 이론에서는 사물과 같은 유형적인 것뿐만 아니라, 개념이나 논리와 같은 무형적인 것들도 객체로 간주한다. 프로그래밍에서의 객체는 클래스에 정의된 내용대로 메모리에 생성된 것을 뜻한다.

>Any data **with** **state** (attributes **or** **value**) **and** defined **behavior** (methods). Also the ultimate **base** **class** of any **new**-style **class**.

+ 객체는 어떠한 속성값과 행동을 가지고 있는 데이터입니다.

+ 파이썬의 모든것들(숫자, 문자, 함수 등)은 여러 속성과 행동을 가지고 있는 데이터입니다.

+ 실제 세상에서도 object는 그 본연의 추상적인 개념만 가지고 있는것이 아니라, 다양한 정보와 행동을 가지고 있습니다.

+ 이러한 객체들이 가진 속성중에 상태들은 value, 또는 attribute라고 부릅니다. 또 객체가 가진 행동들은 method라고 부릅니다.

### 클래스 

+ 클래스 : 틀 

  1. 붕어빵틀
  2. 사람

### 인스턴스 

+ 틀 안의 각각의 **사례** 

  1. 붕어빵1, 2, 3

  2. 아이유, 유재석, 홍길동 

### 속성 

+ 값

### 메서드

+ 함수



# ORM

+ Object - relational - mapping 
  + 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
  + 관계형 데이터베이스 rdbms
+ 파이썬에서는 sqlaichemy, peewee, 등 라이브러리 있고, 장고 프레임워크에서는 내장 django orm을 활용
+ 데이터베이스 게시판의 게시글, 사용자 정보, 노래 정보 

+ 객체로 디비를 조작한다 





## 모델 설계

+ `Genre.objects.all()`  : 객체.머시기 는 뭐다 ? 클래스다 

  => `Select * From Genre;`

```SQL
CREATE TABLE GENRE (
ID PRIMARY KEY,
NAME VARCHAR)
```

```PYTHON
class Genre(models.Model):
  name = models.CharField(max_length=30)
```

+ CharField = TextField 조건 설정 
  + 뒤에 길이는 Varchar(30) 뜻하는 것 



### 환경설정

+ 노션보고 하기 



### 모델 설계 및 반영

+ 오알엠 ? 
  + 파이썬 코드로 데이터 베이스를 조작한다 

1. 클래스를 생성하여 내가 원하는 디비의 구조를 만든다. 
   1. 클래스에 이름을 붙이고 
   2. 다양한 기능을 활용하기 위한 상속을 받고 
   3. 내가 어떤 필드를 할건지 지정한다 

```sql 
from django.db import models

# gerne 클래스를 만드는데,
# models.Model 내부 클래스를 상송 받는다. 
# 왜 상속 받을까 ? (미리 만들어진) 기능들을 활용하고 싶어서 

class Genre(models.Model):
	name = models.CharField(max_length=30)
# 여기까지 만들고 그 이후의 이걸 어떻게 만들어주세요 하는건 터미널에서 한다. 
# 실행명령 공식처럼 외우기 
python manage.py makemigrations #이거 치면 바로 파이썬 파일 만들어줌 
# 디비에서 가장 중요한 프라이머리 키랑, 아이디도 만들어준다. 

# db에 반영
python manage.py migrate #터미널에 실행하면 db에 테이블이 생긴다. 

# sqlite3 db.sqlite3 하면 다 테이블 생겨있음. .tables / .schema db_gerne 명령어로 확인해보기 

shell plus model import
shell plus django import 

#iu = person()
#iu.name = '아이유'
#터미널에
genre = Genre()
genre = 인디밴스'

grenr.save() 하면 저장됨 
그리고 genre 호출하면 아까 저장한거 나옴 
```

2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 (자동)생성한다.

```python
python manage.py mig
```

3. db에 migrate 한다. 

```python
python 
```



#### migration

+ model에 생긴 변화를 디비에 반영하기 위한 방법 
+ 마이그레이션 파일을 만들어서 디비 스키마를 반영한다 
+ 명령어 
  + makemigrations : 마이그레이션 파일 생성
  + Migrate : 마이그레이션을 디비에 반영



##### 정리

1. 클래스 생성 > 테이블 생성
2. 필드 변경 (수정, 삭제, 추가)
3. 클래스 수정 



##### migrate 살펴보기 

```python
BEGIN;



COMMIT;
```

##### 참고 ) DB - Transjection 

+ Ex. 내 쿼리 1000줄, 근데 892줄에 오류 발생 
  + 어 어카지 ? 
  + 쿼리 반영되기 전으로 롤백을 시킨다
+ ex. 클래스 10개 마이그래이션 5개에서 오류 
  + 오류 메시지와 함께 반영하지 x 





## orm기본 조작 

### create

```python
# 직접 명령어를 실행하기 위해서 터미널에서 아래 명령어로 접속
python manage.py shell_plus

# 방법 1
Genre.objects.create(name='트로트')

# 방법 2
genre = Genre() #장르라고 하는 인스턴스를 만들고 
genre.name = '락'
genre.save()

# 위에 실행한거 조회
Genre.objects.all() # = query set 쿼리 결과의 묶음. 일종의 리스트 

tpye(Genre.objects.all())
>> django.db.models.query.QuerySet

# index 로 조회
Genre.objects.all()[0]
>> <Genre: Genre object (1)> # (1) = id값

Genre.objects.all()[0].name
>> '인디밴드'

# 반복문도 가능 
for genre in genres:
  print(genre.name)
>> 인디밴드
>> 트로트
>> 락 

# 아이디가 1인 애만 가져오고 싶다 
Genre.objects.get(id=1) # = SELECT id FROM Genres WHERE id = 1;
>> <Genre: Genre object (1)> 
>>: 반드시 하나. 없거나 많으면 오류, PK:primary key를 바탕으로 찾을때

# 위에꺼랑 이거랑 뭔 차이 ? 
Genre.objects.filter(id=1)
>> <QuerySet [<Genre: Genre object (1)>]>
>>: 결과가 무조건 QuerySet(일종의 리스트), 나머지 모든 where는 필터
```



### 수정

```python
# 먼저 오브젝트를 가지고 온다 
genre = Genre.objects.get(id=1)
genre.name
>> '인디밴드' : 이 문자열이 장르라고 하는 객체의 인스턴스 중 하나

genre.name = '인디음악'

#위에까지 한다고 반영되지 않는다. 무조건 세이브해야 반영됨 
genre.save()
```

### 삭제

```python
# 삭제도 먼저 오브젝트 가지고 와서 
genre = Genre.objects.get(id=2)
genre.delete() # 삭제
# delete는 save 안해도 바로 반영된다 주의하기
```

> 메서드를 chaining 하는 것도 가능하다 
>
> Ex. 'a bc'.strip().upper()
>
> Ex. Genre.objects.get(id=2).delete()





#### 해보기 

> 필드 참고 
>
> [장고 필드](https://www.docs.djangoproject.com/en/4.1/ref/models/fields/#datefield)

```python
# 파이썬 파일을 먼저 만들어 
class Artist(models.Model):
  name = models.CharField(max_length=30)
  debut = models.DateField()
  
# 그 다음 터미널에 
python manage.py makemigrations

python manage.py migrate

# 까지 하면 SQL EXPLORER에서 데이터테이블 만들어진거 확인 할 수 있다. 
```

```python
artist.objects.create(name = '아이브', debut = 2008) 
# 이거 아닌가보다 ㅠㅠ
# 1. 아티스트 생성 
artist = Artist()
artist.name = 'ive'
artist.debut = datetime.date(2021, 12, 1)
artist.save()

ive = Artist.objects.get(id = 1)
ive.debut
>> datetime.date(2021, 12, 1) # 오호. 객체 개념 
```

```sql
artist = Artist()
artist = '아이유'
artist.debut = '2019-12-26'
artist.save()

iu = Artist.objects.get(id = 2)
iu.debut
>>datetime.date(2019, 12, 26)
```

+ 위에 왜 다르게 넣었는데도 똑같이 datetime.date 로 나오냐 ? 
  + 입력한거랑 출력하는거랑 다르다 
  + 왜 ? 파이썬이 알아서 바꿔준다. ㅇ ㅓ? 이거 형식 날짜같네 ? 날짜로 바꿔야지~ 이런 느낌 

