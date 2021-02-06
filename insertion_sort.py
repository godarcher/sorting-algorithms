
#! This program uses insertion sort to sort an unserted array and prints it to console

# * This is the main function for insertionsort
# It takes an array as input and manipules the array for sorted output
def insertion_Sort(input_array):

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
