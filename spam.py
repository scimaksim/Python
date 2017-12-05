# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     Compute a 'spam indicator' for a phrase
#
# Author:      Maksim Nikiforov
# Date:        10/22/2016
# -----------------------------------------------------------------------------
"""
This program classifies messages as either SPAM (unwanted) or HAM (wanted).

This program computes a 'spam indicator' for a phrase based on a set of
pre-defined spam words. If the spam indicator exceeds the spam threshold,
the message is classified as "spam".  Otherwise, it is classified as "ham".
"""
import string                          # Access pre-defined string constants

SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free','offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

SPAM_THRESHOLD = 0.10                   # Global spam threshold: 0.10


def spam_indicator(text):
    """
    This function returns the spam indicator rounded to two decimals

    parameter: user message
    returns:   spam ratio of the message
    """

    spam_word_count = 0                 # Total count of spam words in phrase

    lower_text = text.lower()           # Make program case insensitive
    for char in string.punctuation:     # Get rid of punctuation
        lower_text = lower_text.replace(char, '')

    unique_words = lower_text.split()   # Create a list out of the phrase
    unique_words = set(unique_words)    # Convert to set (isolate unique words)

    for word in unique_words:           # Count total number of spam words
        if word in SPAM_WORDS:
            spam_word_count += 1
        else:
            continue

    spam_ratio = spam_word_count/len(unique_words)
    spam_ratio = round(spam_ratio, 2)

    return spam_ratio


def classify(indicator):
    """
    This function prints the spam classification based on SPAM_THRESHOLD

    parameter: indicator (float)
    returns:   message classification (SPAM or HAM)
    """
    #

    if indicator >= SPAM_THRESHOLD:
        return "SPAM"
    else:
        return "HAM"


def get_input():
    """
    Prompt the user for input and return the input

    parameter: none
    returns:   phrase entered by the user
    """

    message = input("Please enter your message: ")

    return message


def main():

    user_input = get_input()                    # Get user input and save it
    spam_ratio = spam_indicator(user_input)     # Compute the spam indicator
    print("SPAM indicator:", spam_ratio)        # Print the spam_indicator
    print("This message is:", classify(spam_ratio))  # Print classification

if __name__ == '__main__':
    main()