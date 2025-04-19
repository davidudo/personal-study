Week 2 (Exercise 3)
===================

Below is a transcript of a session with the Python shell. Provide the type and
value of the expressions being evaluated. If evaluating an expression would
cause an error, select NoneType and write 'error' in the box. If the result is
a function, select function and write 'function' in the box. As always, try to
do this problem by hand before turning to your interpreter.

Assume the following definitions have been made:

```python
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
```

Question 1
----------

```python
a(False, 2, 3)
```

Answer
------
Type: int
Value: 3

Question 2
----------

```python
b(3, 2)
```

Answer
------
Type: int
Value: 3

Question 3
----------

```python
a(3>2, a, b)
```

Answer
------
Type: function
Value: function

Question 4
----------

```python
b(a, b)
```

Answer
------
Type: NoneType
Value: error

