def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # new_list = []
    # for item in l1:
    #     if l2.count(item) > 0:
    #         new_list.append(item)
    # return new_list
    
    new_list = []
    for item in l1:
        if item in l2:
            new_list.append(item)
    return new_list