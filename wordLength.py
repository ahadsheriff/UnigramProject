"""
Author: Ahad Sheriff
File: wordLength.py

The main program for task 5
Compute word length.
In this task, you will compute the distribution of word length
for our database and compute the five number summary of that distribution. This
summary consists of five numbers characterizing a distribution: the minimum, the first
quartile, the median, the third quartile, and the maximum.

"""

import wordData
import boxAndWhisker

def summaryFromWords(words, year):
    """
    :param words: A dictionary mapping words to lists of YearCount objects.
    :param year: A natural number representing the year of interest.
    :return: a five tuple containing five numbers representing the five number summary
    """

    def wordstoOccur(words):
        """
        Makes a dictionary to see how many times a word occured in a year
        """

        wordsToOccur = {}

        for word in words:
            if word in wordsToOccur:
                for x in words[word]:
                    if x.year == year:
                        wordsToOccur[word] += x.count

            else:
                for v in words[word]:
                    if v.year == year:
                        wordsToOccur[word] = v.count

        return wordsToOccur

    def yeartoWords(words):
        """
        Makes a dictionary that has all the words that exist in a particular year.
        """
        yearToWords = {}

        for word in words:
            list = words[word]

            for i in list:
                thewords = []
                if i.year == year:
                    if i.year in yearToWords:
                        yearToWords[i.year].append(word)
                    else:
                        thewords.append(word)
                        yearToWords[i.year] = thewords

        return yearToWords

    def lengthtoOccur(wordsToOccur, yearToWords):
        """
        Maps the length of each word to the times the length occurred in the year
        """

        lengthToOccur = {}

        for x in yearToWords[year]:

            length = len(x)
            if length in lengthToOccur:
                lengthToOccur[length] += wordsToOccur[x]

            else:
                lengthToOccur[length] = wordsToOccur[x]

        return lengthToOccur

    solution = lengthtoOccur(wordstoOccur(words), yeartoWords(words))
    final = list(solution.items())
    final.sort()

    total = 0
    for x in final:
        total = total + x[1]
    
    small = final[0][0]
    q1 = total//4
    med = total//2
    q3 = (total//4)*3
    large = final[-1][0]

    def math(final, value):
        for i in range(len(final)):
            value = value - final[i][1]
            if value < 0:
                break
        return final[i][0]
    
    med = math(final, med)
    q1 = math(final, q1)
    q3 = math(final, q3)

    summary = (small, q1, med, q3, large)

    return summary


def main():

    file = input("Enter word file: ")
    words = wordData.readWordFile(file)
    year = input("Enter year: ")

    solution = summaryFromWords(words, int(year))

    small = solution[0]
    q1 = solution[1]
    med = solution[2]
    q3 = solution[3]
    large = solution[4]

    print("minimum: ", small)
    print("1st quartile: ", q1)
    print("median: ", med)
    print("3rd quartile ", q3)
    print("maximum: ", large)

    boxAndWhisker.boxAndWhisker(small, q1, med, q3, large)

if __name__ == '__main__':
    main()

