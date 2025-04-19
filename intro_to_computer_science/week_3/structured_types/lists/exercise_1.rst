Week 3 (Exercise 1)
===================

For each of the expressions below, specify its type and value. If it generates
an error, select type 'NoneType' and put the word 'error' in the box for the
value.

Assume we've made the following assignment:

```python
x = (1, 2, (3, 'John', 4), 'Hi')
```

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
Type: tuple
Value: (3, 'John', 4)

Question 3
----------

```python
x[-1]
```

Answer
------
Type: string
Value: Hi

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
x[2][-1]
```

Answer
------
Type: int
Value: 4

Question 6
----------

```python
x[-1][-1]
```

Answer
------
Type: string
Value: i

Question 7
----------

```python
x[-1][2]
```

Answer
------
Type: NoneType
Value: error

Question 8
----------

```python
x[0:1]
```

Answer
------
Type: tuple
Value: (1,)

Question 9
----------

```python
x[0:-1]
```

Answer
------
Type: tuple
Value: (1, 2, (3, 'John', 4))

Question 10
-----------

```python
len(x)
```

Answer
------
Type: int
Value: 4

Question 11
-----------

```python
2 in x
```

Answer
------
Type: boolean
Value: True

Question 12
-----------

```python
3 in x
```

Answer
------
Type: boolean
Value: False

Question 13
-----------

```python
x[0] = 8
```

Answer
------
Type: NoneType
Value: error


