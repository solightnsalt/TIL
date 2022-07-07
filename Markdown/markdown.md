# 🎈마크다운

---

<img src="https://nachwon.github.io/img/markdown.png" alt="markdown" style="zoom: 25%;" />








## 마크다운이란? 

- 2004년 존 그루버가 만든 텍스트 기반의 가벼운 마크업 언어
- 문법이 쉽고 간단한 것이 특징 
- HTML 등의 서식 문서로 쉽게 변환되기 때문에 README 파일 등에 많이 사용됨






## 마크다운 문법



### 제목 (Heading)

* 문서의 제목이나 소제목으로 사용 
* #의 개수에 따라 html h1~h6까지 표현 가능
* 문서의 구조를 위해 사용
  * 글자 크기 조절용으로 사용하지 말기 !

> # \#Heading level 1
>
> ## \##Heading level 2
>
> ### \###Heading level 3
>
> #### \####Heading level 4
>
> ##### \#####Heading level 5
>
> ###### \######Heading level 6



### 목록 (List)

* 순서 있는 목록 : 숫자와 마침표를 사용해 표시

> 1. 첫 번째
> 2. 두 번째
>    1. 하위 첫 번째 



* 순서 없는 목록 : 기호(\*, \-, \+)를 사용하여 표시하며, 뷰어마다 보여지는게 다를 수 있음

> + 첫 번째
> + 두 번째
>   + 하위 첫 번째
>     + ?





### 인용문 (Blockquotes)

* 블럭인용문자 \>를 사용

> 1st BQ
>
> > 2nd BQ
> >
> > > 3rt BQ

* 인용문 안에서 다른 마크다운 요소를 포함할 수 있다. 

> #### This is a H4
>
> + List
>
>   ​	`code`





### 이미지

> \!\[문자열]\(이미지 주소)
>
> *예시*
>
> ![쿼카귀여워](markdown.assets/quokkasmile.jpg)





### 표 (Table)

* 본문 - 표 - 표 삽입 또는 Ctrl+T로 생성

| 코코        | 루루        | 루키        |
| ----------- | ----------- | ----------- |
| 돼냥이(5살) | 돼냥이(5살) | 골댕이(1살) |





### 주소 삽입 (Link)

#### URL 직접 입력

* 삽입하고 싶은 링크의 http 또는 https를 포함한 URL을 \< 주소 >에 입력

> *예시  \<http://www.google.co.kr>은 http://www.google.co.kr로 표시*



#### 인라인 주소 삽입

> \[주소에 대한 설명]\(주소)
>
> *예시  \[Google]\(http://www.google.co.kr)은 [Google](http://www.google.co.kr)로 표시*



#### 링크에 설명(title) 추가

> \[주소명or원하는 텍스트]\(주소 \"주소에 대한 설명")
>
> *예시 [Multicampus](https://www.multicampus.com/main "앞서가는 개발자 커리어의 시작")



#### 참조 링크 삽입

* 같은 링크 URL을 여러 번 입력해야 하거나 글 안의 링크를 따로 관리하고 싶을 때 편리
* 참조할 링크에도 \""기호로 설명 추가 가능 
  * git hub에는 적용되지 않는다고 함


> - 링크 삽입 시 문법 : \[주소명]\[참조 번호]
> - 참조 번호 작성 문법: \[참조 번호]: 주소
>
> *예시*
>
> *\<글 중간>*
>
> *이 부분은 [MD Link][1] 참조*
>
> *<몇 줄 뒤>*
>
> *이 부분도 [MD Link][1], 저 부분은 [Markdown: Syntax][2]를 참조*
>
> *\<글 마지막 or 적고 싶은 위치>*
>
> [1]:  https://opentutorials.org/module/782/6083
>[2]: https://daringfireball.net/projects/markdown/syntax	"영어주의"



#### 이미지에 링크 삽입

> \[!\[이미지설명](이미지 소스 url)]\(링크url)
>
> *예시* 
>
> [<img src="https://ifh.cc/g/ZLHDgV" alt="왕크왕귀" style="zoom:50%;" />](https://www.instagram.com/parkseoham/)





### 코드 블록(Code Block)

#### Fenced Code Block 

* Backtick 기호\(\`) 3 개를 활용하여 작성
* 특정 언어를 명시하면 Syntax Highlighting  적용 가능

> *예시*
>
> ``` js
> function getDevJob(studying, hardWork, luck) {
>     var isPrepared = studying && hardWork && luck;
>     if ( isPrepared ) {
>         return true;
>     } else {
>         return false;
>     }
> }
> ```



#### Inline Code Block

* Backtick 기호\(\`) 1 개를 인라인에 활용하여 작성

> *예시* 
>
> At the command prompt, type `nano`





### 텍스트 강조

* \*기울임* or \_기울임_ > *기울임*

* \**굵게** or \__굵게__ > **굵게**
* \~~취소선~~ > ~~취소선~~

* 동시에 사용 가능 

> *예시* \~\~\*\*\*띠로리\*\*\*~~ > ~~***띠로리***~~





### 수평선 

* 3개 이상의 asterisks (\***), dashed\(-\-\-), underscore \(\_\_\_)로 생성 가능

***

---

___



