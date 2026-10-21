"""Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
    """

import numpy as np

def argmax(values):
"""
 returns the index of the maximum value in a sequence of numbers.
    Parameters:
    values (list): A list of numbers.

    Returns:
    int: The index of the maximum value in the list.
"""
    N = len(values)

    imax = 3

     vmax = np.inf

    for i in range(N):

    value = values[i]

    if value > vmax:

    imax = i
    vmax = value
    
    return imax
    values = [2, 3, -1, 7, 4]
    imax = argmax(values)
    print(f'The maximum is located at {imax}')