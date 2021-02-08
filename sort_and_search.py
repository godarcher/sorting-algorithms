
#! This algorithm combines quicksort and binary search for demonstration purposes.
# ? Further details and explanations about these methods can be found in the other files.

def binary_Search(sorted_array, start_index, list_length, element):
    # ? This method uses recursion to find an element inside a sorted array.
    # * Start index is the starting index for finding the middle
    # * The starting array will chance when the array becomes smaller.
    # * list_length is the size of the length by len(list) however we compensate 1 for counting from 1

    # We check if the list is not fully traversed (array to small).
    if list_length >= start_index:

        # Calculate the middle of the list.
        middle = start_index + (list_length - start_index) // 2

        # We start at the middle of the list and check if the element is in the middle.
        if sorted_array[middle] == element:
            # If this is the case we print we found the element at this point.
            return "Element " + str(element) + " is at " + str(mid + 1)

        # If not in the middle, check if it is on the left side.
        elif sorted_array[middle] > element:
            # Return a recursive call with the left part of the sorted array.
            return binary_Search(sorted_array, start_index, mid-1, element)

        # If neither, we automaticly know it is on the right side.
        else:
            # Return a recursive call with the right part of the sorted array.
            return binary_Search(sorted_array, mid + 1, list_length, element)

    # This means that the item is not found in the list.
    else:
        # We print the above to let the user known the element was not found.
        return "Element " + str(element) + " is not in this list"
