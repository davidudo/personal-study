Week 2 (Exercise 2)
===================

You have the following function definitions:

```python
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

def c(x, y):
   '''
   x: int or float.
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
```

Below is a transcript of a session with the Python shell. Provide the type and
value of the expressions being evaluated. If evaluating an expression would
cause an error, select `NoneType` and write 'error' in the box. If the value of
an expression is a function, select `function` as the type and write 'function'
in the box.

Question 1
----------

```python
a(6)
```

Answer
------
Type: int
Value: 7

Question 2
----------

```python
a(-5.3)
```

Answer
------
Type: float
Value: -4.3

Question 3
----------

```python
a(a(a(6)))
```

Answer
------
Type: int
Value: 9

Question 4
----------

```python
c(a(1), b(1))
```

Answer
------
Type: float
Value: 4.0

Question 5
----------

```python
d('apple', 11.1)
```

Answer
------
Type: NoneType
Value: error

Question 6
----------

```python
e(a(3), b(4), c(3, 4))
```

Answer
------
Type: boolean
Value: False

Question 7
----------

```python
f
```

Answer
------
Type: function
Value: function
