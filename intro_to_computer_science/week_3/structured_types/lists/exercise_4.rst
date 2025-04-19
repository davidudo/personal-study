Week 3 (Exercise 4)
===================

For the last expression in each question below, specify its type and value. If
it generates an error, select type 'NoneType' and put the word 'error' in the
box for the value.

Question 1
----------

```python
>>> aList = [0, 1, 2, 3, 4, 5]
>>> bList = aList
>>> aList[2] = 'hello'
>>> aList == bList
```

Answer
------
Type: boolean
Value: True

Question 2
----------

```python
>>> aList is bList
```

Answer
------
Type: boolean
Value: True

Question 3
----------

```python
>>> aList
```

Answer
------
Type: list
Value: [0, 1, 'hello', 3, 4, 5]

Question 4
----------

```python
>>> bList
```

Answer
------
Type: list
Value: [0, 1, 'hello', 3, 4, 5]

Question 5
----------

```python
>>> cList = [6, 5, 4, 3, 2]
>>> dList = []
>>> for num in cList:
        dList.append(num)
>>> cList == dList
```

Answer
------
Type: boolean
Value: True

Question 6
----------

```python
>>> cList is dList
```

Answer
------
Type: boolean
Value: False

Question 7
----------

```python
>>> cList[2] = 20
>>> cList
```

Answer
------
Type: list
Value: [6, 5, 20, 3, 2]

Question 8
----------

```python
>>> cList[2] = 20
>>> cList
```

Answer
------
Type: dList
Value: [6, 5, 4, 3, 2]


