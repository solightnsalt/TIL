# Django

## Namespace

+ `<a href = ''>`

+ `name = "이 겹칠 때 



### URL namespace

+ App_name attribute를 작성하여 url namespace를 설정한다. 
  + `app_name = 'articles'`이 코드를 urls.py에 추가해준다.  



## DRY원칙

+ don't repeat yourself 
  + ​	소스코드에서 동일한 코드를 반복하지 말자는 뜻 



## Django의 설계 철학 (Templates Sytem)

1. 표현templates과 로직view을 분리 
   + 템플릿 시스템은 표현을 제어하는 도구이자 표현을 하는 도구일 뿐 ! 





2. 중복을 배제
   + 대다수의 동적 웹사이트는 공통 헤더, 푸터, 네브바 같은 사이트 공통 디자인을 가진다 
   + 장고 템플릿 시스템은 이런 요소를 한 곳에 저장하기 쉽게 하여 중복코드를 없애야함



#### framwork의 성경

+ 독선적

+ 관용적

장고는? 

+ 다소 독선적. 양쪽 모두에게 최선의 결과를 준다고 강조 
+ 





Convention over configuration 설정 보다는 관례 



## design pattern

### MVC 소프트웨어 디자인 패턴

+ model : 데이터와 관련된 로직을 관리
+ view : 레이아웃과 화면을 처리
+ controller : 명령을 model과 view 부분으로 연결 
+ 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론 
+ 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴 

> 각자가 잘하는 것만 하자



### MTV

+ 장고는 mtv based on mvc pattern 
+  두 패턴은 크게 다른점은 없고 부루는 용어가 다름 
+ model - template - view



#### Model

+ 데이터와 관련된 로직을 관리 
+ 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 



#### Template

+ 레이아웃과 화면을 처리 
+ 화면상의 사용자 인터페이스 구조



#### View

+ 모델 & 템플릿과 관련한 로직을 처리해서 응답을 반환 
+ 클라이언트의 요청에 대해 처리를 분기하는 역할 



## Database 

+ 체계화된 데이터의 모임 
+ 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장시스템 



### 기본 구조 

1. 스키마 
   + 뼈대
   + 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조 

#### 테이블 

​	필더 

​	Pk



## Model 

+ 모델로 데이터 관리 
+ 아 왜케 잠오냐 도랏냐고 
+ 모텔 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것 



## CRUD hell week 

홧팅







