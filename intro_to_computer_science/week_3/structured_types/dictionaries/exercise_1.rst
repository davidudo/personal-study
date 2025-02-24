Week 3 - Dictionaries (Exercise 1)
==================================

Suppose we evaluate the following expressions:

```python
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
```

We are now going to evaluate a set of expressions, resulting in the following
sequence of interactions. Fill in each blank to show what the Python
interpreter would print at that point. If an expression below would generate an
error, enter 'error'.

Question 1
----------

```python
>>> animals
```

Answer
------
{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}

Question 2
----------

```python
>>> animals['c']
```

Answer
------
'coati'

Question 3
----------

```python
>>> animals['donkey']
```

Answer
------
'error'

Question 4
----------

```python
>>> len(animals)
```

Answer
------
4

Question 5
----------

```python
>>> animals['a'] = 'anteater'
>>> animals['a']
```

Answer
------
'anteater'

Question 6
----------

```python
>>> len(animals['a'])
```

Answer
------
8

Question 7
----------

```python
>>> 'baboon' in animals
```

Answer
------
False

Question 8
----------

```python
>>> 'donkey' in animals.values()
```

Answer
------
True

Question 9
----------

```python
>>> 'b' in animals
```

Answer
------
True

Question 10
-----------

```python
>>> animals.keys()
```

Answer
------
dict_keys(['a', 'b', 'c', 'd'])

Question 11
-----------

```python
>>> del animals['b']
>>> len(animals)
```

Answer
------
3

Question 12
-----------

```python
>>> animals.values()
```

Answer
------
dict_values(['anteater', 'coati', 'donkey'])

