# JOIN

+ 관계형 데이터베이스의 가장 큰 장점이자 핵심 기능 
+ 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 데이터를 저장하는 것이 아닌 여러 테이블로 나눠 저장
+ 여러 테이블을 결합(join)하여 출력하여 활용 
+ 일반적으로 레코드는 기본키 pk나 외래키 fk 값의 관계에 의해 결합함



## 예시

| id   | title | content | writher | role |
| ---- | ----- | ------- | ------- | ---- |
|      |       |         |         |      |

+ 위 테이블 하나로 만들면 수정시 모든 항목을 수정해야함 

**but**

1. 질문 데이터

| id(pk) | title | content      | User_id(fk) |
| ------ | ----- | ------------ | ----------- |
| 1      | git   | 커밋어케해여 | 1           |

2. 유저 정보

| id(pk) | name   | role_id(fk) |
| ------ | ------ | ----------- |
| 1      | 홍길동 | 1           |

3. 역할 정보 

| Id(pk) | role    |
| ------ | ------- |
| 1      | Student |



+ 이런식으로 모든 항목을 하나의 테이블로 만든 후  
+ 필요한 항목을 키로 뽑아서 조합해서 쓰는 것이 조인

+ 그래야 뭐 하나 변경됐을때 하나하나 다 변경해야하는게 아니라 

  세부 항목 테이블의 요소 하나 변경하면 그 아이디 뽀려서 쓰기 때문에 전체 테이블 수정할 필요x

+ 매우 간편~! 



## join queries

![rdb](https://t1.daumcdn.net/cfile/tistory/225AA63458A51E2B07)



#### INNER JOIN 

+ (INNER) 생략가능 

```sql
SELECT * FROM users INNER JOIN role ON users.role_id = role.id;
SELECT users.name, role.title FROM users INNER JOIN role ON users.role_id = role.id;
```

+ 조인 한거에 where로 조건 걸수도 있다 

```sql
SELECT * FROM users INNER JOIN role ON users.role_id = role.id WHERE role.id = 2;
```

+ 여러개 테이블을 결합하고 있기때문에 그냥 column명만 쓰는 것이 아니라 무슨 테이블의 컬럼인지 같이 써줘야됨 

```sql
SELECT * FROM users INNER JOIN role ON users.role_id = role.id ORDER BY users.name DESC;
```



#### OUTER JOIN 

+ 동일한 값이 없는 데이터도 반환할 때 사용 

```sql
SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id;
```

  * 따로 조건 null 이런거 안써도 된다.  알아서 채워줌 

    * 근데 결과에서 null인 항목 빼고 싶다 ? 

    ``` sql
    SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id WHERE article.user_id IS NOT NULL;
    ```

  * 기준이 되는 따라 left .. 뭐시기 



#### FULL OUTER JOIN

+ Outer 조회에선 아우터에서 없는 항목은 오른쪽에 안나왔는데 
+ 풀은 왼쪽꺼에 맞게 오른쪽 가져왔다가, 오른쪽에 안 가져와진거 다 가져와서 중복인거 삭제 ok? 

```sql
SELECT * FROM articles FULL OUTER JOIN users ON articles.user_id = users.id;
```



#### CROSS JOIN

+ 모든 경우의 수를 다 JOIN

```SQL
SELECT * FROM users CROSS JOIN role:
-- 총 9개의 레코드가 조회됨
```



#### 참고

+ [SQL Joins Visualizer](httls://www.sql-joins.leopard.in.ua)



##### 연습,,, 

+ A, B 가 있을 때
  + 이너 조인은 교집합

	```sql
  SELECT * FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId;
  ```
  
  + 아우터조인은 교집합 포함 A 전체
  ```SQL
  SELECT * FROM albums LEFT JOIN artists ON albums.ArtistId = artists.ArtistID;
  ```





