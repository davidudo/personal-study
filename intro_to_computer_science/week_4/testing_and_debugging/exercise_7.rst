Week 4 (Exercise 7)
===================

Question
--------

Consider the following function definition:

```python
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)
```

When we call `f(3)` we expect the result 6, but we get 0.

When we call `f(1)` we expect the result 1, but we get 0.

When we call `f(0)` we expect the result 1, but we get 0.

Using this information, choose what line of code should be changed from the
following choices:

Answer
------

- [ ] `if n == 0:`

- [X] `return n`

- [ ] `else:`

- [ ] `return n * f(n-1)`

Question
--------

How should this line be rewritten?

Answer
------

```python
return 1
```
