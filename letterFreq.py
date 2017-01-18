"""
Author: Ahad Sheriff
File: letterFreq.py

The main program for task 1.
Task 1:
Compute relative letter frequency. In this task, you will compute
the relative frequencies of the 26 English letter across all data
in our database.

"""

from wordData import *
import wordData

"""
The output does not print when I use the test function, because there is a bug when I import file letterFreq
and call function letterFreq.
"""

def letterFreq(words):
    """
    :param words: A dictionary mapping words to lists of YearCount objects aka the data from readWord function
    :return: A string containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character.
    """

    table = {}
    letterString = []


    for word in words:

        times = totalOccurrences(word, words)

        for letter in word:

            if letter in table:
                table[letter] = table[letter] + times

            else:
                table[letter] = times


    for key in table:
        temp = (key, table[key])
        letterString.append(temp)

    sortedList = sorted(letterString, key=getKey, reverse=True)

    string = ""
    for item in sortedList:
        string += item[0]

    return string

def getKey(item):
    return item[1]

def main():
    file = input("Enter the name of a file to read: ")
    words = wordData.readWordFile(file)
    print(letterFreq(words))

if __name__ == '__main__':
    main()