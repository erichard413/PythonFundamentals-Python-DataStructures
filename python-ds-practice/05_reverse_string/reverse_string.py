def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]  ## slice [::-1] means start at the END, with step of -1, meaning working backwards TOWARDS position 0.
