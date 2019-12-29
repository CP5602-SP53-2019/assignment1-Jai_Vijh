import random
import time
import matplotlib.pyplot as plt

def rNGenerator(lowerLimit, upperLimit, numberOfValues, noDuplicates):
    result = [random.randrange(lowerLimit,upperLimit) for i in range(0,numberOfValues)]
    result = list(set(result)) if noDuplicates else result
    return result
    
def saveToFile(generatedRandomNumber, filename, write_or_app):
    file = open(filename, write_or_app)
    file.write(str(generatedRandomNumber))
    file.close()
    return True

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

def main():
    no_of_tests = int(input())
    test_cases = [list(input().split()) for i in range(no_of_tests)]
    time_for_each_save = {}
    time_for_ins_sort = {}
    time_for_q_sort = {}
    for index,case in enumerate(test_cases):
        lowerLimit, upperLimit, numberOfValues = [int(l) for l in case[0:3]]
        t0 = time.time()
        res = (rNGenerator(lowerLimit, upperLimit, numberOfValues, case[3]))
        saveToFile(res,'result-text-file.txt', 'w+')
        t1 = time.time()
        time_for_each_save[index] = t1 - t0
        
        t0 = time.time()
        insertion_sorted_array = insertionSort(res)
        saveToFile(insertion_sorted_array,'result-text-file.txt','a')
        t1 = time.time()
        time_for_ins_sort[index] = t1 - t0

        t0 = time.time()
        quick_sorted_array = quickSort(res,0,len(res)-1)
        saveToFile(quick_sorted_array,'result-text-file.txt','a')
        t1 = time.time()
        time_for_q_sort[index] = t1 - t0

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.bar(range(len(time_for_each_save)), list(time_for_each_save.values()))
    ax1.set_xticks(range(len(time_for_each_save)), list(time_for_each_save.keys()))
    ax1.set_title('Gen and Save')

    ax2.bar(range(len(time_for_ins_sort)), list(time_for_ins_sort.values()))
    ax2.set_title('Insertion Sort')
    ax2.set_xticks(range(len(time_for_ins_sort)), list(time_for_ins_sort.keys()))

    ax3.bar(range(len(time_for_q_sort)), list(time_for_q_sort.values()))
    ax3.set_title('Quick Sort')
    ax3.set_xticks(range(len(time_for_q_sort)), list(time_for_q_sort.keys()))

    plt.show()
    return True

if __name__ == '__main__':
    main()