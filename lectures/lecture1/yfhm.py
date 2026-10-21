import numpy as np

def argmax(values):
    """
    returns the index of the maximum value in a sequence of numbers.

        Parameters:
        values (list): A list of numbers.

        Returns:
        int: 'The index of the maximum value in the list.'
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