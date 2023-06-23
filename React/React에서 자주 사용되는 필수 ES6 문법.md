# React에서 자주 사용되는 필수 ES6 문법

1. 상수와 변수
   + 상수 : `Const` (=constant : 변함없는 수, 재할당이 안되나 내부 속성값은 수정 가능)
   + 변수 : `let` (재할당 가능)



2. 객체(Object) 선언, 단축 속성, 객체 복사

   + key - value pair 항상 기억하기

   + value에는 어떤 형태라도 쓸 수 있다.

     `{doSth : () => ()}`

   + 아래와 같이 생략 가능

   ```javascript
   name = '안보현'
   profile = {
       name,
       doSth : () => ()
   }
   ```

   + *얕은 복사, 깊은 복사*

     + 얕복을 방지하기 위해 쓰는 방법들 알아두기 

       (ex. `JSON.parse(JSON.stringify(obj))`, `map`, `filter` 등 )

3. Template Literals

   ```javascript
   // 일반 텍스트
   `string text`
   
   // 멀티라인
   `string text line 1
    string text line 2`
   
   // 플레이스 홀더를 이용한 표현식
   `string text ${expression} string text`
   ```

4. 구조분해 할당(De + structure)

   + 객체

     ```javascript
     const person = {
     	name: '르탄',
     	age: '21'
     }
     
     function hello({name, age}) {
     	console.log(`${name}님, ${age}살이시네요!`);
     }
     
     hello(person);
     ```

   + 배열

     ```javascript
     const testArr = [1, 2, 3, 4, 5];
     const [val1, val2, val3, val4, val5] = testArr;
     
     console.log(val1);
     ```

   5. 전개 연산자(Spread Operator)

      ```javascript
      let names = ["Steve", "John"];
      let students = ["Tom", ...names];
      ```

   6. 화살표 함수(Arrow Functions)

      ```javascript
      function mysum1(x, y) {
          return x + y;
      }
      
      const mysum2 = (x, y) => x + y;
      const mysum2 = (x, y) => {
          return x + y
      };
      console.log(mysum1(1, 2));
      console.log(mysum2(1, 2));
      ```

      