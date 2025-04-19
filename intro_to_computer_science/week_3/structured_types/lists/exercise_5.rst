Week 3 (Exercise 5)
===================

Here is a different piece of code for working with lists:

```python
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
```

Suppose that you are given the following functions:

```python
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
```

For each of the following questions, indicate what value is returned. If you
believe that an error will occur, write the word 'error'.

Question 1
----------

```python
applyEachTo([inc, square, halve, abs], -3)
```

Answer
------
[-2, 9, -1.5, 3]

Question 2
----------

```python
applyEachTo([inc, square, halve, abs], 3.0)
```

Answer
------
[4.0, 9.0, 1.5, 3.0]


Question 3
----------

```python
applyEachTo([inc, max, int], -3)
```

Answer
------
error


