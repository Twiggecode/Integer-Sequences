def ascendingSelectionSort(MyList):
     for i in range(len(MyList) - 1):
         minimum = i
         for j in range( i + 1, len(MyList)):
             if(MyList[j] < MyList[minimum]):
                 minimum = j
         if(minimum != i):
             MyList[i], MyList[minimum] = MyList[minimum], MyList[i]
     return MyList

def descendingSelectionSort(MyList):
     for i in range(len(MyList) - 1):
         minimum = i
         for j in range(len(MyList)-1,i,-1):
             if(MyList[j] > MyList[minimum]):
                 minimum = j
         if(minimum != i):
             MyList[i], MyList[minimum] = MyList[minimum], MyList[i]
     return MyList

if __name__ == '__main__':
     listItems = [90,42,64, 25, 12, 22, 11,5,4,2,9,8,0,1,7,2]
     print('Selection Sort in ascending order:',ascendingSelectionSort(listItems))
     print('Selection Sort in descending order:',descendingSelectionSort(listItems))
