# Database

+ ? ? ? 

## RDB 

+ Relational Database
+ 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
+ key와 value들의 간단한 관계를 표 형태로 변환한 데이터베이스 

#### schema 스키마

+ 데이터베이스에서 자료의 구조, 자료의 표현 방법, 자료 간의 관계를 형식 언어로 정의한 것 

| name | age  |
| ---- | ---- |
| str  | int  |
| str  | int  |

+ 지식을 표상하는 구조 



#### table

+ 열과 행으로 이루어진 데이터 뭐시기 
+ 행 하나하나의 데이터
+ 열  
+ 키본키primary key : 각 행(레코드)의 고유값 
  + 반드시 설정해야하며, 데이터 베이스 관리 및 관계 설정 시 주요하게 활용됨
  + Ex 대학교 학번,, 주민등록번호 절대로 중복이 발생할 수 없는 고유값

## 관계형 데이터베이스 관리 시스템 RDBMS

![d](https://images.velog.io/images/choijaehyeokk/post/5d76cf78-1f24-44e8-bfef-565eff096a47/rdbms.png)

+ SQLite 로 주로 수업
+ 표준 SQL문은 동일하다 



### data type

---

# SQL

+ Structured query language
+ 관계형 데이터베이스 관리시스템의 데이터관리를 위해 설계된 특수 목적 프로그래밍언어 
+ 데이터 베이스 스키마 생성 및 수정 
+ 자료 검색 및 관리 
+ 데이터베이스 객체 접근 조정 관리 



## 분류 

| 분류 | 개념                                                   |
| ---- | ------------------------------------------------------ |
| ddl  | 관계형 데이터베이스 구조를 정의하기위한 명령어         |
| dml  | 데이터를 저장 조회 수정 삭제 등을 하기 위한 명령어     |
| dcl  | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어 |



## 테이블 생성 및 삭제 

sqlite3 제목.sqlite3 터미널에 치면 시작 

+ 이건 파일 안에서 

```sqlite
-- classmates 라는 이름의 테이블 생성
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회 
.schema classmates

-- 값 추가 
INSERT INTO classmates VALUE (1, '박서함');

-- 테이블 조회
SELENT * FROM classmates;

INSERT INTO classmates 

-- 테이블 삭제 
DROP TABLE classmates

```



###  필드 제약 조건 

```sqlite
CREATE TABLE students(
	id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER DEFAULT ! CHECK (0 < age)
);
```



### CRUD

+ create
+ read
+ update
+ delete



#### insert

+ Insert a single row into a table
+ 테이블에 단일 행 삽입 

```sql
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

SELECT * FROM classmates;
```

```INSERT INTO classmates VALUES ('박서함', 30, '서울');```

```SQL
SELECT rowid, * FROM classmates; 
-- rowid 자동으로 넣어주고 있었다 
-- sqlite에서 자동으로 제공하고 있는 pk. 값이 1씩 증가하는 모습을 보임
-- * :auto increment 자동으로 증가하는 숫자를 로우아이디로 기록 


SELECT name FROM classmates;
```



```sqlite
CREATE TABLE classmates (
	name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
)

INSERT INTO classmates ('홍길동', 30, '서울'), ('김철수', 30, '제주'), ('이호영', 26, '인천');
```



### SELECT

+ Query data from a table
+ 테이블에서 데이터를 조회 

##### LIMIT

##### WHERE

##### SELECT DISTINCT

+ READ ONLY id, name from the table

```sql
SELECT rowid, name FROM classmates;
```

* id, name on one culum from Classmate table

```sql
SELECT rowid, name FROM classmates LIMIT 1; 
-- 홍길동만 나옴
SELECT rowid, name FROM classmates LIMIT 2; 
-- 홍길동, 김철수 까지 2줄 
```

+ 세번째 하나만 어케 ? 
+ 얘도 파이썬때처럼 생각하기, 2칸 띄우고 세번째꺼니까 2

```sql
SELECT rowid, name FROM classmates LIMIT INT OFFSET 2;
```

+ Offset : 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형 
+ limit 2 offset2 는 슬라이싱처럼 2칸 뒤부터 2개 

+ 주소가 서울인 경우

```SQL
SELECT * FROM classmates WHERE address='서울';
```

\* == 전부 

Ex. *.txt = 확장자 txt인 애들 다 

+ 30살 이상 

```sql
SELECT name FROM classmates WHERE age >= 30;
```

+ 중복 없이 조회, distinct 어떤 컬럼 중복 없이 보자 

```sql
SELECT DISTINCT age FROM classmates;
-- 나이만 중복없이 보자 
```

+ 삭제

```sql
DELETE FROM classmates WHERE rowid=5; 
```

+ 위는 자동으로 넘버링해주는거라 중간에꺼 지우면 12345 -> 1235 가 아니라 1234 되는데 어떤 메커니즘이 있는 애들은 갱신 안되고 12356 이렇게 됨 4번 빈채로 

```sql
UPDATE classmates SET address='서울' WHERE rowid=5;
SELECT rowid * FROM classmates;
--- 5번 사람 주소 서울로 변경
```

+ 5열 밖에 없는데 LIMIT 100 이런거 써도 out of range 이런거 ㄷ안뜨고 있는대로 5열만 읽어줌 