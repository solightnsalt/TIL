# Props

+ 컴포넌트 끼리의 정보 교환 방식 

  + 여기서 말하는 정보는 ? 

    = 부모 컴포넌트가 자식 컴포넌트에게 물려준 정보

+ ⭐️ 반드시!!! 위에서 아래로 흐른다. (부모 → 자식으로만)

+ ⭐️ 읽기 전용이므로 변경하지 않는다.



**예시**

```react
import React from "react";

// 2. 엄마가 전달한 정보를 어케 받아올까?
// => props라는 이름으로 input을 받아오면 된다.
function Child(props) {
  const onClinkButtonHandler = () => {
    alert(props.grandfaName + "의 딸 " + props.motherName + "입니다");
  };
  return (
    <div>
      <h1>울엄마는 누구일까요?</h1>
      {/* 이곳에 퀴즈를 위한 html 코드를 작성해 주세요 */}
      <button onClick={onClinkButtonHandler}>click</button>
    </div>
  );
}

function Mother(props) {
  const name = "봉미선";
  return <Child motherName={name} grandfaName={props.grandfaName} />; 
  // 1. 자식컴포넌트에 정보를 전달했다!
}

function GrandFa() {
  const name = "봉선달";
  return <Mother grandfaName={name} />;
}
function App() {
  return <GrandFa />;
}

export default App;
```

✔︎ `props` 또한 변수의 이름이기 때문에 변경해도 상관 없지만 일련의 약속이라 저렇게 사용.



## Props drilling

+ 부모의 데이터를 자식의 자식의 자식의 자식의 ・・・ 자식이 받아야 하는 경우처럼 불필요하게 거쳐야 하는 컴포넌트가 많은 패턴을 이르는 말

+ 코드 작성 시 이러한 패턴을 피해야 한다.

  왜? 중간에 오류 발생하거나 하면 팔로업이 어려워서 유지 보수가 어렵다.

  → 이런 상황을 피하기 위해 상태 관리 툴인 'Redux'와 같은 것을 숙지해야 함😉





## Props Children

+ 위의 props와 같은 개념이나 형태가 조금 다름

  ```react
  //예시코드 src/App.js
  
  import React from "react";
  
  function User() {
    return <div></div>;
  }
  
  function App() {
    return <User>안녕하세요</User>;
  }
  export default App;
  ```

  + 위의 코드는 화면에 아무것도 표시되지 않음.
  + 왜? App 컴포넌트에서 보낸 정보를 자식컴포넌트인 user에서 받아오지 않았기 때문.

+ 기존의 props

  + input: `<User greeting="안녕하세요" />` 
  + output: `{props.greeting}`

+ Children props

  + Input: `<User>안녕하세요</User>`
  + Output: `{props.children}`
    + 받는 방식은 props로 동일하나, 이름이 children으로 정해져 있다.
    + 따라서, 위의 예시의 경우 user를 아래와 같이 고쳐야 정보를 받아올 수 있음

  ```react
  function User(props) {
    return <div>{props.children}</div>;
  }
  ```

+ 여는 태그와 닫는 태그 사이에 어떤 값을 넣으면 그 요소를 칠드런으로 하위 컴포넌트에 넘겨줄 수 있다. 라고 생각하기



### children의 용도

+ Layout 컴포넌트를 만들 때 자주 사용된다.

  ```react
  // src/About.js
  
  import React from "react";
  import Layout from "./components/Layout";
  
  function App() {
    return (
  
      <Layout> 
        <div>여긴 App의 컨텐츠가 들어갑니다.</div>
      </Layout>
    );
  }
  export default App;
  ```

  

