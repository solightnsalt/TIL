### `type()`

+ 데이터 타입을 확인 할 수 있는 함수 



##### 예제 

+ 123의 데이터 타입 = 정수 

```python
type(123)
<class 'int'>
```

+ 변수에 데이터를 담고, 변수 이름으로 데이터 타입 확인 가능 

```python
jb = 123
type(jb)
<class 'int'>
```

+ `print()`함수로 결과 출력 가능

```python
jb = 123
print(type(jb))
<class 'int'>
```

+ 기타 등등,, 

```python
>>> type( 123 )
<class 'int'>

>>> type( 123.123 )
<class 'float'>

>>> type( 'abc' )
<class 'str'>

>>> type( [ 1, 2, 3 ] )
<class 'list'>

>>> type( ( 1, 2, 3 ) )
<class 'tuple'>

>>> type( 1+2j )
<class 'complex'>

>>> type( True )
<class 'bool'>
```