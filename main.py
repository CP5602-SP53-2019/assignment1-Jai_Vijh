import random

def rNGenerator (lowerLimit, upperLimit, numOfValues, noDuplicates):
    randomNumbers = []
    while len(randomNumbers) < numOfValues:
        num = int(random.randrange(lowerLimit, upperLimit+1))
        if (noDuplicates):
            if (num not in randomNumbers):
                randomNumbers.append(num)
        else:
            randomNumbers.append(num)
    return randomNumbers

def saveToFile(generatedRandomNumber, filename):
    f = open(filename,"w+")
    output = " "
    output = output.join([str(elem) for elem in generatedRandomNumber])
    f.write(output)
    f.close()

def insertionSort(generatedRandomArray): 
    # Traverse through 1 to len(generatedRandomArray) 
    for i in range(1, len(generatedRandomArray)): 
        key = generatedRandomArray[i] 
        # Move elements of generatedRandomArray[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < generatedRandomArray[j] : 
                generatedRandomArray[j+1] = generatedRandomArray[j] 
                j -= 1
        generatedRandomArray[j+1] = key 
    return generatedRandomArray

def partition(generatedRandomArray,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = generatedRandomArray[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   generatedRandomArray[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            generatedRandomArray[i],generatedRandomArray[j] = generatedRandomArray[j],generatedRandomArray[i] 
  
    generatedRandomArray[i+1],generatedRandomArray[high] = generatedRandomArray[high],generatedRandomArray[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# generatedRandomArray[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(generatedRandomArray,low,high): 
    if low < high: 
  
        # pi is partitioning index, generatedRandomArray[p] is now 
        # at right place 
        pi = partition(generatedRandomArray,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(generatedRandomArray, low, pi-1) 
        quickSort(generatedRandomArray, pi+1, high)   
    return generatedRandomArray



    
    
