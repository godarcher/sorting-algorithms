
#! This method uses linear search for finding an element inside a list

"""
? In computer science, a linear search or sequential search is a method for finding an element within a list. 
? It sequentially checks each element of the list until a match is found or the whole list has been searched.[1]

* A linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list. 
* If each element is equally likely to be searched, then linear search has an average case of n + 1 / 2 comparisons,
* but the average case can be affected if the search probabilities for each element vary. 
* Linear search is rarely practical because other search algorithms and schemes, such as the binary search algorithm and hash tables, 
* allow significantly faster searching for all but short lists.[2]
"""


def linear_search(input_array, element_tofind):
    # ? linear search checks all elements in a list till the value is found
    # * it takes the input array and the element to be found

    # For every element inside the input array
    for i in range(0, len(input_array)):

        # If it is the element we want to find
        if (input_array[i] == element_tofind):

            # Return the index of the found element.
            return "Element " + str(element_tofind) + " is at index" + str(i+1)

    # We tell the runner that the element has not been found if that's the case
    return "Element is not inside the input array"
