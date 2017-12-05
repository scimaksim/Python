# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys

'''
def url_contents(file_name):
    with open(file_name, 'r', encoding='utf-8') as my_file:
        for url in my_file:
            try:
                with urllib.request.urlopen(url) as url_file:
                    page = url_file.read().decode('UTF-8')
            except urllib.error.URLError as url_err:
                print('Error opening url: ', url, url_err)
            except UnicodeDecodeError as decode_err:
                print('Error decoding url: ', url, decode_err)
            else:
                return page
'''

def paren_references(article, word):
    """
    capture references to the given word found in the given article
    inside parentheses.
    Parameters:
    article (string) - the input text
    word (string) - the word we are searching for
    Return:
    all_references (string) -  references to the word found inside parentheses,
                                separated by new line characters.
                                an empty string if there are no such references
    """
    all_references = ''
    # extract text inside parentheses containing the word
    pattern = r'\>([^\<]*\b{}\b.*?)\<'.format(word)
    matches = re.findall(pattern, article, re.IGNORECASE | re.DOTALL)
    if matches:
        # print("Source \n", url)
        all_references = '\n'.join(matches)
    return all_references


def main():
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        topic = sys.argv[2]
        with open(file_name, 'r', encoding='utf-8') as my_file:
            for url in my_file:
                try:
                    with urllib.request.urlopen(url) as url_file:
                        page = url_file.read().decode('UTF-8')
                except urllib.error.URLError as url_err:
                    print('Error opening url: ', url, url_err)
                except UnicodeDecodeError as decode_err:
                    print('Error decoding url: ', url, decode_err)
                else:
                        text = paren_references(page, topic)
                        if text:
                            with open(topic + "summary.txt", 'a',
                                      encoding='utf-8') as output:
                                output.write("Source \nurl:")
                                output.write(url)
                                output.write('\n')
                                output.write(text),
                                output.write('\n-------------------------\n\n')
    else:
        print("Error:  invalid number of arguments \n"
              "Usage: aggregator.py filename topic")


if __name__ == '__main__':
    main()