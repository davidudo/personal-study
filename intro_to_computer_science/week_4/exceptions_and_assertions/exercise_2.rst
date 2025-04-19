Week 4 (Exercise 2)
===================

Below are some short Python programs. For each program, answer the associated
question.

Try to answer the questions without running the code. Check your answers, then
run the code for the ones you get wrong.

These questions will ask you to write what the code prints out. If an exception
is raised that is not handled by the code write "error" (no quotes), in
addition to any other text that is output.

The function in the following questions takes a list of integers `numbers` and a
position `index`, and divides each entry in the list of numbers by the value at
entry `index`.

Write what it prints out, separating what appears on a new line by a comma and
a space.

Program A
----------

```python
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
```

Question 1
----------

What does `fancy_divide([0, 2, 4], 1)` print out?

Answer
------
1
0

Question 2
----------

What does `fancy_divide([0, 2, 4], 4)` print out?

Answer
------
-1
0

Question 3
----------

What does `fancy_divide([0, 2, 4], 0)` print out?

Answer
------
0
error

Program B
----------

```python
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
```

Question 1
----------

What does `fancy_divide([0, 2, 4], 1)` print out?

Answer
------
1
0

Question 2
----------

What does `fancy_divide([0, 2, 4], 4)` print out?

Answer
------
1
0
0

Question 3
----------

What does `fancy_divide([0, 2, 4], 0)` print out?

Answer
------
-2
0

Program C
----------

```python
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
```

Question 1
----------

What does `fancy_divide([0, 2, 4], 1)` print out?

Answer
------
1
0

Question 2
----------

What does `fancy_divide([0, 2, 4], 4)` print out?

Answer
------
1
0
0

Question 3
----------

What does `fancy_divide([0, 2, 4], 0)` print out?

Answer
------
0
-2

Program D
----------

```python
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
```

Question
--------

Does this code print 0 when you call `fancy_divide([0, 2, 4], 0)`?

Answer
------
No

Program E
----------

```python
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
```

Question
--------

Does this code print 0 when you call `fancy_divide([0, 2, 4], 0)`?

Answer
------
Yes
