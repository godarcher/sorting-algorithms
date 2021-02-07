
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


def merge_Sort(input_array):
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

        # We recursively call this function for the subsets left side and right side
        merge_Sort(left_side)
        merge_Sort(right_side)

        # We create three integers with value 0
        # I is index of left side, J of right side, K of input array
        i = j = k = 0

        # We coppy the data to left side and right side arrays.
        while i < len(left_side) and j < len(right_side):

            # If right is bigger then left
            if left_side[i] < right_side[j]:

                # We set element k of the array to element i of left side
                input_array[k] = left_side[i]

                # Increment i by 1
                i += 1
            # If right is smaller then left
            else:

                # We set element k of the array to element j of right side
                input_array[k] = right_side[j]
                # Increment j by 1
                j += 1

            # We increment k anyways (independent of if else above)
            k += 1

        # As long as index of left side is lower then size of left side (for size of left side)
        while i < len(left_side):

            # We set element k of the array to element i of left side
            input_array[k] = left_side[i]

            # Increment i by 1, k also
            i += 1
            k += 1

    # As long as index of right side is lower then size of right side (for size of right side)
        while j < len(right_side):

            # We set element k of the array to element j of right side
            input_array[k] = right_side[j]

            # Increment j by 1, k also
            j += 1
            k += 1


def display(input_array):
    # ? This function will print the elements of the array
    # * It takes sorted array input_array as input

    # For every element inside the now sorted array
    for element in range(len(input_array)):

        # Print the actual element
        print(input_array[element], end=" ")

    # then print a new line after the entire for loop
    print()


# This code contains the main function (ran on running code)
if __name__ == '__main__':

    # We create an unsorted example array
    unsorted_array = [6, 5, 12, 10, 9, 1, 3, 12, 25, 8, 1]

    # We print the original array first
    print("Original array")
    display(unsorted_array)

    # Then we use merge sort to sort the unsorted array
    merge_Sort(unsorted_array)

    # Now we can print the array, which now is sorted by mergesort
    print("Sorted array")
    display(unsorted_array)
