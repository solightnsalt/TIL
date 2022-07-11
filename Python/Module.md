### 모듈(Module)



##### 모듈 가져오고 사용하기
+ **import**로 모듈을 가져온다. 예를 들어 random 모듈 전체를 가져오고 싶다면

```
import random
```

+ 모듈에 포함된 함수 등 목록을 보고 싶다면 dir() 함수를 이용합니다.

```
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

+ 2의 3제곱을 구하고 싶다면 모듈.변수()

```
math.pow(2,3)
8.0
```

##### 모듈 중 일부 함수만 가져오기

+ 예를 들어 math 모듈의 pow 함수''만'' 가져오고 싶다면

```
from math import pow
```

+ 사용할 땐 모듈 이름 없이 함수 이름만 쓴다.

```
pow(2,3)
8.0
```

+ 여러 개를 가져오고 싶다면 쉼표로 구분

```
from math import pow, sqrt, trunc
```

모두 가져오고 싶다면 별표(*) 사용.

```
from math import *
```

##### 모듈 이름을 다르게 가져오기

예를 들어 math 대신 ma를 사용하고 싶다면

```
>>> import math as ma
>>> ma.pow(2,3)
8.0
```

##### 불러온 모델 지우기 

+ `del 모듈`

