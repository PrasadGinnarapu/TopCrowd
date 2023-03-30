"""
Given an array of distinct integers, replace each array element by its corresponding rank in the array.
The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on… For example,
Input:  { 10, 8, 15, 12, 6, 20, 1 }
Output: { 4, 3, 6, 5, 2, 7, 1 }
"""

import copy
def array_elements_ranks(array):
    """
    This function returns rank of given array elements
    """
    result = []
    new_array = copy.deepcopy(array)
    for first_value in range(len(new_array)):
        for second_value in range(len(new_array)):
            if new_array[first_value]<new_array[second_value]:
                new_array[first_value],new_array[second_value] = \
                new_array[second_value],new_array[first_value]
    for ind in range(len(array)):
        if array[ind] in new_array:
            result.append(new_array.index(array[ind]))
    print([i+1 for i in result])


array = [10, 8, 15, 12, 6, 20, 1]
array_elements_ranks(array)


