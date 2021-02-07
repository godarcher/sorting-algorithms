
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


def build_heap(input_array, n, root):

    # Initialize the largests value to be the root element
    largest = root

    # Calculate the left and right of the heap stack
    left = 2 * root + 1
    right = 2 * root + 2

    # if left inside scope (exists) and greater then largest overwrite root
    if left < n and input_array[largest] < input_array[left]:
        largest = left

    # if right inside scope (exists) and greater then largest overwrite root
    if right < n and input_array[largest] < input_array[right]:
        largest = right

    # If largest is overwritten (not i anymore)
    if largest != root:

        # We swap i with largest
        input_array[root], input_array[largest] = input_array[largest], input_array[root]

        # Then we build the heap again (recursive call!)
        build_heap(input_array, n, largest)

# The main function to sort an array of given size


def sort_heap(input_array):
    n = len(input_array)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        build_heap(input_array, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        input_array[i], input_array[0] = input_array[0], input_array[i]  # swap
        build_heap(input_array, i, 0)


# Driver code
input_array = [12, 11, 13, 5, 6, 7]
sort_heap(input_array)
n = len(input_array)
print("Sorted array is")
for i in range(n):
    print("%d" % input_array[i]),
