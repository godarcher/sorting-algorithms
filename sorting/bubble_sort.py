
#! This program uses bubble sort to sort an unserted array and prints it to console

"""
? Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
? compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
? The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.
?
? This simple algorithm performs poorly in real world use and is used primarily as an educational tool. 
? More efficient algorithms such as quicksort, timsort, or merge sort are used by the sorting libraries built into popular programming languages such as Python and Java
?
? Bubble sort has a worst-case and average complexity of О(n2), where n is the number of items being sorted. Most practical sorting algorithms have substantially better 
? worst-case or average complexity, often O(n log n). Even other О(n2) sorting algorithms, such as insertion sort, generally run faster than bubble sort, and are no more complex.
? Therefore, bubble sort is not a practical sorting algorithm.
"""

# * This is the main function for bubble sort
# It takes an array as input and manipules the array for sorted output


def bubble_Sort(input_array):

    # size is the amount of elements of the input array
    size = len(input_array)

    # We traverse trough every element of the input array
    for i in range(size):

        # For all between 0 and size - current element - 1
        for j in range(0, size - i - 1):

            # If the element is bigger then the next element, we swap
            if input_array[j] > input_array[j+1]:

                # The actual swap
                input_array[j], input_array[j +
                                            1] = input_array[j+1], input_array[j]


# For demonstration purposes, we create an empty array
unsorted_array = [63, 24, 29, 32, 12, 19, 10, 71, 31, 42]

# Printing unsorted array
print("")
print("Unsorted Array : ", unsorted_array)

# sort the unsorted array
bubble_Sort(unsorted_array)

# Printing Sorted Array
print("Final Sorted array : ", unsorted_array)
print("")
