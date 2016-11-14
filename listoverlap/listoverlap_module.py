#!/bin/python3.5
from random import randint


def generate_list(length):
    ranList = []
    for i in range(length):
        ranList.append(randint(1, 100))
    ranList.sort()
    return ranList


def listoverlap(list1, list2):
    overlap = []
    for item1 in list1:
        if (item1 in list2) and (item1 not in overlap):
            overlap.append(item1)
    return overlap


def main():
    listOne = generate_list(10)
    listTwo = generate_list(10)
    print(listOne)
    print(listTwo)
    print(listoverlap(listOne, listTwo))
    return


if __name__ == '__main__':
    main()
