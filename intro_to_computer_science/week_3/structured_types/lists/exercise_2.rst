Week 3 (Exercise 2)
===================

For each of the expressions below, specify its type and value. If it generates
an error, select type 'NoneType' and put the word 'error' in the box for the
value.

Assume we've made the following assignment:

```python
x = [1, 2, [3, 'John', 4], 'Hi']
```

Additionally, assume that the expressions are evaluated in the order shown -
that is, each problem part is evaluated directly after the previous problem
part(s).

Question 1
----------

```python
x[0]
```

Answer
------
Type: int
Value: 1

Question 2
----------

```python
x[2]
```

Answer
------
Type: list
Value: [3, 'John', 4]

Question 3
----------

```python
x[-1]
```

Answer
------
Type: string
Value: 'Hi'

Question 4
----------

```python
x[2][2]
```

Answer
------
Type: int
Value: 4

Question 5
----------

```python
x[0:1]
```

Answer
------
Type: list
Value: [1]

Question 6
----------

```python
2 in x
```

Answer
------
Type: boolean
Value: True

Question 7
----------

```python
3 in x
```

Answer
------
Type: boolean
Value: False

Question 8
----------

```python
x[0] = 8
x
```

Answer
------
Type: list
Value: [8, 2, [3, 'John', 4], 'Hi']
