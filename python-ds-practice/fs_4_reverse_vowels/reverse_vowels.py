from selectors import EpollSelector


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    lst = []
    new_string = ""
    for letter in s:
        if letter in vowels:
            lst.append(letter)
    for letter in s:
        if letter in vowels:
            new_string += (lst.pop())
        else:
            new_string +=letter
    return new_string
    # return new_string
