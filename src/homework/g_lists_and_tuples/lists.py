def get_lowest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    lowest = first[0]
    for num in first[1:]:
        if num < lowest:
            lowest = num
            return lowest
        
def get_highest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    highest = first[0]
    for num in first[1:]:
        if num > highest:
            highest = num
        return highest