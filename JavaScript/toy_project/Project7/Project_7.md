# 40 JavaScript Projects for Beginners
> Easy Ideas to Get Started Coding JS



## Project 7 - How to create a FAQ page

![faqpage](https://www.freecodecamp.org/news/content/images/size/w1000/2021/03/FAQ-section.png)

#### FAQ 페이지 만들기

이 [튜토리얼](https://www.youtube.com/watch?v=3PHXvlpOkf4&t=6506s)에서는 FAQ(자주 묻는 질문) 페이지를 만드는 방법에 대해 소개합니다. 
사용자들에게 사업 내용을 알려주고 유기적인 검색 결과를 통해 웹 사이트로 유입시키고자 할 때 사용됩니다.



#### Key concepts covered:

+ `document.querySelectorAll(selectors)`

  + `()` 안의 유효한 CSS 선택자 또는 선택자 뭉치와 일치하는 document 내 모든 요소를 반환

  + 일치하는 요소가 있으면 정적 `NodeList`를 반환한다.

    > 일치하는 요소가 없으면 `null`이 반환되는 것이 아니라 빈 `NodeList`가 반환된다.
    >
    > 관련 메서드, for loop활용법은 [`MDN문서`](https://developer.mozilla.org/ko/docs/Web/API/NodeList) 참고

  

+ `EventTarget.addEventListener()`

  + 이벤트의 대상이 될 수 있는 객체 `EventTarget`(대표적으로 `Element`, `Document`, `Window` 등..)에 지정한 특정힌 유형의 이벤트를 대상이 수신할 때마다 호출할 함수를 등록하는 메서드
  + 이 메서드에 지정하는 이벤트 수신기는 콜백함수 또는 콜백으로 작동할 `handleEvent()`메서드를 포함하는 객체

  

+ `NodeList.forEach()`

  + `document.querySelectorAll()`로 받아온 `NodeList`에 적용하는 메서드

  + `NodeList`의 각 요소마다 인자로 전달 받은 함수를 실행하여 요소를 인수로 함수에 전달한다.

    (리스트 내의 각각의 값 쌍에 대해 매개 변수에 지정된 콜백을 삽입 순서로 호출?)

    ```js
    NodeList.forEach(callback[, thisArg]);
    ```

    

+ `Element.classList`

  + `Element`의 클래스 속성 컬렉션을 반환하는 읽기 전용 프로퍼티지만 메서드를 이용하여 변형할 수 있다.
  + `remove( String [, String [, ...]] )` : `()`안 지정한 클래스 값을 제거한다.
  + `toggle( String )` : 클래스가 있으면 제거하고, 없으면 추가




#### 정리

##### 방법 1 객체들 가로질러서 

1. 버튼 전체를 변수로 지정하고 
2. `forEach()`로 각각에 콜백함수를 전달하는데
3. 그 각각에 어떤 이벤트 발생 시 (클릭)
4. 걔네의 부모의 부모요소를 찾아서
5. class를 빼거나 추가



##### 방법 2 요소 안의 선택자를 사용

1. 박스들을 먼저 변수로 받아와서 
2. `forEach()`로 다시 각 박스 안에 버튼을 찾고 
3. 그 버튼에 이벤트 발생 시 
4. `.show-text` 클래스가 있는 버튼과 이벤트 발생한 버튼이 동일하지 않으면
5. 전자에서 해당 클래스 빼고 후자에 class 추가
6. 같으면 이벤트 발생한 버튼만 빼거나 추가



> 두 방법 다 어쨌든 css랑 잘 연결하는게 관건인 것 같다.
>
> 자스로는 .show-text만 넣고 뺐을 뿐인데 css를 똑똑하게 잘 짠 듯.. 

