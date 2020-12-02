def count_words(text):
    """ Count and returns the number of words in a string.

    The counting is performed iterating over the characters 
    in the text and counting the number of times that an 
    space character (space, tabs, new lines) is preceeded 
    by a non-space character.

    Args:
        text (str): text to have words counted

    Returns:
        int: the number of words in the text

    Raises:
        ValueError: If text is not an instance of str.
    """
    if not isinstance(text, str):
        raise TypeError('The argument must be an instance of str')

    total_words = 0
    is_current_space = None
    is_previous_char = None
    for char in text:
        is_current_space = char.isspace()
        if is_current_space and is_previous_char:
            total_words += 1
        is_previous_char = not is_current_space
    if is_previous_char:
        total_words += 1
    return total_words
