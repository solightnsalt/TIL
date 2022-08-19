어떤 언어를 개발 환경에서 실행 시키고 싶다 ? 

이런 모든 것들이 시스템에서 설정되는 곳 ? 

시스템 환경 변수 .. 

맥은 터미널에서 zchrc bashrc 이런것들이 환경변수 관리 하는 것 

그냥 `sqlite3` 하면 

Connected to a transient in-memory database.

그냥 임시로 하나 연 거 

`sqlite3 filename.sqlite3`

저 파일명의 데이터베이스를 연 거

예쁘게 보고싶어요 ! 

.mode column

---

# update

C insert insert into 테이블이름 (컬럼1, 컬럼2, ''') values (값1, 값2);

R select select * from table name where 조건

U update 

D delete



## WHERE

+ Table users

### .csv 파일을 적용하기 

1. 우선 `CREATE TABLE 테이블명(column)` 로 테이블을 만든다 

2. 데이터 추가 `.mode csv`

3. 같은 디렉토리에 있는 users.csv 파일을 테이블로 

   `.import users.csv users`



#### 활용

+ `SELECT * FROM users WHERE age >= 30;`

+ `SELECT first_name FROM users WHERE age >= 30 LIMIT 3`
+ `SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김'



### WHERE 절에서 사용할 수 있는 연산자

+ 비교 연산자 

  + =,  >, >=, <, <=

+ 논리 연산자 

  + AND
  + OR
  + NOT 뒤에 오는 조건의 결과를 반대로 

+ ***주의 !*** 우선순위 잘 생각하기 

  ```sql
  WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
  -- 1. 키가 175 이거나, 키가 183 이면서 몸무게가 80인 사람
  WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
  -- 2. 키가 175 또는 183 인 사람 중에서 몸무게가 80인 사람
  ```



### SQL 사용할 수 있는 연산자

+ BETWEEN VALUE1 AND VALUE2

+ IN (VALUE1, VALUE2 .... )

  + 목록 중 값이 하나라도 일치하면 성공

+ LIKE

  + 비교문자열과 형태 일치
  + 와일드카드 (% : 0개 이상 문자, _ : 1개 단일 문자)

+ IS NULL / IS NOT NULL 

  + `=`이거 안됨. NULL 여부를 확인할 때는 항상 IS 사용

    

+ 부정연산자 
  + 같지 않다 !=, ^=, <>
  + ~와 같지 않다 NOT 칼럼명 =
  + ~보다 크지 않다 NOT 칼럼명 >

### 연산자 우선순위

1. 괄호 ()
2. NOT
3. 비교 연산자. SQL
4. AND
5. OR



## SQLite Aggregate Functions

### 집계함수

+ 값 집합에 대한 계산을 수행하고 단일 값을 반환

  + COUNT

  + AVG 

  + MAX ex. 계좌 잔ㅇㄱ이 제일 높은 사람

    `SELECT MAX(balance), first_name FROM users;`

  + MIN ex. 이씨 중에 젤 어린 사람 나이랑 이름 

    `SELECT MIN(age), first_name FROM users WHERE last_name = '이';`

  + SUM



#### LIKE

```sql
SELECT * FROM users WHERE last_name LIKE '김%'
-- 김으로 시작하는 사람
```

+ 패턴 일치를 기반으로 데이터를 조회하는 방법
+ % 0개 이상의 문자 
+ _ 임의의 단일 문자 

+ Wildcards 사용 예시 
  + 2% : 2로 시작
  + %2 : 2로 끝
  + %2% : 어디든 2가 들어가면 
  + _2% : 두번째 글자가 2 
  + 1___ : 1로 시작하는 4글자 숫자로 치면 1000~ 1999
  + 2\_%_# / 2\_\_% : 2로 시작하고 적어도 3자리 인 값

> 정규표현식 ? 
>
> 문자열 패턴 
>
> ex. 이메일 
>
> 이메일 형식에 맞지 않습니다. 
>
> 전화번호 000 - 0000 - 0000



Q.  지역 번호가 02인 사람 수

`SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';`

땀 흘리는거 까먹지 말기 ~~~! 

Q. 준으로 끝나는 사람

`SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';`

Q. 중간번호가 5114인 사람 

`LIKE '%-5114-%';`



#### ORDER BY

+ sort a result set of a query

+ 조회결과 집합을 정렬 

+ `SELECT`문에 추가하여 사용 

+ 정렬 순서를 위한 2개의 keyword 제공

  + ASC ascending 오름차순 default 
  + DESC desceding 내림차순

  > *`1 11 20 22 3 34837 548` 이거는 뭐다 ? 문자열이라서 이렇게 정렬된다*

Q. 나이순 오름차순 상위 10개? 

`SELECT * FROM users ORDER BY age (ASC) LIMIT 10;`

ASC 는 디폴트라 안써도 된다 

Q. 나이, 성 순 

`SELECT * FROM users ORDER BY age, last_name LIMIT 10;`

Q. 계좌 잔액 순 내림차순 

`SELECT last_name,  first_name, balance FROM users ORDER BY balance DESC LIMIT 10;`

Q. 계좌 잔액 내림차순 성 오름차순 

`SELECT * FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;`



