Week 2 (Exercise 4)
===================

Below is a transcript of a session with the Python shell. Provide the type and
value of the expressions being evaluated. If evaluating an expression would
cause an error, select NoneType and write 'error' in the box. If the result is
a function, select function and write 'function' in the box.

To get the most out of this problem, try to figure out the answers by reading
the code, not running it. Run the code in your interpreter only after you've
checked your answers a few times.

**Hint:** If you are confused, you may find it helpful to draw out an
environment diagram similar to what was presented in lecture.

Question 1
----------

```python
>>> a = 10
>>> def f(x):
      return x + a
>>> a = 3
>>> f(1)
```

Answer
------
Type: int
Value: 4

Question 2
----------

```python
>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
```

Answer
------
Type: int
Value: 19
