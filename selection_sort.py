
#! This program uses selection sort to sort an unserted array and prints it to console

"""
? In computer science, selection sort is an in-place comparison sorting algorithm. 
? It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. 
? Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.

? The algorithm divides the input list into two parts:
? a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. 
? Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
? The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element 
? (putting it in sorted order), and moving the sublist boundaries one element to the right.

? The time efficiency of selection sort is quadratic, so there are a number of sorting techniques which have better time complexity than selection sort. 
? One thing which distinguishes selection sort from other sorting algorithms is that it makes the minimum possible number of swaps, n − 1 in the worst case.
"""

# * This is the main function for selection sort
# It takes an array as input and manipules the array for sorted output


def selection_sort(input_array):

    # for every element inside the input array
    for i in range(len(input_array)):

        # Finding the minimum element in remaining unsorted array
        min_value = i

        # For every element inside i+1 --> len(array)
        for j in range(i+1, len(input_array)):

            # If a new lower value is found
            if input_array[min_value] > input_array[j]:

                # Overwrite old value
                min_value = j

        # Swapping input_array[i] with minimum element
        input_array[i], input_array[min_value] = input_array[min_value], input_array[i]


# Unsorted initial array
unsorted_array = [12, 45, 67, 2, 3, 9, 21, 5, 4, 19]

# We use seletion sort to sort the unsorted array
selection_sort(unsorted_array)

print("")
print("Final array after sorting: \n")

# for evey element inside the unsorted array (which is now sorted)
for i in range(len(unsorted_array)):
    # Print element of sorted array
    print(unsorted_array[i])

print("")
