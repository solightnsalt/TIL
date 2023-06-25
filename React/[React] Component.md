# React Component

+ 컴포넌트를 통해 UI를 재사용이 가능한 개별적인 여러 조각으로 나누고, 각 조각을 개별적으로 살펴볼 수 있다.
+ 컴포넌트는 개념적으로 Javascript 함수와 유사하다.
  + JS : input -> output
  + ***React : props -> React element***





## 함수형 컴포넌트와 클래스형 컴포넌트

+ 함수형 컴포넌트와 클래스형 컴포넌트는 기능상으로는 동일하지만, React 공식 홈페이지에서 권장하는 컴포넌트 방식은 <u>*함수형 컴포넌트*</u>이다.



**함수형 컴포넌트**

```react
// 1. input으로 props라는 입력을 받으면 
// 2. output으로 화면에 어떻게 표현되는지를 기술하는 React 엘리먼츠를 반환한다.

function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App () {
	return <div>hello</div>
}
```



**클래스형 컴포넌트**

```react
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```





## 컴포넌트 관점에서 보는 CRA pjt

ex. `pjt/src/App.js`

```react 
import './App.css'; //컴포넌트 밖 1. 가져온다. 무엇을?? 내가 필요한 파일을

function App() {
    // 자바스크립트 코드 작성 영역
    
    const x = 1;
    function testFunc () {
        어쩌구어쩌구
    }
    
  return (
      // 리턴문 안 JSX(Javascript + XML + HTML) 작성 영역
      // Javascript는 중괄호{} 안에 작성
    <div className="App">
      <p>Hello React</p>
    </div>
  );
}

export default App; //2. 내보낸다. 무엇을?? 내가 만든 컴포넌트를
```

※주의, 

+ 컴포넌트 이름은 무조건 대문자로 시작!!!!!
+ 폴더는 소문자로 시작하는 카멜케이스

+ 스타일은 쟉스 영역 안 필요한 곳에 key-value pair로 작성

  ```react
      <div
        style={{  /* 중괄호 안에 객체를 넣어준 것 */
          height: '100vh',
          display: ' flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
  ```

  



## 컴포넌트의 부모자식 관계

+ 컴포넌트 안에 또다른 컴포넌트가 들어갈 수 있다.

  -> 컴포넌트{컴포넌트{컴포넌트{}}}

  + 다른 컴포넌트를 품는 컴포넌트 = 부모 컴포넌트
  + 다른 컴포넌트 안에서 품어지는 컴포넌트 = 자식 컴포넌트

  ```react
  // src/App.js
  import React from "react";
  
  function Child() {
    return <div>응애</div>; //app 속의 child
  }
  
  function App() { 
    return <Child />; // app은 child라는 컴포넌트를 받아와서 리턴
  }
  
  export default App; // 최종적으로 App 컴포넌트를 내보냄
  ```

  > 하나의 컴포넌트였던 것들 리팩토링을 통해 *<u>반복되는 일정 부분</u>*을 따로 빼서 부모자식화 해준다.
  >
  > ```react
  > // src/App.js
  > import React from "react";
  > 
  > function App() {
  >   return <div>응애</div>;
  > }
  > 
  > export default App;
  > ```

