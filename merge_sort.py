
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

# Function


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the middle of the array
        r = len(arr)//2

        # Dividing array into two halves
        leftArray = arr[:r]
        rightArray = arr[r:]

        # Calling mergesort function on subparts of array
        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        # Copying data to temp arrays leftArray[] and rightArray[]
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

# function to print the array


def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code
if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    print("Original array")
    display(arr)
    mergeSort(arr)
    print("Sorted array")
    display(arr)
