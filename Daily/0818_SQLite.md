# 기본 함수와 연산

## 문자열 함수

+ 실제 DB값이 변경되는 것은 아니고 출력만 내가 쿼리문으로 요구한 형태로 나오는 것 

  + DB 변경은 `UPDATE` 로만 가능 

+ SUBSTR(str, start, length) : 문자열 자르기

  + 시작 인덱스는 1, 마지막 인덱스는 -1  

+ TRIM(문자열), LTRIM(문자열), RTRIM(문자열) : 문자열 공백 제거 

+ LENGTH(문자열) : 문자열 길이 

  ```sql
  SELECT LENGTH(first_name) FROM users; 
  ```

+ REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경

  ```SQL
  SELECT REPLACE(phone, '-', '') FROM users;
  ```

+ UPPER, LOWER : 대소문자 변경

+ || : 문자열 합치기 (!=alph 'I', =vertical bal) concatenation

  ```sql
  SELECT last_name || first_name 이름 FROM users; 
  ```






## 숫자 함수

+ ABS(숫자) : 절대값
+ SIGN(숫자) : 부호 (양수 1, 음수 -1, 0 0)
+ MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나눈 나머지
+ CEIL(숫자), FLOOR(숫자) : 천장. 바닥ㅋㅋ 올림, 내림, 
+ ROUND(숫자) 또는 (숫자, 자리) : 반올림
+ POWER(숫자1, 숫자2) :숫자 1의 숫자2 제곱
+ SQRT(숫자) : 제곱근



# GROUP BY

+ 단일 행이 나온다 라는 개념?.....

+ Select 문의 optional 절 

+ 행 집합에서 요약 행 집합을 만듦

+ 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦 

+ **문장에 where 절이 포함된 경우 반드시 where절 뒤로 가야함 **

  `SELECT * FROM users GROUP BY last_name;`

  + distinct랑 같은거 아냐 ? 아님 

  ```sql
  SELECT AVG(age) FROM users GROUP BY 성;
  -- 전체 나이평균이 아닌, 성 별로 평균 나이가 구해진다 
  ```

+ 행들의 집계함수를 뭐시기



***Ex)  성 별 인원수***

```sql
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- group by 에서 활용하는 컬럼을 제외하고는 집계함수를 써라. 왜냐? 위 쿼리문에서 select age 해버리면 의미없는 값이 나옴 
-- 하지만 AVG(age) 를 껴넣으면 의미있는 성씨별 평균 나이가 구해짐
```

+ `GROUP BY`는 결과가 정렬되지 않는다. 기존 순서와 바뀜 
+ 원칙적으로 내가 정렬해서 보고 싶으면 꼭!  `ORDER BY`를 써주기 

```sql
--GROUP BY WHERE 을 쓰고 싶다.
--100번 이상 등장한 성만 출력하고 싶음.
SELECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name)>100 GROUP BY last_name; 
-- 이거 안 됨 !!!!! count 같은 집계함수는 SELECT 절 바로 뒤에만 사용 가능하다 

--조건에 따른 GRUOP 하려면 HAVING을 쓴다 
SELECT SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name HAVING COUNT(last_name)>100;
```

### HAVING

+ 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 이용

  ```sql
  SELECT * FROM TABLE_NAME GROUP BY COLUMN1, COLUMN2 HAVING GROUP CONDITION;
  ```

  



# SELECT 문장 실행 순서 

1. FROM 테이블을 대상으로
2. WHERE 제약조건에 맞춰서 뽑아서 
3. GROUP BY 그룹화한다
4. HAVING 그룹 중에 조건과 맞는 것 만을 
5. SELECT 조회하여
6. ORDER BY 정렬하고 
7. LIMIT/OFFSET 특정 위치의 값을 가져온다.

```SQL
SELECT 칼럼명
FROM 테이블명
WHERE 조건식
GROUP BY 칼럼 혹은 표현식
HAVING 그룹조건식
ORDER BY 칼럼 혹은 표현식
LIMIT 숫자 OFFSET 숫자;
```



# ALTER TABLE

+ 테이블 이름 변경

  ```sql
  ALTER TABLE table_name RENAME TO new_name;
  ```

+ 새로운 column 추가
	```sql
  ALTER TABLE table_name ADD COLUMN column_defimition;
  ```
+ Column 이름 수정 
	```sql
  ALTER TABLE table_name RENAME COLUMN current_name TO new_name;
  ```
+ Column 삭제
	```sql
  ALTER TABLE table_name DROP COLUMN column_name;
  ```



🧐***주의***  임시테이블명 member

| id   | name    | age  | `gender TEXT NOT NULL`  된다? 안된다? |
| ---- | ------- | ---- | ------------------------------------- |
| 1    | Jame    | 26   | 안된다                                |
| 2    | John    | 28   |                                       |
| 3    | Michael | 30   |                                       |

> ```SQP
> sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
> Error: Cannot add a NOT NULL column with default value NULL
> ```
>
> 머선뜻? 
>
> 새로 컬럼을 생성하게 되면 테이블에 있던 기존 레코드들의 경우에는 그 컬럼에 대한 정보가 없기 때문에 NULL로 입력된다.
>
> 따라서 NOT NULL 형태의 컬럼은 추가 불가능

* 해결방법

  1. 아싸리 NOT NULL 설정 없이 추가하기

  2. 새로운 컬럼을 만들면서 DEFAULT값으로 임시로 채워넣기 

     ```sql
     sqlite> ALTER TABLE member ADD COLUMN gender TEXT NOT NULL DEFAULT 'F or M';
     ```

     











