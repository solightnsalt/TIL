// // 방법 1. DOM 가로질러서 
// // 문서 내 선택자가 open-btn 첫번째 요소를 모두 buttons로 명명
// const buttons = document.querySelectorAll('.open-btn')

// // buttons 각각을 btn라고 명명하고  (callback function)
// buttons.forEach(function(btn){
//   // btn가 클릭되는 이벤트가 발생 했을 때 또다른 콜백함수를 실행
//     btn.addEventListener("click", function (e) {
//       // 클릭한 버튼의 부모요소(제목)의 부모요소(content박스)를 찾아서 content라고 명명
//       const content = e.currentTarget.parentElement.parentElement;
//       // 이벤트가 발생할 때마다 show-text라는 class를 content에 넣거나 빼는 메서드를 실행
//       content.classList.toggle("show-text");
//     });
// });

// 방법2. 요소의 선택자 이용
// 문서 내 .content css선택자가 있는 요소를 모두 contents로 받아와서
const contents = document.querySelectorAll('.content');
//그 리스트 내의 각 요소를 box
contents.forEach(function (box) {
  console.log(box);
  // 각 박스에서 .open-btn css 선택자가 있는 첫 번째 요소를 button이라고 하고
  const button = box.querySelector(".open-btn");
  console.log(button);
  // 버튼이 클릭 됐을 때
  button.addEventListener('click', function(){
    // 클릭한 버튼의 box가 show-text를 가진 box가 아니면 
    contents.forEach(function (openedBox) {
      if(openedBox !== box){
        //show-text를 가진 박스에서 그 클래스를 빼자
        openedBox.classList.remove("show-text");
      }
    });
    // 그리고 box인 <div class="content-title">에 show-text class를 추가하거나 뺀다.
    box.classList.toggle("show-text");
  });
});
