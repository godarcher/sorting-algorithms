
#! This algorithm uses binary search to find an item inside a sorted database

"""
? In computer science, binary search, also known as half-interval search,[1] logarithmic search,[2] or binary chop,[3] 
? is a search algorithm that finds the position of a target value within a sorted array.[4][5] 
? Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated 
? and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.
? If the search ends with the remaining half being empty, the target is not in the array.

* Binary search runs in logarithmic time in the worst case, making {\displaystyle O(\log n)}O(\log n) comparisons, 
* where {\displaystyle n}n is the number of elements in the array.[a][6]
"""


def binary_Search(sorted_array, left, right, element):
    # l is the starting reference to find the middle.
    # It will keep changing time we split the array to get subarrays.
    # Hence it is not hard coded into the algorithm.
    # It won't make much importance to the user since the user needs to know the first middle point is in reference with the first index which is zero.
    # Therefore when calling the function, l will be 0.
    # R is the lenght of the list.
    # Python's len() function gives the accurate lenght but indexing starts at one value less.
    # Hence the lenght will be one value less.
    # Check if the list has not been exhausted.
    if right >= left:
        # We are checking i
        mid = left + (right - left) // 2
        # We start at the middle of the list and check if the element
        if sorted_array[mid] == element:
            return "Element " + str(element) + " is at " + str(mid + 1)
        # We check if the element is on the left side of the split array
        elif sorted_array[mid] > element:
            return binary_Search(sorted_array, left, mid-1, element)
        # Otherwise, the element is in the right side of the split array.
        else:
            return binary_Search(sorted_array, mid + 1, right, element)
    # If we fail to find the element in the list we return an absent statement.
    else:
        # Element is not present in the array
        return "Element " + str(element) + " is not in the list"
