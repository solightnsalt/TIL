import React from "react";
import Header from "Header";

function Child(props) {
  // <---- 자바스크립트 영역 ---->
  // function onClinkButtonHandler(e) {
  //   alert("good job🎉");
  // }
  // 화살표 함수
  const onClinkButtonHandler = () => {
    alert(props.grandfaName + "의 딸 " + props.motherName + "입니다");
  };

  return (
    /* <---- HTML/JSX 영역  ---->*/
    <Header>
      <div
        style={{
          height: "100vh",
          display: " flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <h1>{props.children} 울엄마는 누구일까요?</h1>
        {/* 이곳에 퀴즈를 위한 html 코드를 작성해 주세요 */}
        <button onClick={onClinkButtonHandler}>click</button>
      </div>
    </Header>
  );
}

function Mother(props) {
  const name = "봉미선";
  return (
    <Child motherName={name} grandfaName={props.grandfaName}>
      안녕하세요.
    </Child>
  ); // 자식컴포넌트에 정보를 전달했다!
}

function GrandFa() {
  const name = "봉선달";
  return <Mother grandfaName={name} />;
}
function App() {
  return <GrandFa />;
}

export default App;
