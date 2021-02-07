
#! This program uses merge sort to sort an unserted array and prints it to console

"""
? In computer science, merge sort (also commonly spelled mergesort) is an efficient, general-purpose, comparison-based sorting algorithm.
? Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.
? Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.[2]
? A detailed description and analysis of bottom-up merge sort appeared in a report by Goldstine and von Neumann as early as 1948.[3]

? Conceptually, a merge sort works as follows:
* Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
* Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
"""


def mergeSort(input_array):
    # ? The mergesort function sorts using dividing and merging sublists.
    # * The input it takes is an input_array, which normally is unsorted.

    # If the amount of elements inside the array is more then 1 (otherwise already sorted)
    if len(input_array) > 1:

        # We take the middle index by dividing the length by 2
        middle = len(input_array) // 2

        # The left part of the array is the input array from start till middle (using substring method)
        left_side = input_array[:middle]

        # The right part of the array is the input array from middle till end (using substring method)
        right_side = input_array[middle:]

        # Calling mergesort function on subparts of array
        mergeSort(left_side)
        mergeSortright_side)

        i=j=k=0

        # Copying data to temp arrays leftArray[] and rightArray[]
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                input_array[k]=left_side[i]
                i += 1
            else:
                input_array[k]=right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            input_array[k]=left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            input_array[k]=right_side[j]
            j += 1
            k += 1

# function to print the array


def display(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()


# driver code
if __name__ == '__main__':
    arr=[6, 5, 12, 10, 9, 1]
    print("Original array")
    display(arr)
    mergeSort(arr)
    print("Sorted array")
    display(arr)
