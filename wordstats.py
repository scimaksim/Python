# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:
#
# Author:
# Date:
# -----------------------------------------------------------------------------
"""
Play a tic-tac-toe game against the computer.

The user always starts playing first.  The user marks a space on the grid by
clicking on that space.  That space is then colored with the user’s assigned
color. The computer immediately plays its move by coloring an available space
with the other color. The game goes on until one player
(the user or the computer) has 3 colored spaces in a line.
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
    """     Enter your function docstring here     """
    # build and return the dictionary for the given filename
    word_count = {}
    lower_text = filename.lower

    with open(filename, 'r', encoding='utf-8') as my_file:
        # read line by line
        for line in my_file:
            # read word by word
            for word in line.split():
                word = word.strip(string.punctuation)
                word_count[word] += 1
    print(word_count)


def report(word_dict):
    """     Enter your function docstring here     """
    # report on various statistics based on the given word count dictionary


def valid_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        result =  False
    finally:
        result = True
        return result


def main():
    # get the input filename and save it in a variable
    filename = input("Which file would you like to analyze?: ")
    # call count_words to build the dictionary for the given file
    count_words(filename)

# save the dictionary in the variable word_count
# call report to report on the contents of the dictionary word_count

# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)


if __name__ == '__main__':
    main()