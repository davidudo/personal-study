Week 2 (Exercise 6)
===================

As we'll see in subsequent lectures, everything in Python is an object. Objects
are special because we can associate special functions, referred to as object
methods, with the object. In this problem you'll be working with string
objects, and their built-in methods.

A complete description of the methods available to string objects can be found
in the Python library reference on string methods.

In this exercise, we want you to get some experience in using methods as
functions. The convention for object methods is to use the "dot" notation, so
that if s is a string, evaluating s.upper will return the actual function, and
evaluating s.upper() will cause the function itself to be evaluated (in this
case it returns a new string, since strings are immutable) with every character now in upper case. An example of this follows:

```python
>>> s = 'abc'
>>> s.capitalize
<built-in method capitalize of str object at 0x104c35878>
>>> s.capitalize()
'Abc'
```

For each of the expressions in this problem, specify its type and value. If it
generates an error, select type 'NoneType' and put the word 'error' in the box
for the value. If it would be a function, select type 'function' and put the
word 'function' in the box for the value.

Assume we've made the following assignments:

```python
> str1 = 'exterminate!'
> str2 = 'number one - the larch'
```

Assume that the expressions are evaluated in the order shown - that is, each
problem part is evaluated directly after the previous problem part(s).

Question 1
----------

```python
str1.upper
```

Answer
------
Type: function
Value: function

Question 2
----------

```python
str1.upper()
```

Answer
------
Type: string
Value: 'EXTERMINATE!'

Question 3
----------

```python
str1
```

Answer
------
Type: string
Value: 'exterminate!'

Question 4
----------

```python
str1.isupper()
```

Answer
------
Type: boolean
Value: False

Question 5
----------

```python
str1.islower()
```

Answer
------
Type: boolean
Value: True

Question 6
----------

```python
str2 = str2.capitalize()
str2
```

Answer
------
Type: string
Value: 'Number one - the larch'

Question 7
----------

```python
str2.swapcase()
```

Answer
------
Type: string
Value: 'nUMBER ONE - THE LARCH'

Question 8
----------

```python
str1.index('e')
```

Answer
------
Type: int
Value: 0

Question 9
----------

```python
str2.index('n')
```

Answer
------
Type: int
Value: 8

Question 10
-----------

```python
str2.find('n')
```

Answer
------
Type: int
Value: 8

Question 11
-----------

```python
str2.index('!')
```

Answer
------
Type: NoneType
Value: 'error'

Question 12
-----------

```python
str2.find('!')
```

Answer
------
Type: int
Value: -1

Question 13
-----------

```python
str1.count('e')
```

Answer
------
Type: int
Value: 3

Question 14
-----------

```python
str1 = str1.replace('e', '*')
str1
```

Answer
------
Type: string
Value: '*xt*rminat*!'

Question 15
-----------

```python
str2.replace('one', 'seven')
```

Answer
------
Type: string
Value: 'Number seven - the larch'
