
#! This program uses heap sort to sort an unserted array and prints it to console

"""
? Why array based representation for Binary Heap? 
? Since a Binary Heap is a Complete Binary Tree, it can be easily represented as an array and the array-based representation is space-efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

? Heap Sort Algorithm for sorting in increasing order: 
* 1. Build a max heap from the input data. 
* 2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. 
        *  Finally, heapify the root of the tree. 
*3. Repeat step 2 while size of heap is greater than 1.

? How to build the heap? 
? Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom-up order.
* https://www.geeksforgeeks.org/heap-sort/
"""


def build_heap(input_array, size, root):
    # ? This function builds the heap out of a binary tree and swaps

    # Initialize the largests value to be the root element
    largest = root

    # Calculate the left and right of the heap stack
    left = 2 * root + 1
    right = 2 * root + 2

    # if left inside scope (exists) and greater then largest overwrite root
    if left < size and input_array[largest] < input_array[left]:
        largest = left

    # if right inside scope (exists) and greater then largest overwrite root
    if right < size and input_array[largest] < input_array[right]:
        largest = right

    # If largest is overwritten (not i anymore)
    if largest != root:

        # We swap i with largest
        input_array[root], input_array[largest] = input_array[largest], input_array[root]

        # Then we build the heap again (recursive call!)
        build_heap(input_array, size, largest)


def sort_heap(input_array):
    # ? This function iterates over the build heap and uses it to sort the input

    # We calculate the amount of elements inside the input array
    size = len(input_array)

    # Build a heap from high to low
    for element in range(size//2 - 1, -1, -1):
        # We build the heap
        build_heap(input_array, size, element)

    # Extract the elements and make swaps
    for element in range(size-1, 0, -1):
        # We swap the values
        input_array[element], input_array[0] = input_array[0], input_array[element]
        # We build the heap
        build_heap(input_array, element, 0)


# Unsorted Array
unsorted_array = [13, 15, 3, 4, 6, 11, 21, 4, 42]

# Apply the heap sort function on the unsorted array
sort_heap(unsorted_array)

# Calculate the size of the unsorted array
size = len(unsorted_array)

# Print the output
print("")
print("Sorted array is")

# For every element in the sorted array
for element in range(size):
    # Print the actual element
    print("%d" % unsorted_array[element]),
