# JavaScript

+ lightweight, interpreted, or just-in-time compiled programming language with first-class functions
>**JIT 컴파일**(just-in-time compilation) 또는 **동적 번역**(dynamic translation)은 프로그램을 실제 실행하는 시점에 기계어로 번역하는 컴파일기법이다.
>
>전통적인 입장에서 컴퓨터 프로그램을 만드는 방법은 두 가지가 있는데, 인터프리트 방식과 정적 컴파일 방식으로 나눌 수 있다. 이 중 인터프리트 방식은 실행 중 프로그래밍 언어를 읽어가면서 해당 기능에 대응하는 기계어 코드를 실행하며, 반면 정적 컴파일은 실행하기 전에 프로그램 코드를 기계어로 번역한다.
>
>JIT 컴파일러는 두 가지의 방식을 혼합한 방식으로 생각할 수 있는데, 실행 시점에서 인터프리트 방식으로 기계어 코드를 생성하면서 그 코드를 캐싱하여, 같은 함수가 여러 번 불릴 때 매번 기계어 코드를 생성하는 것을 방지한다.

+ 크로스-플랫폼, 객체지향 스크립트 언어 (객체의 형 간에 차이 없음)

+ 숫자, 불리언, 그리고 문자열 값을 표현하는 적은 수의 자료 형을 기반으로 한 런타임 시스템

+ 프로토타입 기반 객체 모델 > 동적 상속. 즉, 속성과 메서드는 어떤 객체든 동적으로 추가될 수 있음.

+ 어떤 특정한 선언을 요구하지 않는 함수도 지원. 

  + 함수는 객체의 속성이나, 타입이 느슨하게 형지정된 채 실행되는 메소드가 될 수 있다.
  + (dynamic typing, loosely typed)



## basics

+ 웹사이트([HTML](https://developer.mozilla.org/ko/docs/Glossary/HTML) 문서에 적용될 때)에 동적 상호작용성을 더해 주는 프로그래밍 언어

> ex. 게임, 버튼이 눌리거나 폼에 자료가 입력될 때 반응, 동적인 스타일링과 애니메이션

> **Note:**  <script> 요소를 HTML 파일의 맨 아래쪽 근처에 둔 이유는 **the browser reads code in the order it appears in the file**. If the JavaScript loads first and it is supposed to affect the HTML that hasn't loaded yet, there could be problems. Placing JavaScript near the bottom of an HTML page is one way to accommodate this dependency.



### 변수 Variables

+ 값을 저장할 수 있는 컨테이너
+ 변수를 선언할 때 `var` 또는 `let` 키워드 뒤에 원하는 변수명 붙이면 됨



#### 주의할 점 

1. [When do you need a semicolon?](https://www.codecademy.com/resources/blog/your-guide-to-semicolons-in-javascript/)
   
   + Required: When two statements are on the same line
   + Optional: After statements
   + Avoid!
	
	  1. **After a closing curly bracket ** (`var obj = {};`)
	
	  2. **After the round bracket of an if, for, while or switch statement**
	
	     (`alert ("hi");`)
	
	+ Exception !
	 ```javascript
	  for (var i=0; i < 10; i++)  {/*actions*/}       // correct
	  for (var i=0; i < 10; i++;) {/*actions*/}       // SyntaxError
	 ```

2. 변수 이름 규칙 Naming Conventions
   + under bar `_` o. hypen `-` x
   + 숫자로 시작 x. `_` or `$` 이런거는 시작 가능
   + 예약어 x
   + 

2. 자바스크립트는 대소문자를 구분한다! 