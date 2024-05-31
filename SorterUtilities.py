#(1)First, ask the user for the number of arrays to sort and then the number of items in those arrays.
#(2)Create a 2D array with that many arrays of that many random numbers
#(3)Deepcopy (see below) the array and send each array one at a time to your bubble sort function
#(4)Use the timerClass below to time the execution of your sorts
#(5)Deepcopy the original array and do the same steps as before, but with a selection sort
#(6)Repeat the above steps one last time using an insertion sort
#(7)Ask the user if they want to generate another set of arrays. If not, end the program.


# loops though data set compares list[n] to data[n+1]
#if list[n] > data[n+1]
#it swaps them and compares the next number next to compare to
def BubbleSort(_list):
    for i in range(0, len(_list)-1):
        for j in range(0, len(_list)-i-1):
            if (_list[j] > _list[j+1]):
                temp = _list[j]
                _list[j] = _list[j+1]
                _list[j+1] = temp


# loops though our list it compares the list[i] to the other numbers
# if list [i] > the other numbers it places it in the next position of the sorted part of the array.
def SelectionSort(_list):
    for i in range(len(_list)):
        temp = i
        for j in range(i+1, len(_list)):
            if (_list[i] > _list[j]):
                temp = j                   
            _list[i], _list[temp] = _list[temp], _list[i]
    

# starts the loop at list[1]
#store list[i-1] in num  
#if list[i] < num it swaps the num with list[i-1]
def InsertionSort(_list):
    for i in range (1, len(_list)):
        temp = _list[i]
        num = i-1
        while num >= 0 and temp < _list[num]:
            _list[num + 1] = _list[num]
            num -=1
        _list[num+1] = temp
temp = [4,3,4,5]
InsertionSort(temp)
print(temp)

# with this function we can pull out the whole row of our spreadsheet now
def BinarySearch(_list,item):
    for i in range(len(_list)-1):
        for j in range(len(_list[i])-1):
            startIndex = 0
            endIndex = len(_list[j])-1
            while(startIndex <= endIndex):
                mpIndex = startIndex +(endIndex - startIndex) // 2
                midpoint = _list[j][mpIndex]
                if (midpoint == item):
                    return _list[j]
                elif (midpoint > item):
                    endIndex = mpIndex-1

                else:
                    startIndex = mpIndex+1
    return None

