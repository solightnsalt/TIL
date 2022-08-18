-- SQLite
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INT NOT NULL, 
  sido TEXT NOT NULL,
  phone TEXT  NOT NULL, 
  balance INT NOT NULL
);

.mode csv
.import users.csv users

SELECT * FROM users;

.headers on
.mode column

CREATE TABLE test (for, what);
DROP TABLE test;
sqlite> .tables

.schema users
CREATE TABLE users (first_name TEXT NOT NULL, last_name TEXT NOT NULL, age INT NOT NULL, sido TEXT NOT NULL, phone TEXT  NOT NULL, balance        
 INT NOT NULL);

--INSERT INTO users (first_name, age) VALUES ('유진', '18');
--Runtime error: NOT NULL constraint failed: users.last_name (19)
INSERT INTO users VALUES ('유진', '안', 18, '서울시', 010-6541-6871, 3992998);

SELECT rowid FROM users;

SELECT COUNT(*) FROM users;
-- COUNT(*)
-- --------
-- 1001

-- 1001번째 하나 이름, 잔고
SELECT first_name, balance FROM users LIMIT 1 OFFSET 1000;
-- first_name  balance
-- ----------  -------
-- 유진          3992998

SELECT first_name, sido FROM users WHERE sido = '서울시';
-- first_name  sido
-- ----------  ----
-- 유진          서울시

-- 시도 중복없이 
SELECT DISTINCT sido FROM users;
-- sido
-- -------
-- 전라북도
-- 경상남도
-- 전라남도
-- 충청남도
-- 충청북도
-- 경기도
-- 제주특별자치도
-- 경상북도
-- 강원도
-- 서울시

DELETE FROM users WHERE rowid = 1001;

UPDATE users SET first_name='유진', last_name='안' WHERE rowid=1000;

SELECT * FROM users WHERE rowid=1000;
---이까지 0816

SELECT * FROM users WHERE age >= 30;

SELECT first_name, last_name FROM users WHERE age >= 30;

SELECT first_name, age FROM users WHERE age >= 30 AND last_name='김';

-- 1. 시도가 경상남도거나, 2. 경상북도면서 30세인 사람
SELECT * FROM users WHERE sido='경상남도' OR sido='경상북도' AND age = 30; 
-- 1. 시도가 경상남도이거나 경상북도이면서 2. 30세인 사람
SELECT * FROM users WHERE (sido='경상남도' OR sido='경상북도') AND age = 30; 

--BETWEEN
SELECT * FROM users WHERE sido='경상남도' AND age BETWEEN 20 AND 30; 
--IN
SELECT * FROM users WHERE sido='제주특별자치도' AND last_name IN ('부', '고', '양', '초', '좌'); 
--NOT IN
SELECT * FROM users WHERE last_name NOT IN ('김', '이', '박'); 
--LIKE
SELECT phone FROM users WHERE phone LIKE '02-%';
--null허용으로 변경 이거는 SQLITE는 안된다고함.. 
--ALTER TABLE users ALTER COLUMN balance integer NULL;
--1.제약조건을 포함한 새로운 스키마로 새테이블 만들어서 데이터복사 
.schema users
CREATE TABLE new_users (first_name TEXT NOT NULL, last_name TEXT NOT NULL, age INT NOT NULL, sido TEXT NOT NULL, phone TEXT  NOT NULL, balance        
 INT NULL);
--2.기존 테이블에서 새테이블로 데이터 복사 
INSERT INTO new_users SELECT * FROM users;
--3.기존테이블 삭제 
DROP TABLE users;
--4.새테이블 이름 기존테이블로 변경 
ALTER TABLE new_users RENAME TO users;

-- DELETE balance FROM users WHERE rowid=1000;
-- 위에 효과를 노린게 아래거인가봄
UPDATE users SET balance='' WHERE rowid=1000;
--null 왜 안나오지.... 빈게 아닌가 암튼 이렇게 쓴다..
SELECT * FROM users WHERE balance IS NULL;

SELECT COUNT(*) FROM users WHERE balance > 500000;
-- COUNT(*)
-- --------
-- 137
SELECT AVG(balance) From users WHERE sido='경기도';
-- AVG(balance)
-- ----------------
-- 138846.929824561
SELECT SUM(balance) FROM users WHERE sido='제주특별자치도';
-- SUM(balance)
-- ------------
-- 17178400
SELECT MAX(balance), first_name FROM users WHERE balance !='';
-- MAX(balance)  first_name
-- ------------  ----------
-- 1000000       순옥
-- 지금 rowid=1000 유진이는 null아니고 공백임 따라서 IS NOT NULL X
SELECT MIN(age), balance FROM users;
-- 2%, %2, %2%, _2%, 등 다양하게 활용하기 
SELECT * FROM users WHERE age LIKE '_7';
--order by
SELECT * FROM users ORDER BY age;
SELECT * FROM users ORDER BY balance, age DESC LIMIT 10;
SELECT * FROM users ORDER BY balance, age DESC LIMIT 10;
-- first_name  last_name  age  sido     phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 현숙          곽          15   충청남도     016-7423-1481  710000
-- 정남          박          15   경상북도     010-3772-2402  660000
-- 서영          김          15   제주특별자치도  016-3046-9822  640000
-- 지민          정          15   제주특별자치도  02-2765-8053   630000
-- 재호          김          15   전라남도     02-4375-8097   420000
-- 상호          이          15   강원도      010-3611-9776  310000
-- 정식          김          15   충청남도     02-5538-3528   160000
-- 예준          김          15   충청북도     016-3898-3279  150000
-- 은영          이          15   전라남도     010-5284-4904  78000
-- 예준          김          15   충청남도     02-9726-5034   76000
SELECT * FROM users ORDER BY age, balance DESC LIMIT 10;
-- first_name  last_name  age  sido     phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 진우          김          33   경기도      02-1114-4892   150
-- 우진          성          32   전라북도     010-7636-4368  150
-- 광수          김          32   충청남도     02-7695-5421   150
-- 승민          김          28   경기도      010-2919-6864  150
-- 민재          오          20   전라남도     011-2524-3749  150
-- 수민          김          36   경상북도     016-3424-9936  160
-- 명자          김          32   전라남도     016-2871-7505  160
-- 지아          허          25   전라남도     010-8679-1685  160
-- 순옥          성          23   제주특별자치도  011-4667-2759  160
-- 현숙          김          37   강원도      02-2389-8172   170

