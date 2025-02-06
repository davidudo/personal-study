Week 2 (Exercise 7)
===================

Question 1
----------
Assume the two files below are in the same folder. You run inventory.py. What
happens?

FILE: batteries.py
```python
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```

FILE: inventory.py
```python
aa = "aa"
tripleA = "aaa"
print(aa)
```

Answer
------
prints `aa`

Question 2
----------
Assume the two files below are in the same folder. You run inventory.py. What
happens?

FILE: batteries.py
```python
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```

FILE: inventory.py
```python
aa = "aa"
tripleA = "aaa"
print(batteries.aa)
```

Answer
------
There is an error.

Question 3
----------
Assume the two files below are in the same folder. You run inventory.py. What
happens?

FILE: batteries.py
```python
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```

FILE: inventory.py
```python
import batteries
aa = "aa"
tripleA = "aaa"
print(batteries.aa)
```

Answer
------

prints `AA`

Question 4
----------

FILE: batteries.py
```python
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```

FILE: inventory.py
```python
from batteries import *
aa = "aa"
print(aa, aaa, c, d)
```

Answer
------
prints `aa AAA C D`
