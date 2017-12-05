def longest(*args):
    longest_word_length = 0
    longest_word = ''
    for arg in args:
        if len(arg) > longest_word_length:
            longest_word = arg
    if longest_word:
        return longest_word
    else:
        return None

longest('hi', 'hello', 'python')