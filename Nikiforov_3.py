# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     assignment # 3
#
# Author:      Maksim Nikiforov
# Date:        1015/2016
# -----------------------------------------------------------------------------
"""
Translates a given text into a secret language

Each word in the text is translated according to the following rules:
If the word starts with a vowel, append 'zus' to the word.
The vowels are a, e, i, o, u.
Otherwise, take the first letter of the word,
move it to the end, and then append 'ix'.
"""


def starts_with_vowel(word):
    """
    Return 'True' if the word starts with a vowel and 'False' otherwise

    parameter: word
    returns: 'True' if the word starts with a vowel and 'False' otherwise
    """
    vowels = ['a', 'e', 'i', 'o', 'u']    # Create list of all vowels
    if word[0] in vowels:                 # Check if first letter is a vowel
        return True
    else:
        return False


def encode(word):
    """
    Translate a single word to the secret language

    parameter: word to be translated
    returns: translated string
    """

    if starts_with_vowel(word):           # Decide which append pattern to use
        word += 'zus'                     # Case with first-letter vowels
    else:
        word = word[1:] + word[0] + 'ix'  # Case with first-letter consonants

    return word                           # Return a single, translated word


def translate(text):
    """
    Translate whole text to the secret language

    parameter: text to be translated
    returns: full text in secret language
    """

    translated_words = []                 # Empty list to hold translated words
    text = text.split()                   # Split sentence into list of words

    for word in text:                     # Translate each word using 'encode'
        translated_words.append(encode(word))  # Add to list of transl. words

    full_translated_string = ' '.join(translated_words)  # Join all words

    return full_translated_string         # Return fully-translated string


def get_input():
    """
    Prompt the user for input repeatedly until they enter a non-empty string

    input: none
    returns: text entered by the user
    """

    string_empty = True

    while string_empty:                 # Prompt the user for input (cont.)
        text = input("Please enter your message: ")
        if text:                        # Stop prompting when a word is entered
            string_empty = False
            return text


def main():
    user_input = get_input()                    # Get input from the user
    translated_text = translate(user_input)     # Translate the input
    print(translated_text)                      # Print the result

if __name__ == '__main__':
    main()
