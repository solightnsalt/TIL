# [Github] Duplicating a repository
## Mirroring a repository

### 기존에 썼던 방법



#### 1. 깃허브 새로운 저장소 생성

2번 개발자는 새로운 저장소를 생성합니다.



#### 2. 1번 개발자 저장소 clone

2번 개발자는 1번 개발자의 저장소를 clone 합니다

```bash
git clone --mirror {1번 개발자 페어 프로그래밍 저장소 주소}
cd {클론된 1번 개발자의 저장소 폴더}
```



#### 3. 복사한 저장소의 원격 저장소 설정

2번 개발자는 새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정합니다.

```bash
git remote set-url --push origin {2번 개발자의 새롭게 생성한 저장소 주소}
```

#### 4. push

2번 개발자는 프로젝트를 Push 합니다.

```bash
git push --mirror
```





### Github Docs 방법

> [Repositories/Create & manage repositories/Duplicating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository)



위 방법으로 했을 때 아래 오류가 뜨는 경우가 있어서 찾아본 공식 문서

```bash
! [remote rejected] refs/pull/1/head -> refs/pull/1/head (deny updating a hidden ref)
! [remote rejected] refs/pull/1/merge -> refs/pull/1/merge (deny updating a hidden ref)
```



#### 1. `clone --mirror`가 아닌 `clone --bare`로 받아온다.

```bash
git clone --bare {1번 개발자 페어 프로그래밍 저장소 주소}
cd {클론된 1번 개발자의 저장소 폴더}
```



#### 2. 새 저장소로 바로 `push`한다.

```bash
git push --mirror {2번 개발자의 새롭게 생성한 저장소 주소}
```

끝 ! 

