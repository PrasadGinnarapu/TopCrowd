"""
25)
In-place merge two sorted arrays
Input:
 
X[] = { 1, 4, 7, 8, 10 }
Y[] = { 2, 3, 9 }
 
Output:
 
X[] = { 1, 2, 3, 4, 7 }
Y[] = { 8, 9, 10 }
"""

def in_place_merge(array_1,array_2):
    """
    This is function docstring
    """
    len_x = len(array_1)
    array_1.extend(array_2)
    array_1.sort()
    return f"X = {[int(i) for i in array_1[:len_x]]} \nY = {[int(i) for i in array_1[len_x:]]}"
print(in_place_merge(input("Enter array_1: ").split(" "),input("Enter array_2: ").split(" ")))