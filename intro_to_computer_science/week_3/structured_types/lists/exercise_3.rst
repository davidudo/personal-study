Week 3 (Exercise 3)
===================

For each of the expressions below, specify its type and value. If it generates
an error, select type 'NoneType' and put the word 'error' in the box for the value. If it would be a function, select type 'function' and put the word
'function' in the box for the value.

If the method returns None, select type 'NoneType' and put the word 'None' in
the box for the value.

Assume we've made the following assignments:

```python
> listA = [1, 4, 3, 0]
> listB = ['x', 'z', 't', 'q']
```

You may want to refer to the Python Library Reference to learn about list
methods. Assume these calls appear one after another (so if the list is
modified in a question, that modification stays for subsequent questions).

Question 1
----------

```python
listA.sort
```

Answer
------
Type: function
Value: function

Question 2
----------

```python
listA.sort()
```

Answer
------
Type: NoneType
Value: None

Question 3
----------

```python
listA
```

Answer
------
Type: list
Value: [0, 1, 3, 4]

Question 4
----------

```python
listA.insert(0, 100)
```

Answer
------
Type: NoneType
Value: None

Question 5
----------

```python
listA.remove(3)
```

Answer
------
Type: NoneType
Value: None

Question 6
----------

```python
listA.append(7)
```

Answer
------
Type: NoneType
Value: None

Question 7
----------

```python
listA
```

Answer
------
Type: list
Value: [100, 0, 1, 4, 7]

Question 8
----------

```python
listA + listB
```

Answer
------
Type: list
Value: [100, 0, 1, 4, 7, 'x', 'z', 't', 'q']

Question 9
----------

```python
listB.sort()
listB.pop()
```

Answer
------
Type: string
Value: 'z'

Question 10
-----------

```python
listB.count('a')
```

Answer
------
Type: int
Value: 0

Question 11
-----------

```python
listB.remove('a')
```

Answer
------
Type: NoneType
Value: error

Question 12
-----------

```python
listA.extend([4, 1, 6, 3, 4])
```

Answer
------
Type: NoneType
Value: None

Question 13
-----------

```python
listA.count(4)
```

Answer
------
Type: int
Value: 3

Question 14
-----------

```python
listA.index(1)
```

Answer
------
Type: int
Value: 2

Question 15
-----------

```python
listA.pop(4)
```

Answer
------
Type: int
Value: 7

Question 16
-----------

```python
listA.reverse()
```

Answer
------
Type: NoneType
Value: None

Question 17
-----------

```python
listA
```

Answer
------
Type: list
Value: [4, 3, 6, 1, 4, 4, 1, 0, 100]

