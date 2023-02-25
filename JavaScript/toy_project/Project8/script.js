const drinks = [
  {
    id: 1,
    title: "카페 아메리카노",
    eng_title: "Caffe Americano",
    category: "espresso",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[94]_20210430103337006.jpg",
    desc: `진한 에스프레소와 뜨거운 물을 섞어 스타벅스의 깔끔하고 강렬한 에스프레소를 가장 부드럽게 잘 느낄 수 있는 커피`,
  },
  {
    id: 2,
    title: "카페 라떼",
    eng_title: "Caffe Latte",
    category: "espresso",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[41]_20210415133833725.jpg",
    desc: `풍부하고 진한 에스프레소가 신선한 스팀 밀크를 만나 부드러워진 커피 위에 우유 거품을 살짝 얹은 대표적인 커피 라떼`,
  },
  {
    id: 3,
    title: "아이스 돌체 라떼",
    eng_title: "Iced Starbucks Dolce Latte",
    category: "espresso",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[128695]_20210426092031969.jpg",
    desc: `스타벅스의 다른 커피 음료보다 더욱 깊은 커피의 맛과 향에 깔끔한 무지방 우유와 부드러운 돌체 시럽이 들어간 음료로 달콤하고 진한 커피 라떼`,
  },
  {
    id: 4,
    title: "바닐라 크림 콜드 브루",
    eng_title: "Vanilla Cream Cold Brew",
    category: "coldbrew",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000000487]_20210430112319040.jpg",
    desc: `콜드 브루에 더해진 바닐라 크림으로 깔끔하면서 달콤한 콜드 브루를 새롭게 즐길 수 있는 음료입니다.`,
  },
  {
    id: 5,
    title: "카라멜 프라푸치노",
    eng_title: "Caramel Frappuccino",
    category: "frappuccino",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[168010]_20210415154711116.jpg",
    desc: `카라멜과 커피가 어우러진 프라푸치노`,
  },
  {
    id: 6,
    title: "자바 칩 프라푸치노",
    eng_title: "Java Chip Frappuccino",
    category: "frappuccino",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[168016]_20210415154152122.jpg",
    desc: `커피, 모카 소스, 진한 초콜릿 칩이 입안 가득 느껴지는 스타벅스에서만 맛볼 수 있는 프라푸치노`,
  },
  {
    id: 7,
    title: "차이 티 라떼",
    eng_title: "Chai Tea Latte",
    category: "tea",
    img: "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[135608]_20210415154244810.jpg",
    desc: `스파이시한 향과 독특한 계피향, 달콤한 차이로 만든 부드러운 티 라떼`,
  },
];
// 먼저 페이지 로딩 될 때 아이템 나열
// 음료 나열할 섹션 지정
const drinksSection = document.querySelector(".drinks");
// 필터 영역
const filterSection = document.querySelectorAll(".filter-btn");

// 문서 로딩될 때 다음 동작 실행 
window.addEventListener("DOMContentLoaded", function () {
  displayDrinks(drinks);
});
// 위에서 실행할 동작 정의 
function displayDrinks(drinkItems){
  // 맨 위 리스트랑 맵핑시켜서 return 안 html 나열
  let displayDrink = drinkItems.map(function (drink) {
    return `<div class="drink">
    <img src=${drink.img} alt="drink img">
    <div class="drink-detail">
    <h4 class="title">${drink.title}</h4>
    <h6 class="eng_title">${drink.eng_title}</h6>
    <p class="desc">${drink.desc}</p>
    </div>
    </div>`;
  });
  displayDrink = displayDrink.join("");
  drinksSection.innerHTML = displayDrink;
}

// 필터 
filterSection.forEach(function(btn){
  btn.addEventListener('click', function(e){
    //dataset을 쓰기 위해 html button에 'data-'추가
    // console.log(e.currentTarget.dataset.id);
    const category = e.currentTarget.dataset.id;
    const drinkCategory = drinks.filter(function(drinkItem) {
      // console.log(drinkItem.category); 여기서 조건을 안 걸면 모든 카테고리 다 나옴
      if(drinkItem.category === category) {
        return drinkItem 
      }
    });
    // console.log(drinkCategory);
    if(category === 'all'){
      displayDrinks(drinks)
    }
    else{
      displayDrinks(drinkCategory)
    }
  });
});