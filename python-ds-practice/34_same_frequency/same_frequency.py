def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    set1 = list(set(str(num1)))
    set2 = list(set(str(num2)))

    for num in set1:
        if set1.count(str(num)) != set2.count(str(num)):
            return False
    return True