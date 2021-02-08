
#! This program uses insertion sort to sort an unserted array and prints it to console

"""
? Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
? It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
? However, insertion sort provides several advantages:
    * Simple implementation: Jon Bentley shows a three-line C version, and a five-line optimized version[1]
    * Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    * More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
    * Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(kn) when each element in the input is no more than k places away from its sorted position
    * Stable; i.e., does not change the relative order of elements with equal keys
    * In-place; i.e., only requires a constant amount O(1) of additional memory space
    * Online; i.e., can sort a list as it receives it
"""


def insertion_Sort(input_array):
    # * This is the main function for insertionsort
    # It takes an array as input and manipules the array for sorted output

    # For entire input array
    for i in range(1, len(input_array)):

        # The key is the index of the input array
        index = input_array[i]

        # Shifting elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and index < input_array[j]:
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = index


# For this example we created an unsorted array
unsorted_array = [19, 4, 55, 13, 12, 3, 99, 8]

# apply the function to our unsorted array
insertion_Sort(unsorted_array)

# This code section generates the output
print("")
print("The insertion sorted array is:")

# We iterate over the entire array length
for i in range(len(unsorted_array)):
    # We print each element of the sorted output array
    print("%d" % unsorted_array[i])

print("")
