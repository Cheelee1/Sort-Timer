"""
Aurelio Amparo
03-02-21
program: Timing SortTools
"""
import random
from Timer import Timer
import copy
from SorterUtilities import*
from MyUtilities import ClearScreen

def Main():
    while True:
        input1 = input("How many arrays? (Q) to quit: ").upper()
        if(input1 == "Q"):
            break
        input2 = input("How many numbers in array? ")
        dataList = []
        while(input1.isnumeric() == False or input2.isnumeric() == False):
            ClearScreen()
            input1 = input("How many arrays? ")
            input2 = input("How many numbers in array? ")
        for i in range(int(input1)):
            temp = []
            for i in range(int(input2)):
                temp.append(random.randint(1,100))
            dataList.append(temp)
        with Timer(True):
            for i in range(len(dataList)):
                temparray = copy.deepcopy(dataList[i])
                BubbleSort(temparray)
            print("----BubbleSort Complete----")
        with Timer(True):
            for i in range(len(dataList)):
                temparray = copy.deepcopy(dataList[i])
                SelectionSort(temparray)
            print("----SelectionSort Complete----")
        with Timer(True):
            for i in range(len(dataList)):
                temparray = copy.deepcopy(dataList[i])
                InsertionSort(temparray)         
            print("----InsertionSort Complete----")

Main()
