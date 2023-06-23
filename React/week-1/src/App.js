import React from 'react';
function App() {
	// <---- 자바스크립트 영역 ---->
  // function onClinkButtonHandler(e) {
  //   alert("good job🎉");
  // }
  // 화살표 함수
  const onClinkButtonHandler = () => {
    alert("good job🎉");
  }

  return (
  /* <---- HTML/JSX 영역  ---->*/
    <div
      style={{
        height: '100vh',
        display: ' flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <h1>my component</h1>
  {/* 이곳에 퀴즈를 위한 html 코드를 작성해 주세요 */}
      <button onClick={onClinkButtonHandler}>click</button>

    </div>
  );
}

export default App;