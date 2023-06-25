# JSX

+ JavaScript 파일 내에서 HTML과 유사한 마크업(xml)을 작성할 수 있는 확장된 문법
+ 컴포넌트를 작성할 수 있는 다른 방법이 있지만 JSX의 간결성 때문에 대부분의 React사용자가 사용



## 특징

+ 표현식을 포함할 수 있다.

  ```react
  function formatName(user) {
    return user.firstName + ' ' + user.lastName;
  }
  
  const user = {
    firstName: 'Harper',
    lastName: 'Perez'
  };
  
  const element = (
    <h1>
      Hello, {formatName(user)}!
    </h1>
  );
  ```

+ JSX 자체도 표현식으로 사용할 수 있다.

  ⇨ 즉, JSX를 `if` 구문 및 `for` loop 안에 사용하고, 변수에 할당하고, 인자로서 받아들이고, 함수로부터 반환할 수 있다.

+ 어트리뷰트에 따옴표를 이용해 문자열 리터럴을 정의할 수 있다.

+ 중괄호를 사용하여 어트리뷰트에 JavaScript 표현식을 삽입할 수도 있다.

  `const element = <img src={user.avatarUrl}></img>;`

+ 태그가 비어있다면 XML처럼 `/>` 로 꼭! 닫아줘야 한다.

+ 자식을 포함할 수 있지만 최상위 태그는 무조건 하나

  ```react
  const element = (
    <div>
      <h1>Hello!</h1>
      <h2>Good to see you here.</h2>
    </div>
  );
  ```

  

+ SX는 HTML보다는 JavaScript에 가깝기 때문에, React DOM은 HTML 어트리뷰트 이름 대신 `camelCase` 프로퍼티 명명 규칙을 사용

  + `class`는 [`className`](https://developer.mozilla.org/ko/docs/Web/API/Element/className)
  +  tabindex는 [`tabIndex`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/tabIndex)

  

+ 객체를 표현한다. 

  ```react
  {/* 방법1 */}
  function App() {
      const pTagStyle = {
          color : "blue",
      }
  }
  return (
  	<p style={pTageStyle}>hello</p>
  )
  
  {/* 방법2 */}
  function App() {
      const pTagStyle = {
          color : "blue",
      }
  }
  return (
  	<p style={pTageStyle}>hello</p>
  )
  ```

  

+ 주입 공격을 방지하여 사용자 입력을 삽입하는 것이 안전하다.

  + React DOM은 JSX에 삽입된 모든 값을 렌더링하기 전에 이스케이프 하므로, 애플리케이션에서 명시적으로 작성되지 않은 내용은 주입되지 않는다.
  + 모든 항목은 렌더링 되기 전에 문자열로 변환되기 때문에 XSS(cross-site-scripting) 공격을 방지할 수 있다.

