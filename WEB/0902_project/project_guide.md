## 목표

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성



## 준비 사항

1. **(필수)** HTML/CSS 환경 구성

2. (필수)

    웹 페이지를 위한 Assets 다운로드

   - `**index.html`에 마크업을 작성하여 주세요.**

   - `reboot.css` 는 브라우저 기본 설정 CSS를 모두 동일하게 설정하기 위해 사용됩니다.

     [reboot.css](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc05621e-8174-4eb4-9c81-7d4429f69286/reboot.css)

   - `style.css` 에 스타일을 작성합니다.

   - `images` 폴더에는 활용할 포스터 이미지가 있습니다.

     [images.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/96632103-3df0-4e9e-b946-6faafabfa298/images.zip)

## 요구 사항

> HTML/CSS을 활용하여 목표로 하는 웹사이트의 레이아웃을 구성합니다. 아래의 필수 사항을 제외한 요소는 자유롭게 꾸며 주세요.

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/75c9b7b2-a012-4c52-9df1-71153248d3f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220902T051940Z&X-Amz-Expires=86400&X-Amz-Signature=936a2507bf5cc30f29656b8a2febb1a4c1b9f2a1f46ee3dc72d7db4d8396a0bd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### **HTML 기초**

- `DOCTYPE`은 html입니다.
- `html`의 언어는 한국어(ko)입니다.
- `meta` 태그에 인코딩 설정을 UTF-8로 설정 해주세요.
- `meta` 태그에 기본 viewport 설정을 해주세요. (width: device-width, initial-scale: 1.0)
- `title` 태그는 영화추천사이트 라고 설정 해주세요.

### `**header`**

웹 사이트의 헤더 부분에는 로고 이미지와 네비게이션 바를 구성합니다.

- 속성

  - 헤더는 항상 상단에 유지 됩니다. **(sticky)**
  - 높이는 80px이며, 좌우 안쪽 여백(padding)은 40px입니다.

- 이미지 배치

  - 로고 이미지는 좌측에 배치합니다.
  - 로고 이미지의 높이는 60px입니다.
  - 로고 이미지는 `images/logo.png` 입니다.

- 네비게이션 바 (

  ```
  nav
  ```

  )

  - 네비게이션 바의 항목은 우측에 배치합니다.
  - 총 4개의 항목이 배치되며, 각각 임의의 링크(`#`) 으로 설정합니다.
  - 수직 정렬을 통해 중앙으로 일치시킵니다.

### **title `section`**

서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다.

- 속성
  - 높이는 320px이며, `header` 의 높이만큼 상단 여백을 설정합니다.
  - 수직 정렬을 통해 중앙으로 일치시킵니다.
  - 배경 이미지는 적절하게 삽입하고, 이미지에 맞게 사이즈와 위치를 조절 합니다.
  - `h1` 태그를 활용하여 사이트의 제목을 작성합니다.

<aside> 👉 aside와 movie는 8:2의 비율을 가집니다.
</aside>

### `**aside**`

좌측 레이아웃에 장르 목록을 구성합니다.

- 속성
  - 좌측에 위치하며, 상위 div 요소(`#content`)의 상단에 고정 시킵니다.
  - 상하좌우 안쪽 여백(padding)은 1rem입니다.
  - `h2` 태그를 활용하여 `장르 목록` 이라고 작성합니다.
  - 개별 장르는 `ul` 태그를 활용 하되 기본 안쪽 여백을 제거합니다.

### **movie `section`**

우측 레이아웃에 제공된 영화 포스터를 활용하여 실시간 영화 순위 목록을 구성합니다.

<aside> 👉 먼저 3개를 한 줄로 배치하는 것만 진행하고, 추후에 6개로 늘려보세요.

</aside>

- 속성
  - 우측에 위치하며, `aside` 를 제외한 모든 너비를 가집니다.
  - 상하좌우 안쪽 여백(padding)은 24px입니다.
  - 적절한 배경 색상을 적용 시킵니다.
  - `h2` 태그를 활용하여 `실시간 영화 순위` 라고 작성하며, 가운데 정렬을 합니다.
  - 영화는 한 행에 3개씩 배치하며, 각각 너비는 동일합니다.
  - 영화 이미지는 너비를 300px로 설정합니다.
  - 이미지 하단에는 영화명을 작성합니다.

### `**footer`**

연도와 이름이 작성된 푸터를 구성합니다.

- 속성
  - 푸터는 항상 하단에 유지 됩니다.
  - 높이는 40px이며, 모든 내용은 수직/수평 가운데 정렬을 합니다.
  - 적절한 배경 색상을 적용 시킵니다.