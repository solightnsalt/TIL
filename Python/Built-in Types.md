# Built-in Types

## Truth Value Testing

1. ###### `and`, `or`, `not`

   + `x or y`
   + `x and y`
   + `not x`

2. 비교

   + `<`
   + `<=`
   + `>`
   + `>=`
   + `==`
   + `!=`
   + `is`
   + `is not`

3. Numeric Types — `int`, `float`, `complex`

| Operation         | Result                                                       | Notes  | Full documentation                                           |
| :---------------- | :----------------------------------------------------------- | :----- | :----------------------------------------------------------- |
| `x + y`           | sum of *x* and *y*                                           |        |                                                              |
| `x - y`           | difference of *x* and *y*                                    |        |                                                              |
| `x * y`           | product of *x* and *y*                                       |        |                                                              |
| `x / y`           | quotient of *x* and *y*                                      |        |                                                              |
| `x // y`          | floored quotient of *x* and *y*                              | (1)    |                                                              |
| `x % y`           | remainder of `x / y`                                         | (2)    |                                                              |
| `-x`              | *x* negated                                                  |        |                                                              |
| `+x`              | *x* unchanged                                                |        |                                                              |
| `abs(x)`          | absolute value or magnitude of *x*                           |        | [`abs()`](https://docs.python.org/3/library/functions.html#abs) |
| `int(x)`          | *x* converted to integer                                     | (3)(6) | [`int()`](https://docs.python.org/3/library/functions.html#int) |
| `float(x)`        | *x* converted to floating point                              | (4)(6) | [`float()`](https://docs.python.org/3/library/functions.html#float) |
| `complex(re, im)` | a complex number with real part *re*, imaginary part *im*. *im* defaults to zero. | (6)    | [`complex()`](https://docs.python.org/3/library/functions.html#complex) |
| `c.conjugate()`   | conjugate of the complex number *c*                          |        |                                                              |
| `divmod(x, y)`    | the pair `(x // y, x % y)`                                   | (2)    | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) |
| `pow(x, y)`       | *x* to the power *y*                                         | (5)    | [`pow()`](https://docs.python.org/3/library/functions.html#pow) |
| `x ** y`          | *x* to the power *y*                                         | (5)    |                                                              |

4. 