"""
Week 3 (Exercise - apply to each 3)

Here is the code for a function `applyToEach`:

```python
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
```

Assume that

```python
testList = [1, -4, 8, -9]
```

For each of the following questions (which you may assume is evaluated
independently of the previous questions, so that `testList` has the value
indicated above), provide an expression using `applyToEach`, so that after
evaluation testList has the indicated value. You may need to write a simple
procedure in each question to help with this process.

Example Question:

```python
>>> print testList
[1, 16, 64, 81]
```
"""

testList = [1, -4, 8, -9]

def square(num):
    return num * num

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

applyToEach(testList, square)
