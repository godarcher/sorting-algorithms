
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


def linear_search(values, searched):
    # The function takes in only two parameters.
    # 'Searched' is the element being looked for.
    # 'Values' is the list in which the element is searched.
    for i in range(0, len(values)):
        # We iterate over every element in the list.
        if (values[i] == searched):
            # If we find the element, we return the position of the element in the list.
            return "Element " + str(searched) + " is at " + str(i+1)
    # If we don't find the element, we return an 'absent statement'
    return "Element has not been found"
