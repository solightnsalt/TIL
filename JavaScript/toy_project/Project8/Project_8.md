# 40 JavaScript Projects for Beginners

> Easy Ideas to Get Started Coding JS



## Project 8 - How to create a restaurant menu page

![menupage](https://www.freecodecamp.org/news/content/images/size/w1000/2021/03/menu.png)

#### 식당 메뉴판 만들기

이 [튜토리얼](https://www.youtube.com/watch?v=3PHXvlpOkf4&t=8185s)에서는 레스토랑의 메뉴를 필터링해주는 페이지를 만드는 법에 대해 소개합니다. 

재미있는 이 프로젝트를 통해 map, reduce, filter와 같은 고차 함수에 대해서도 학습할 수 있습니다.



Yazeed Bzadough는 [이 글](https://www.freecodecamp.org/news/a-quick-intro-to-higher-order-functions-in-javascript-1a014f89c6b/)에서 '*고차 함수의 가장 큰 이점은 엄청난 재사용성에 있다*.'라고 언급하고 있습니다.



#### Key concepts covered:

+ 배열(`arrays`)
  + js에서 순서가 있는 컬렉션을 저장할 때 쓰는 자료구조
  + 생성자 `Array()`를 사용하거나 다음과 같이 `let deserts = ["cake", "icecream", "cookie"];` 주로 대괄호를 사용하여 선언
  + 수정 : `desert[2] = 'candy';`
  + 추가 : `desert[3] = 'jelly';` 등 다양하게 조작 가능하다.



+ 객체(`objects`)

+ `forEach()`

+ `DOMContentLoaded` (= `Event`)

  + 초기 HTML 문서를 완전히 불러오고 분석했을 때 발생(처음 페이지 열거나 새로고침하거나 문서 열 때)하고, style sheet나 이미지 등의 로딩은 기다려주지 않는다.

  + `document`객체에서 발생하기 때문에 이 이벤트를 다루기 위해 `addEventListener`를 사용한다.

  + ex. `document.addEventListener("DOMContentLoaded", ready);`

    

+ `map, reduce, and filter`

  + 장고 템플릿처럼 사용 가능한 배열의 메서드들
  + `map()` : 배열 내 모든 요소에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환.
  + `reduce()` : 배열의 각 요소에 대해 주어진 reducer 함수를 실행하고 하나의 결괏값을 반환.
  + `filter()` : 주어진 함수의 테스트를 통과하는 모든 요소를 모아서 새로운 배열로 반환.

  

+ `Element.innerHTML`

  + 요소 내에 포함된 HTML 또는 XML 마크업을 가져오거나 설정한다.
  + 보안 위험이 있으니 일반 텍스트 삽입 시에는 사용하지 않는 것이 좋다.

  

+ `includes` method

  + 얘도 배열의 메서드. 배열이 특정 요소를 포함하고 있는지 판별한다.