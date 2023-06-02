# API(Application Programming Interface)

![API](https://media.geeksforgeeks.org/wp-content/uploads/20230216170349/What-is-an-API.png)



+ 컴퓨터나 컴퓨터 프로그램 사이의 연결

  (↔  User Interface : 컴퓨터와 최종 사용자(사람)을 연결)

+ 일종의 소프트웨어 인터페이스이며, 다른 종류의 소프트웨어에 서비스를 제공한다. 

+ 나중에 변경되더라도 개발자가 유용하게 사용할 수 있고 일정하게 관리할 수 있는 부분들만 노출 시키고, 시스템이 동작하는 방식과 관련된 내부의 세세한 부분을 숨기기 위해 사용된다.



> FROM AWS
>
> + API는 정의 및 프로토콜 집합을 사용하여 두 소프트웨어 구성 요소가 서로 통신할 수 있게 하는 메커니즘 
>
>   ex) 일일 기상 데이터 in 기상청 소프트웨어 시스템
>
>   ​	↑
>
>   ​	요청 & 응답으로 통신 
>
>   ​	↓
>
>   ​	휴대폰 날씨 앱

## WEB API

+ 웹 어플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세를 일 컫는다.
+ 요즘은 우체국의 우편번호 API, 기상청의 미세먼지, 구글 or 카카오 or 네이버의 지도 API 등의 유용한 오픈 API들이 많기 때문에 홈페이지 구축이나 추가개편 시 따로 개발하지 않고 필요한 오픈 API를 가져와서 사용하는 추세이다. 





### Fetch

+ `fetch`기본 골격👇🏻

  ```javascript
  fetch("URL").then(res => res.json()).then(data => {
  		console.log(data)
  })
  ```

  : URL에서 받은 데이터를 json 형식으로 바꾸고 console에 띄워라