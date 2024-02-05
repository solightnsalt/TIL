# 이벤트에 응답하기

☝🏻 이벤트 핸들러(Event Handler)는 클릭, 마우스 호버, 폼 인풋 포커스 등  사용자 상호작용에 따라 유발되는 특정 이벤트가 발생했을 때 그 처리를 담당하는 함수를 의미하며, 주로 JSX 요소에 **`onClick`**, **`onChange`**, **`onSubmit`** 등과 같은 이벤트 속성을 통해 설정한다.





## **이벤트 핸들러 추가하기**

```jsx
import React from "react";

function App() {
// 1. 먼저 버튼이 클릭되었을 때 실행될 함수를 컴포넌트 내부에 정의한다.
	const handleClick = () => {
		alert("button clicked");
	};

	return (
		<>
			<h1>이벤트 핸들러</h1>
			{/* 2. onClick 이벤트 속성에 연결하여 버튼 클릭 시 실행되도록 한다. */}
			<button onClick={handleClick}>Click</button>
		</>
	);
}

export default App;
```

**이벤트 핸들러 함수의 특징**

- 주로 컴포넌트 내부에서 정의된다.

- `handle`로 시작하고 그 뒤에 이벤트명을 붙인 함수명을 가진다.

  (ex. `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`)



**인라인으로 이밴트 핸들러 정의하기**

```jsx
// 함수 선언
<button onClick={function handleClick() {
  alert("button clicked");
}}>
  
// 화살표 함수
<button onClick={() => {
  alert("button clicked");
}}>
```

- 짧은 함수를 정의할 때 편리하다.



🚨 **괄호 존재 여부의 차이**

React의 JSX에서는 중괄호`{ }` 내부의 JavaScript는 즉시 실행된다.

**A. `<button onClick={handleClick}>`**

**B. `<button onClick={handleClick()}>`**

A의 경우, **`handleClick`** 함수를 호출하는 것이 아니라 참조만 이벤트 핸들러로 전달하고 있다. 이 경우에는 버튼이 클릭될 때 **`handleClick`** 함수가 호출된다. 그러나 B의 경우 **`onClickHandler()`**가 즉시 호출되어, *렌더링될 때마다 클릭이벤트 핸들러가 실행*되므로 주의가 필요하다.

**A. `<button onClick={() => alert("button clicked")}>`**

**B. `<button onClick={alert("button clicked")}>`**

인라인으로 정의된 이벤트 핸들러의 경우에도, B는 랜더링과 동시에 `alert("button clicked")`가 실행된다. 반면에 A는 `()`로 함수에 대한 참조를 생성해서, 클릭 이벤트가 발생했을 때만 코드가 실행된다.





## **이벤트 핸들러 내에서 Prop 읽기**

이벤트 핸들러는 컴포넌트의 내부에서 선언되기에 해당 컴포넌트의 prop에 접근할 수 있다.

```jsx
const Child = (props) => {
	const handleClick = () => {
		alert("엄마 이름은 " + props.name);
	};
	return <button onClick={handleClick}>{props.children}</button>;
};

const Parent = () => {
	return (
		<div>
			<Child name="봉미선">나는 짱구</Child>
		</div>
	);
};
```





## **이벤트 핸들러를 Prop으로 전달하기**

부모 컴포넌트에서 자식 컴포넌트에게 함수를 전달하여 자식의 이벤트 핸들러로 사용할 수 있다. 자식 컴포넌트가 어떤 이벤트가 발생했을 때 부모 컴포넌트에게 알리고, 부모 컴포넌트에서 이에 대한 처리를 할 수 있도록 하는 방법으로 사용된다.

```jsx
// LikeButton.js
import React from "react";

const LikeButton = (props) => {
  return (
    <button onClick={props.onLikeClick}>
      Like
    </button>
  );
};

export default LikeButton;

// Post.js
import React, { useState } from "react";
import LikeButton from "./LikeButton";

const Post = () => {
  const [likes, setLikes] = useState(0);

  const handleLikeClick = () => {
    // 좋아요 클릭 시 상태 업데이트
    setLikes(likes + 1);
  };

  return (
    <div>
      <p>Post Content</p>
      <p>Likes: {likes}</p>
      {/* 부모 컴포넌트에서 자식의 이벤트 핸들러를 전달 */}
      <LikeButton onLikeClick={handleLikeClick} />
    </div>
  );
};

export default Post;

// 좋아요 버튼을 클릭하면 handleLikeClick 함수가 실행되어 
// Post 컴포넌트의 likes 상태가 업데이트되고, 화면에 좋아요 개수가 갱신!
```

