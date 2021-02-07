
#! This program uses quick sort to sort an unserted array and prints it to console

"""
? Quicksort is an efficient sorting algorithm. Developed by British computer scientist Tony Hoare in 1959[1] and published in 1961,[2] 
? it is still a commonly used algorithm for sorting. When implemented well, it can be about two or three times faster than its main competitors, merge sort and heapsort.

? Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
? according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort.[4] 
? The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.

? Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined.
? Efficient implementations of Quicksort are not a stable sort, meaning that the relative order of equal sort items is not preserved.
? Mathematical analysis of quicksort shows that, on average, the algorithm takes O(n log n) comparisons to sort n items. 
? In the worst case, it makes O(n2) comparisons, though this behavior is rare.
"""


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


# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_Sort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
