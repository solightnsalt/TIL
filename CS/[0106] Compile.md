# Compile

![compile](https://scaler.com/topics/images/mac-c-compiler.webp)

+ 고급 프로그래밍 언어로 쓰인 원시 프로그램을 당초 의미와 동등한 컴퓨터로 실행 가능한 파일로 변환 시키는 프로세스

+ 즉, 고급 프로그래밍 언어로 작성한 원시 코드(Source Code)를 컴퓨터 내부에서 사용 가능한 언어인, 기계어 (Machine Language)로 번역하고 이를 실행 가능하게 만들어 주는 과정

  + Compiler = 이 과정을 해주는 프로그램(소프트웨어)
  + "조립(assembling)"또는 "빌드(build)"라고도 한다.

  > why? 
  >
  > 프로그래밍 언어들은 사람이 알아볼 수 있는 인간친화적 언어
  >
  > 컴퓨터는 0과 1로 이루어진 기계어 신호만 알아듣기 때문에 이해할 수 없다. 

![img](https://miro.medium.com/max/640/1*Mc67XYaouCiOfPbL4QR5sQ.webp)

## 정적 컴파일과 동적 컴파일

+ **정적 컴파일러** : 프로그램 실행 시점 전 기계어로 변환하는 컴파일러
  + 장점 : 런타임 성능이 뛰어나다.
  + 단점 : 컴파일 타임에 시간이 너무 오래 소요된다.
  + ex. C, C++
+ **동적 컴파일러** : 프로그램 실행 중 기계어로 변환하는 컴파일러 (= 인터프리트 언어)
  + 장점 : 컴파일 시간이 거의 필요 없이 프로그램 실행을 할 수 있다.
  + 단점 : 실행 중 리소스의 일부를 컴파일에 사용하기 때문에 프로그램 성능이 떨어진다.
  + ex. javascript, python



## JIT(Just In Time) 컴파일러

+ 정적 컴파일과 동적 컴파일의 단점을 최소화하고 장점을 극대화하는 방향으로 설계된 컴파일러



## Compiler의 실행 단계

![process](https://s3.ap-south-1.amazonaws.com/s3.studytonight.com/tutorials/uploads/pictures/1621501647-71449.png)

1. 선행 처리 (Preprocessing)

   + 컴파일 전에 원시 프로그램을 처리하는 컴파일러의 한 부분

   

2. 컴파일 (Compile)

   1. 어휘 분석 : 토큰 분리 등
      + 토큰이라는 의미 있는 문법 단위(식별자, 특수어, 연산자 등)로 분리하는 것

   2. 구문 분석 : 구조화된 구문 트리 생성 등
      + 어휘 단위들을 가져와서, 이들로부터 파스 트리라는 계층적 구조를 생성
   3. 의미 분석 : 타입 검사 (Type Checking)등
      + 구문 분석 시 탐지가 어려운 타입 오류 등을 검사함

   4. 중간 코드 생성 : 원시 프로그램과 기계어 간의 중간 수준의 코드
      + 중간 코드 (Intermediate Code) : 중간 수준의 코드로써, 다른 언어에서 공유 가능
      + ex. Pascal의 P 코드, Java의 바이트 코드 등
   5. 코드 최적화 : 프로그램 크기를 축소하거나, 실행 속도를 높이는 등
      + 기계어 상에서 수행하기 어려워, 중간 코드를 대상으로 이루어짐
   6. 목적 코드 생성 : 중간 코드 버전을 동등한 기계어로 변환시킴
      + 목적 코드 (Object Code) : 기계어로 번역된 파일

   

3. 결합(Assemble)                            

  + 소스 코드의 컴파일 후 기계어 변환

  + 때론, 어셈블러 단계를 거치지 않고, 컴파일러에서 바로 기계어로 변환되기도 함

  + 어셈블러의 출력은 오브젝트 파일(object file)이라고 함

    > 컴파일러에 의해 생성된 기계어 만으로, 직접 실행될 수도 있지만,
    > 통상, 다른 코드들과 함께 연결되어 실행됨

    

4. 링킹(Linking) & 로딩(Loading) : 실행 파일의 생성

      + 주 기억 장치의 할당 (확보)
      + 연결 (Linking)
      + 재배치 (Relocation)
      + 프로그램 연결 적재 (Loading)







> 참고 
>
> https://kotlinworld.com/307#%EC%A-%--%EC%A-%--%--%EC%BB%B-%ED%-C%-C%EC%-D%BC%EA%B-%BC%--%EB%-F%--%EC%A-%--%--%EC%BB%B-%ED%-C%-C%EC%-D%BC%EC%-D%--%--%ED%--%-C%EA%B-%--%EC%A-%--%EA%B-%BC%--%EC%-E%A-%EC%A-%--
>
> https://wikidocs.net/132948
>
> https://velog.io/@bami/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0-%EB%B0%A9%EC%8B%9D%EA%B3%BC-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC-%EB%B0%A9%EC%8B%9D
>
> https://medium.com/@su_bak/%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC%EC%9D%98-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%A2%85%EB%A5%98-e3ff01bd9e1f
>
> http://www.ktword.co.kr/test/view/view.php?m_temp1=1436





