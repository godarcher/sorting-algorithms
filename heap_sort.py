
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
"""

# * This is the main function for heap sort
# It takes an array as input and manipules the array for sorted output