또는, 어떤 컴포넌트를 사용하는 위치에 따라 다른 기능을 수행하도록 만들고자 할 때도 사용된다.

아래 `Button`컴포넌트에서는 부모 컴포넌트에서 전달하는 **`action`** prop을 통해 어떤 동작을 할지 결정할 수 있다.

```jsx
// LikeRetweetButton.js
import React from "react";

const LikeRetweetButton = (props) => {
  const handleClick = () => {
    // 부모 컴포넌트에서 전달한 handleClick 함수 호출
    props.onClick();
  };

  return (
    <button onClick={handleClick}>
      {props.action === 'like' ? ' Like' : ' Retweet'}
    </button>
  );
};

export default LikeRetweetButton;

// 부모 컴포넌트에서 LikeRetweetButton 사용 예시
import React from "react";
import LikeRetweetButton from "./LikeRetweetButton";

const ParentComponent = () => {
  const handleLikeClick = () => {
    alert("Liked!");
    // 좋아요 동작 수행 로직 추가
  };

  const handleRetweetClick = () => {
    alert("Retweeted!");
    // 리트윗 동작 수행 로직 추가
  };

  return (
    <div>
      {/* 좋아요 버튼 */}
      <LikeRetweetButton action="like" onClick={handleLikeClick} />

      {/* 리트윗 버튼 */}
      <LikeRetweetButton action="retweet" onClick={handleRetweetClick} />
    </div>
  );
};

export default ParentComponent;
```

