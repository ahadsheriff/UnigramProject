"""
Author: Ahad Sheriff
File: printedWords.py

The main program for task 2
Task 2:
Compute the number of printed words.
In this task, I will compute the total number of printed words as a
function of year. Ultimately I will plot this information and see
how the total number of printed words has increased or decreased
over the years.
"""

from wordData import *
import simplePlot

def printedWords(words):
    """
    All the YearCount entries for each year a word exists
    :param words: A dictionary mapping words to lists of YearCount objects
    :return: A list containing a YearCount entry for each year for which data exists.
    The list is sorted in ascending order of year.
    """

    table = {}
    newlist = []

    for word in words:

        list = words[word]

        for i in list:

            # years.append(i)

            key = i.year
            value = i.count

            if key in table:
                table[key] += value

            elif key not in table:
                table[key] = value

    for key in table:
        temp = wordData.YearCount(key, table[key])
        newlist.append(temp)

    return newlist


def wordsForYear(year, yearList):
    """

    :param year: An integer representing the year being queried
    :param yearList: a list of YearCount objects
    :return: An integer count reprenting the total number of printed words for that year.
             If none, return 0.

    """

    for i in yearList:
        if i.year == int(year):
            return i.count

    return 0

def plot(newlist):

    labels = "Year", "Total Words"
    plot = simplePlot.plot2D('Number of printed words over time', labels)
    for yc in newlist:
        point = yc.year, yc.count
        plot.addPoint(point)
    plot.display()

def main():
    file = input("Enter the name of a file to read: ")
    words = wordData.readWordFile(file)
    printed = (printedWords(words))
    year = input("Enter year: ")
    wordyear = wordsForYear(year, printed)
    print("Total printed words in", year, ":", wordyear)

    plot(printed)

if __name__ == '__main__':
    main()