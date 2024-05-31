"""
Aurelio Amparo
Program: Bubble Sort
2020-07-2021
"""
import random
def BubbleSort(_list):
    sorttype = input("(A)scending, (D)escending: ").upper()
    while (sorttype != "A" and sorttype != "D" and sorttype != "Q"):
        sorttype = input("(A)scending, (D)escending: ").upper()
    capCount = 0
    swapCount = 0
    print("\nUnsorted Data: "+str(_list))
    for i in range(0, len(_list)-1):
        for j in range(0, len(_list)-i-1):
            capCount+=1
            if (sorttype == "A"):
                if (_list[j] > _list[j+1]):
                    swapCount+=1
                    temp = _list[j]
                    _list[j] = _list[j+1]
                    _list[j+1] = temp
            elif (sorttype == "D"):
                if (_list[j] < _list[j+1]):
                    swapCount+=1
                    temp = _list[j]
                    _list[j] = _list[j+1]
                    _list[j+1] = temp
    print("""
Sorted Data: """+str(_list)+"""
Comparisons: """+str(capCount)+"""
Swaps: """+str(swapCount)+"""

""")


def SelectionSort(_list):
    sorttype = input("(A)scending, (D)escending: ").upper()
    while (sorttype != "A" and sorttype != "D" and sorttype != "Q"):
        sorttype = input("(A)scending, (D)escending: ").upper()
    print("\nUnsorted Data: "+str(_list))
    for i in range(len(_list)):
        temp = i
        for j in range(i+1, len(_list)):
            if (sorttype == "A"):
                if (_list[i] > _list[j]):
                    temp = j                   
                _list[i], _list[temp] = _list[temp], _list[i]
            elif (sorttype == "D"):
                if (_list[i] < _list[j]):
                    temp = j                    
                _list[i], _list[temp] = _list[temp], _list[i]
    print("Sorted Data: "+ str(_list) )


def InsertionSort(_list):
    sorttype = input("(A)scending, (D)escending: ").upper()
    while (sorttype != "A" and sorttype != "D" and sorttype != "Q"):
        sorttype = input("(A)scending, (D)escending: ").upper()
    capCount = 0
    swapCount = 0
    print("\nUnsorted Data: "+str(_list))
    for i in range (1, len(_list)):
        temp = _list[i]
        num = i-1
        while num >= 0 and temp < _list[num]:
            _list[num + 1] = _list[num]
            num -=1
        _list[num+1] = temp
    print("Sorted Data: "+ str(_list) )


def Main():
    dataList = []
    userInput = input("How many numbers do you want to sort? ")
    while (userInput != int()):
        for i in range(userInput):
            temp = random.randint(1,100)
            dataList.append(temp)
        InsertionSort(dataList) 
        dataList = [] 
        break
    userInput2 = input("please type a sentence: ")
    while (userInput2 != str()):
        userInput2 = userInput2.replace(" ", "")
        for i in userInput2:
            dataList.append(i)
        InsertionSort(dataList) 
        break

Main()
















