"""
Given a binary array of size two having at least one element as zero, 
write a single line function to set both its elements to zero. 
Use of ternary operator and direct assignment of elements are not allowed.
There are three combinations of array elements as per problem constraints:

 
arr[0] = 0 and arr[1] = 1
arr[0] = 1 and arr[1] = 0
arr[0] = 0 and arr[1] = 0
"""

def array_elements_to_zero(array):
    """
    This function takes binary array, having atlease one zero element,
    and makes to all elements into zeros in single line.
    """
    return [array[value]*0 if array[value]==1 else array[value] for value in range(len(array))]

array = [0,1]
print(array_elements_to_zero(array))