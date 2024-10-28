Week 2 (Exercise 1)
===================

Below are some short Python programs. For each program, answer the associated
questions.

Question 1
----------

```python
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```

a. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 0?

   Answer
   ------
   12

b. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 1?

   Answer
   ------
   24

c. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 2?

   Answer
   ------
   36

d. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 3?

   Answer
   ------
   48

5. What is the value of the variable count that is printed out (at the print
   statement) on iteration 4?

   Answer
   ------
   60

Question 2
----------

```python
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```

a. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 0?

   Answer
   ------
   12

b. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 1?

   Answer
   ------
   12

c. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 2?

   Answer
   ------
   12

d. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 3?

   Answer
   ------
   12

e. What is the value of the variable `count` that is printed out (at the print
   statement) on iteration 4?

   Answer
   ------
   12

Question 3
----------

```python
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```

1. How many times will the print statement be executed?

   Answer
   ------
   5

2. What is the largest value of the variable `iteration` that will be printed
   out (at the print statement)?

   Answer
   ------
   4

3. What is the largest value of the variable `count` that will be printed out
   (at the print statement)?

   Answer
   ------
   12

4. What is the smallest value of the variable `count` that will be printed out
   (at the print statement)?

   Answer
   ------
   1