[디자인 시스템](https://uxdesign.cc/everything-you-need-to-know-about-design-systems-54b109851969)을 적용할 때, 버튼처럼 재사용이 많은 컴포넌트에는 스타일과 레이아웃이 지정되고, 특정 동작과 관련된 로직은 부모 컴포넌트에서 처리하는 경우가 일반적이나, 프로젝트의 특정 상황과 요구사항에 따라 동작을 지정할 수도 있다.





## **이벤트 핸들러 Prop 명명하기**

**빌트인 컴포넌트 (예: `<button>`, `<div>`)**

- 웹 브라우저에서 기본적으로 제공되는 HTML 요소

- 브라우저 이벤트 이름을 지원한다.

  > **브라우저 이벤트 예시**
  >
  > 1. 폼 관련 이벤트:
  >    - **`onSubmit`**: 폼 제출 시 발생
  >    - **`onChange`**: 폼 요소의 값이 변경될 때 발생 (input, select, textarea 등)
  >    - **`onClick`**: 요소를 클릭할 때 발생
  > 2. 키보드 이벤트:
  >    - **`onKeyDown`**: 키를 누를 때 발생
  >    - **`onKeyPress`**: 키를 누르고 문자가 입력될 때 발생
  >    - **`onKeyUp`**: 키를 눌렀다가 뗄 때 발생
  > 3. 마우스 이벤트:
  >    - **`onClick`**: 요소를 클릭할 때 발생
  >    - **`onDoubleClick`**: 요소를 더블 클릭할 때 발생
  >    - **`onMouseDown`**: 마우스 버튼을 누를 때 발생
  >    - **`onMouseUp`**: 마우스 버튼을 눌렀다가 뗄 때 발생
  >    - **`onMouseMove`**: 마우스를 움직일 때 발생
  >    - **`onMouseOver`**: 요소 위로 마우스가 올라갈 때 발생
  >    - **`onMouseOut`**: 요소에서 마우스가 벗어날 때 발생
  > 4. 포커스 이벤트:
  >    - **`onFocus`**: 요소에 포커스가 맞춰질 때 발생
  >    - **`onBlur`**: 요소에서 포커스가 빠져나갈 때 발생
  > 5. 그 외 이벤트:
  >    - **`onLoad`**: 리소스(이미지, 스크립트 등)가 로드될 때 발생
  >    - **`onUnload`**: 페이지를 나갈 때(새로고침, 다른 페이지로 이동 등) 발생
  >    - **`onResize`**: 창의 크기가 조절될 때 발생

  

**사용자 정의 컴포넌트**

- 사용자가 직접 만든 컴포넌트들은 브라우저 이벤트 이름과 상관없이 이벤트 핸들러 prop의 이름을 마음대로 지을 수 있다.
- 관습적으로, 이벤트 핸들러 prop의 이름은 **`on`**으로 시작하고 그 뒤에 이어지는 단어는 대문자로 시작한다.

```jsx
import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart, faRetweet } from "@fortawesome/free-solid-svg-icons";

// 버튼 컴포넌트
// 클릭 이벤트가 발생하면 onAction prop으로 전달된 함수를 호출
function TwitterButton({ onAction, count, children, icon }) {
  return (
    <button onClick={onAction}>
      <FontAwesomeIcon icon={icon} />
      {children} {count}
    </button>
  );
}

// 앱 컴포넌트
// handleLikeClick 함수와 handleRetweetClick 함수를 각각 onAction prop으로 전달
export default function App() {
  const [likeCount, setLikeCount] = useState(0);
  const [retweetCount, setRetweetCount] = useState(0);

  const handleLikeClick = () => {
    setLikeCount(likeCount + 1);
  };

  const handleRetweetClick = () => {
    setRetweetCount(retweetCount + 1);
  };

  return (
    <div>
      {/* 좋아요 버튼 */}
      <TwitterButton onAction={handleLikeClick} count={likeCount} icon={faHeart}>
        Like
      </TwitterButton>

      {/* 리트윗 버튼 */}
      <TwitterButton onAction={handleRetweetClick} count={retweetCount} icon={faRetweet}>
        Retweet
      </TwitterButton>
    </div>
  );
}
```

<aside> 🤙🏻 **적절한 HTML 태그를 사용하기**

클릭을 핸들링하려면 **`<div>`** 대신 **`<button>`**을 사용하는 것이 좋다. **`<button>`**은 브라우저에서 기본적으로 키보드 내비게이션 및 다른 빌트인 브라우저 동작을 활성화하며, 이는 웹 접근성과 일반 사용자 경험을 향상시키기 때문!

기본적인 브라우저 스타일링이 싫다면, CSS를 사용하여 스타일을 수정할 수 있다.





## **이벤트 전파**

이벤트의 "버블링(bubbling)"은 HTML 문서의 요소 트리를 따라 이벤트가 전파되는 현상으로, 이벤트가 발생한 요소에서 시작하여 부모 요소를 거슬러 올라가는 과정을 말한다. 따라서 부모 요소에서도 해당 이벤트에 대한 핸들러가 등록되어 있다면 실행된다.

```jsx
export default function Toolbar() {
  return (
    <div className="Toolbar" onClick={() => {
      alert('You clicked on the toolbar!');
    }}>
      <button onClick={() => alert('Playing!')}>
        Play Movie
      </button>
      <button onClick={() => alert('Uploading!')}>
        Upload Image
      </button>
    </div>
  );
}

// 부모 요소인 툴바 영역에도 onClick 이벤트 핸들러가 등록되어 있기 때문에 실행됨
```

 🧐 **`onScroll` 이벤트는 왜 일반적인 이벤트 버블링 형태로 전파되지 않을까?**

**`onScroll`** 이벤트는 스크롤이 발생할 때마다 매우 빈번하게 발생하는 이벤트.

특히 사용자가 페이지를 스크롤할 때, 스크롤 이벤트가 계속해서 발생하는데 이 때문에 모든 스크롤 이벤트가 상위 요소로 계속해서 전파된다면 성능 문제가 발생할 수 있기 때문에 웹 브라우저에서는 **`onScroll`** 이벤트를 일반적인 이벤트 버블링과는 다르게 **`onScroll`** 이벤트가 부여된 요소 내에서만 실행하며, 부모 요소로 이벤트가 전파시키지 않는다.





## **전파 멈추기**

React에서 모달 내에서 이벤트의 전파를 멈추려면, **`event.stopPropagation()`** 메서드를 사용한다. 이 메서드를 호출하면 이벤트가 현재의 단계에서 더 이상 전파되지 않는다.