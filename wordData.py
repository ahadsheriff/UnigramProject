"""
Author: Ahad Sheriff
File: wordData.py

A supporting module. Will include class definitions and utility functions relevant to all tasks.
(Will refer to this as task 0)
"""

from rit_lib import *
import wordData

class YearCount(struct):
    _slots = ((int, "year"), (int, "count"))

class WordTrend(struct):
    _slots = ((str, "word"), (float, "trend"))

def readWordFile(fileName):
    """

    :param fileName: A file from inside the "data/" file
    :return:

    """

    file = open("data/" + fileName)

    table = {}
    list = []
    lastline = []

    for line in file:
        line = line.strip()
        line = line.split(",")


        if len(line) == 1 and len(lastline) == 2:
            key = line[0]
            table[key] = list
            list = []

        if len(line) == 1:
            key = line[0]
            table[key] = list


        elif len(line) == 2:
            list.append(YearCount(int(line[0]), int(line[1])))

        lastline = line

    file.close()
    return table

def totalOccurrences(word, words):
    """

    :param word: The word for which to calculate the count. Not guaranteed to exist in
    words.
    :param words: A dictionary mapping words to lists of YearCount objects.
    :return: The total number of times that a word has appeared in print.

    """
    count = 0

    if word in words:
        list = words[word]
        for i in list:
            count += i.count

    return count

def main():
    file = input("Enter the name of a file to read: ")
    words = wordData.readWordFile(file)
    print(words)

    word = input("Enter word you want to count the occurences of: ")
    print(totalOccurrences(word, words))

if __name__ == '__main__':
    main()