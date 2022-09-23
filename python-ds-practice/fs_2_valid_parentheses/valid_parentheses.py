def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 != 0:
        return False
    dict = {'(' : ')'}
    lst = []
    for letter in parens:
        if letter in dict.keys():
            lst.append(letter)
        else:
            if lst == []:
                return False
            a = lst.pop()
            if letter != dict[a]:
                return False
    return lst == []
