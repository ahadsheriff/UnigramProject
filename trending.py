"""
Author: Ahad Sheriff
File: trending.py

The main program for task 3
Task 3:
Compute trends.
In this task, you will choose a starting year and an ending year, and identify
which words saw the greatest increase (or decrease) in usage in this timespan.

"""

import wordData
from wordData import *


def trending(words, startYr, endYr):
    """

    :param words: A dictionary mapping words to lists of YearCount objects
    :param startYr: An integer, the starting year for the computation of the trending words
    :param endYr: An integer, the ending year for the computation of the trending words.
    :return: A list containing a WordTrend entry for each word for which qualifying data exists.
    """

    trendlist = []
    for word in words:
        starting = 0.0
        ending = 0.0
        line = words[word]

        for i in line:
                if i.year == startYr:
                    if i.count >= 1000:
                        starting += i.count
                if i.year == endYr:
                    if i.count >= 1000:
                     ending += i.count
        if starting >= 1000 and ending >= 1000:
            trend = ending/starting
            temp = wordData.WordTrend(word, float(trend))
            trendlist.append(temp)

    sortedList = sorted(trendlist, key=Eval, reverse=True)

    return sortedList

def Eval(key):
    return key.trend

def main():
    file = input("Enter the name of a file to read: ")
    words = wordData.readWordFile(file)
    start = input("Enter starting year: ")
    end = input("Enter ending year: ")

    trends = (trending(words, float(start), float(end)))

    print("")

    print("The top 10 trending words from", start, "to", end, ":")
    for x in trends[:10]:
        print(x.word)

    print("")

    print("The bottom 10 trending words from", start, "to", end, ":")


    mylist = []
    for x in trends[-10:]:
        mylist.append(x.word)
    mylist.reverse()
    for i in mylist:
        print(i)

if __name__ == '__main__':
    main()