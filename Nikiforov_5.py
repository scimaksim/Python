# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     Compute language statistics based on the contents of a file
#
# Author:      Maksim Nikiforov
# Date:        10/28/2016
# -----------------------------------------------------------------------------
"""
This program computes language statistics based on the contents of a file.

Enter the name of a file to analyze. This program then computes the longest
word in the file, the five most common words, and the word count of all words
in the file. The word count is placed into a .txt file called "out.txt".
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


# Enter your own helper function definitions here


def count_words(filename):
    """
    Produce a dictionary of "word: word count" pairs.

    Parameters:
        filename (string) - name of the file which will be opened
    Output:
        word_dict - dictionary with the count of all words in the file
    """
    # initialize the dictionary for the given filename
    word_dict = {}

    with open(filename, 'r', encoding='utf-8') as my_file:
        # read line by line (needed for large files)
        for line in my_file:
            # ignore capitalization
            line = line.lower()
            # create list of words from each line in file
            for word in line.split():
                # take out leading, trailing punctuation characters and numbers
                word = word.strip(string.punctuation + string.digits)
                # ignore whitespace, update word count of each word
                if word:
                    word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def report(word_dict):
    """
    Report on various statistics based on the given word count dictionary

    Parameters:
        word_dict (dictionary) - disctionary of all words and their count
    Output:
        out.txt - text file with all words and their word count
        longest word (printed)
        five most common words (printed)
    """
    # dictionary sorted in descending order according to frequency of words
    sorted_dict = sorted(word_dict, key=word_dict.get, reverse=True)

    # determine the longest word in the file
    longest_word = max(sorted_dict, key=len)
    print("The longest word is:", longest_word)

    # list of the 5 most common words
    common_words = sorted_dict[:5]

    print("The five most common words are:")
    for word in common_words:
        print(word + ':', word_dict[word])

    # output the word count of all words into a file
    with open('out.txt', 'w', encoding='utf-8') as my_file:
        for word in sorted(word_dict):
            word_stat = word + ' : ' + str(word_dict[word]) + '\n'
            my_file.write(word_stat)


def main():
    # get the input filename and save it in a variable
    filename = input("Which file would you like to analyze?: ")
    # call count_words to build the dictionary for the given file
    word_count = count_words(filename)
    # call report to report on the contents of the dictionary word_count
    report(word_count)
    # If you want to generate a word cloud, uncomment the line below.
    draw_cloud(word_count)


if __name__ == '__main__':
    main()
