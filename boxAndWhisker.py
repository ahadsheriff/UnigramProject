"""
Author: Ahad Sheriff
File: boxAndWhisker.py

The plotting module for task 4. This module supports task 5.
Display a distribution.
For this task, you will write a program to generate a "box-and-whisker"
plot as a tool to visually represent a data set.
"""

import turtle

t = turtle


def boxAndWhisker(small, q1, med, q3, large):
    """
    input: 5 number summary
    will use turtle to draw box and whisker plot according to the input

    """

    range = (large-small)*2
    rangeToQ1 = (q1-small)*4
    rangeToMed = (med-q1)*4
    rangeToQ3 = (q3-med)*4
    rangeToMax = (large-q3)*4

    t.hideturtle()
    initialize()
    markMin(range)
    t.forward(rangeToQ1)
    drawQ1(rangeToMed)
    drawMed()
    drawQ3(rangeToQ3)
    t.forward(rangeToMax)
    markMax()
    t.done()

def initialize():
    t.up()
    t.left(90)

def markMin(range):

    t.left(90)
    t.forward(range*2)
    t.down()
    t.right(90)
    t.forward(10)
    t.back(20)
    t.up()
    t.forward(10)
    t.right(90)
    t.down()


def markMax():
    t.left(90)
    t.forward(10)
    t.back(20)
    t.forward(10)

def drawQ1(rangeToMed):

    initialize()
    t.down()
    t.forward(25)
    t.right(90)
    t.forward(rangeToMed)
    t.back(rangeToMed)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(rangeToMed)

def drawMed():
    initialize()
    t.down()
    t.forward(50)
    t.back(50)
    t.right(90)

def drawQ3(rangeToQ3):
    initialize()
    t.down()
    t.right(90)
    t.forward(rangeToQ3)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(rangeToQ3)
    t.back(rangeToQ3)
    t.left(90)
    t.forward(25)
    t.left(90)

def main():
    small = int(input("Enter the minimum: "))
    q1 = int(input("Enter the first quartile: "))
    med = int(input("Enter the median: "))
    q3 = int(input("Enter the third quartile: "))
    large = int(input("Enter the maximum: "))

    boxAndWhisker(small, q1, med, q3, large)


if __name__ == '__main__':
    main()