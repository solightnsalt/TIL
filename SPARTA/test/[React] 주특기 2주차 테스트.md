# [React] 주특기 2주차 테스트

## 시험 문제 내용

<aside style="background-color: #D5CBE7; padding: 10px;">📢 답안 제출 내용<br/>
	어떤 부분이 문제였고 어떻게 해결 했는지에 대해 소스코드를 포함해서 자세한 설명을 적어주세요.
	</aside>

> `yarn start`시 eslint warning 참고

```bash
src\features\todos\components\Form.jsx
  Line 3:10:  'useDispatch' is defined but never used  no-unused-vars
  Line 5:10:  'addTodo' is defined but never used      no-unused-vars
  Line 8:9:   'id' is assigned a value but never used  no-unused-vars

src\pages\Detail.jsx
  Line 1:17:   'useEffect' is defined but never used          no-unused-vars
  Line 5:10:   'getTodoByID' is defined but never used        no-unused-vars
  Line 8:9:    'dispatch' is assigned a value but never used  no-unused-vars
  Line 11:11:  'id' is assigned a value but never used        no-unused-vars
```



### 문제1

#### 추가하기 버튼을 클릭해도 추가한 아이템이 화면에 표시되지 않음



##### 원인

`onSubmitHandler` 함수에서 인풋값을 todo에 추가해줘야 하는데 그 부분은 없고, submit 시 빈 배열로 돌리는 코드만 있어서 발생하는 현상

```js 
const onSubmitHandler = (event) => {
		event.preventDefault();
		if (todo.title.trim() === "" || todo.body.trim() === "") return;

		setTodo({
			id: 0,
			title: "",
			body: "",
			isDone: false,
		});
	};
```



##### 해결방법

```jsx
const onSubmitHandler = (event) => {
    event.preventDefault();
    if (todo.title.trim() === "" || todo.body.trim() === "") return;

    dispatch(addTodo({
      id: id,
      title: todo.title,
      body: todo.body,
      isDone: false,
    }));

    setTodo({
      id: 0,
      title: "",
      body: "",
      isDone: false,
    });
  };
```

1. 훅 `{ useDispatch }`로 `dispatch ` 함수를 가져온 뒤, 
2. `onSubmitHandler` 함수 내에서 상태 변경에 대한 정보를 담고 있는 `addTodo` 액션을 dispatch로 redux에 전달
3. 전달된 `addTodo`실행되고 todo가 추가됨





### 문제 2

#### 추가하기 버튼 클릭 후 기존에 존재하던 아이템들이 사라짐



##### 원인

`redux/modules/todos.js`에 정의된 리듀서 함수의 `ADD_TODO` 액션의 처리하는 부분에서 todo의 상태를 업데이트 할 때, 기존 배열에 새로운 배열을 더하는 것이 아니라 새로운 배열만 넣어서 발생하는 문제.


```js
const todos = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TODO:
      return {
        ...state,
        todos: [action.payload],
      };

```



##### 해결방법

```jsx
const todos = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TODO:
      return {
        ...state,
        todos: [...state.todos, action.payload],
      };
```

새 todo를 받아오는 `action.payload` 앞 부분에 기존의 todo 배열을 받아오는 `...state.todos`를 추가해주면 된다.





### 문제 3

#### 삭제 기능이 동작하지 않음



##### 원인

`redux/modules/todos.js` 안에 *Todo를 지우는 action creator*인 `deleteTodo`는 정의되어 있으나 todos의 상태를 변경하는 리듀서 함수 내부에 `DELETE_TODO` 액션을 처리하는 코드가 없음. 



##### 해결

아래와 같이 리듀서 함수 내부에 `case DELETE_TODO` 일 때 할 일을 삭제하는 코드를 추가

```js
case DELETE_TODO:
      return {
        ...state,
        todos: state.todos.filter((todo) => {
          return todo.id !== action.payload;
        }),
      };
```



### 문제 4

##### 상세 페이지에 진입 하였을 때 데이터가 업데이트 되지 않음



##### 원인

id를 이용해서 해당 to do의 내용을 불러오는 코드 누락



##### 해결

```jsx
useEffect(() => {
    dispatch(getTodoByID(id)); // ID를 이용하여 todo를 가져오는 액션 디스패치
  }, [dispatch, id]);
```

1. `디테일` 컴포넌트가 마운트될 때 `useEffect` 콜백 함수를 실행
2. `getTodoByID` 액션을 디스패치하여 해당 ID에 해당하는 `todo`를 가져온다.





### 문제 5

#### 완료된 카드의 상세 페이지에 진입 하였을 때 올바른 데이터를 불러오지 못함



##### 원인

`List.jsx`에서 완료된 카드의 Link 경로가 잘못 들어가 있었음

```jsx
<StLink to={`/${index}`} key={todo.id}>
	<div>상세보기</div>
 </StLink>
```



##### 해결 

working과 같이 ``/${todo.id}`` 경로를 todo의 id로 바꿔주면 된다.





### 문제 6

#### 취소 버튼 클릭 시 기능이 작동하지 않음



##### 원인

```js
const onToggleStatusTodo = (id) => {
		dispatch(toggleStatusTodo(id));
	};
```

`onToggleStatusTodo`함수는 todo.id를 인자로 받아 처리하는 함수이다.

그러나 아래 코드에선 함수에 인자를 전달하지 않고 있다.

```jsx
<StButton borderColor="green" onClick={onToggleStatusTodo}>
										{todo.isDone ? "취소!" : "완료!"}
									</StButton>
```



##### 해결

아래와 같이 `onClick` 이벤트 핸들러에 `onToggleStatusTodo`함수를 호출하고 `todo.id`를 인자로 넣어주면 정상적으로 동작한다. 

```jsx
<StButton borderColor="green" onClick={() => onToggleStatusTodo(todo.id)}>
  {todo.isDone ? "취소!" : "완료!"}
</StButton>
```

