
#! This algorithm combines quicksort and binary search for demonstration purposes.
# ? Further details and explanations about these methods can be found in the other files.

#?############
#* FUNCTIONS #
#?############

def partition_array(input_array, low, high):
    # ? The partition functions takes the last element of an array as pivot.
    # * It then places this pivot at the correct positions and uses it to sort the remaining data left and right of it.

    # Smaller is left of low, so it should be a smaller element
    smaller = (low-1)

    # The pivot is the high of the input array (last element)
    pivot = input_array[high]

    # For every element between low and high
    for element in range(low, high):

        # If current element is smaller than the pivot
        if input_array[element] < pivot:

            # We increment the smaller element by 1
            smaller += 1

            # We swap
            input_array[smaller], input_array[element] = input_array[element], input_array[smaller]

    # After all the computations, we adjust accordingly
    input_array[smaller +
                1], input_array[high] = input_array[high], input_array[smaller+1]

    # We return the value
    return (smaller+1)


def quick_Sort(input_array, low, high):
    # ? This function uses recursive calls with smaller arrays from partitions
    # * it continues till it has recursively quicksorted the array

    # If high is higher then low (logical condition)
    if low < high:

        # input_array[pi] is now rightly sorted
        partition_index = partition_array(input_array, low, high)

        # Recursively sort the left part of the array (pivot - 1)
        quick_Sort(input_array, low, partition_index - 1)

        # Recursively sort the right part of the array (pivot + 1)
        quick_Sort(input_array, partition_index + 1, high)


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


def display(input_array):
    # ? This function will print the elements of the array
    # * It takes sorted array input_array as input

    # For every element inside the now sorted array
    for element in range(len(input_array)):

        # Print the actual elements, with spaces in between following elements.
        print(input_array[element], end=" ")

    # then print a new line after the entire for loop
    print()

#?###################
#* Actual main code #
#?###################


# This is the unsorted input array
unsorted_array = [10, 7, 8, 9, 1, 5, 21, 3, 5, 11, 18, 31, 2, 4, 56, 6]

# Size is the amount of elements inside the unsorted array
size = len(unsorted_array)

# Apply quick sort (including partitioning) to the unsorted array
quick_Sort(unsorted_array, 0, size-1)

# Show the quicksorted array
print("Sorted array")
display(unsorted_array)

# Find element 11 in sorted array using binary search
binary_Search(unsorted_array, 1, len(unsorted_array), 11)
