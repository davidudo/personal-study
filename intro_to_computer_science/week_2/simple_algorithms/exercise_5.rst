Week 2 (Exercise 5)
===================

Enter the value of the expressions below.

To get the most out of this problem, try to figure out the answers by reading
the code, not running it. Run the code only after you've used up a few of your
checks.

**Hint:** If you are confused, you may find it helpful to draw out an
environment diagram similar to what was presented in lecture.

Question 1
----------

```python
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)

foo(3)
```

Answer
------
11

Question 2
----------

```python
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)

foo(3, 0)
```

Answer
------
1

Question 3
----------

```python
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
```

Answer
------
5

Question 4
----------

```python
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
```

Answer
------
3
