# SQL



## CASE

+ 특정 상황에서 데이터를 변환하여 사용할 수 있음 

+ ELSE를 생략하는 경우 NULL값이 지정됨 

```sql
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
```



### 적용예시 

1. 

```sql
SELECT id
	CASE
		WHEN gender=1 THEN '남자'
		WHEN gender=2 THEN '여자'
	END AS "성별"
FROM healthcare
LIMIT 5;
-- 여기서 gender에 공백값이 있었다 등등 when으로 조건지정해준거에 해당하지 않는게 있을때
-- else 값이 없으면 NULL로 표시되기 때문에 
-- 웬만하면 NULL을 꼭 입력해주는 것이 좋다 	
```

2. 

```sql
-- 흡연자 분류 확인 
SELECT DESTINCT smoking 
FROM healthcare
-- 적용
SELECT id, smoking
	CASE 
		WHEN smoking = 1 THEN '비흡연자'
		WHEN smoking = 2 THEN '흡연자'
		WHEN smoking = 3 THEN '헤비스모커'
		ELSE '무응답'
	END
FROM healthcare
LIMIT 50;
```

3. 

```SQL
SELECT first_name, last_name, 
	CASE 
		WHEN age <= 18 THEN '청소년'
		WHEN age <= 40 THEN '청년'
    WHEN age <= 90 THEN '중장년'
    ELSE '노년'
	END
FROM users
LIMIT 10;
```





## 서브쿼리 

+ 특정한 값을 메인 쿼리에 반환하여 활용하는 것 

+ 실제 테이블에 없는 기준을 이용한 검색 가능 

+ 소괄호로 감싸서 사용, 메인쿼리 컬럼 모두 사용 가능 But 메인쿼리는 서브쿼리 컬럼 이용 못 함



### 적용 예시

0. 전에 배운걸로만 했을 때

```SQL
-- 가장 나이가 적은 사람의 수 기존 방법
SELECT COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1; 
-- 이렇게 하면 나이순으로 분류해서 나이 내림차순으로 인원수 계산해주는데 리미트 1을 걸어서 젤 어린 사람 수만 출력 
  
-- 위에꺼 재확인 과정 
-- 1. 먼저 젤 어린 사람 찾고 
SELECT MIN(age)
FROM users;
-- 2. 조건 걸어서 그 수만 출력
SELECT COUNT(*)
FROM users
WHERE age = 15;
```



#### 단일행 서브쿼리

##### `WHERE` 에서의 활용 

  1. 가장 나이가 적은 사람의 수

  ```sql
  SELECT COUNT(*)
  FROM users
  WHERE age = (SELECT MIN(age) FROM users); 
  -- 소괄호 안에 1번 내용이 들어가있음 
  ```

2. 평균 계좌 잔고보다 높은 발란스 가지고 있는 사람의 수 

  ```sql
  SELECT COUNT(*)
  FROM users
  WHERE balance > (SELECT MAX(balance) FROM users);
  ```

3. users에서 유은정과 같은 지역에 사는 사람의 수

  ```sql
  SELECT COUNT(*)
  FROM users
  WHERE sido = (SELECT sido FROM users WHERE last_name='유'AND fist_name='은정');
  ```

##### `SELECT `에서의 활용

  ```sql
  -- 기존
  SELECT COUNT(*), AVG(balance), AVG(age)
  FROM users;
  
  -- 서브쿼리 예시 
  -- 테이블 하나인 경우는 그냥 위에 기존처럼 쓰면됨
  -- 다른테이블의 정보를 지금 사용하는 테이블에 계산해서 옮겨올 때 활용
  SELECT
  	(SELECT COUNT(*) FROM users) AS 총인원 
  	(SELECT AVG(balance) FROM users) AS 평균연봉;
  ```

##### `UPDATE` 에서의 활용 

  ```sql
  UPDATE users
  SET balance = (SELECT AVG(balance) FROM users);
  ```



#### 다중행 서브쿼리
> 함정 주의 

```sql
-- Q. users에서 유은정과 같은 지역에 사는 사람의 수를 이은정으로 바꾸면 ? 
SELECT COUNT(*)
FROM users
WHERE sido = (SELECT sido FROM users WHERE last_name = '이' AND fist_name = '은정'); 
-- 나오기는 하는데 틀린 값 나옴 왜냐 ? 
-- 전라북도랑 경상북도에 각각 이은정 한 명 씩 있어서  
SELECT sido FROM users WHERE last_name='이' AND fist_name = '은정';
-- sido
-- ----
-- 전라북도 
-- 경상북도
-- 그럼 어떻게 ? 
```

```SQL
SELECT COUNT(*)
FROM users
WHERE sido IN 
(SELECT sido FROM uses WHERE last_name = '이' AND first_name = '은정');
-- 위와 같이 작성하면 두 지역의 이은정 수 합한 값으로 출력해줌.
```

+ 서브쿼리 결과가 2개인 경우 
+ 다중행 비교 연산자와 함께 사용(IN, EXISTS)



#### 다중컬럼 서브쿼리 

```sql
-- Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이 
-- 필요한 것 : 성, 최연소 나이 
SELECT last_name, first_name, age 
FROM users
WHERE (last_name, age) IN 
(SELECT last_name, MIN(age) FROM users GROUP BY last_name) 
ORDER BY last_name; 
```



###### 내일 할 거 미리보기

* 다중테이블 쓸 때는 테이블이랑 스키마 계속 조회해가면서 정확하게 진행하기 

```sql
SELECT * 
FROM Albums 
WHERE ARTISTID = (SELECT ArtistID FROM artists WHERE Name = 'AC/DC');
```

