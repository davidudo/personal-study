"""
Week 3 - Dictionaries (Exercise - biggest)

Consider the following sequence of expressions:

```python
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```

We want to write some simple procedures that work on dictionaries to return
information.

This time, write a procedure, called `biggest`, which returns the key
corresponding to the entry with the largest number of values associated with
it. If there is more than one such entry, return any one of the matching keys.

Example usage:

```python
>>> biggest(animals)
'd'
```

If there are no values in the dictionary, `biggest` should return `None`.
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = None
    max_value = max(aDict.values())
    for (key, value) in aDict.items():
        if value == max_value:
            biggest = key
    return biggest
