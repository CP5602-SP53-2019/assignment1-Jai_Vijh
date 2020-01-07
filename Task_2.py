import time
import main

def executeTestCase(lowerLimit, upperLimit, numOfValues, sortType, fileName, testName):

    print(testName+'\t',end='')

    #PRINT TEST CASE:
    print(lowerLimit,'\t',end='')
    print(upperLimit,'\t',end='')
    if (numOfValues < 1000000):
        print(numOfValues,'\t\t',end='')
    else:
        print(numOfValues,'\t',end='')

    numbers = main.rNGenerator(lowerLimit, upperLimit, numOfValues, False)

    #TIME TAKEN TO GENERATE NUMBERS.
    startTime = time.process_time()
    if (sortType == 1):
        main.insertionSort(numbers)
    else:
        main.quickSort(numbers,0,numOfValues-1)
    endTime = time.process_time()
    elapsedTime1 = endTime - startTime
    print(format(elapsedTime1, '.6f'),'\t',end='')

    #TIME TAKEN TO SAVE VALUES TO FILE.
    startTime = time.process_time()
    main.saveToFile(numbers, fileName)
    endTime = time.process_time()
    elapsedTime2 = endTime - startTime
    print(format(elapsedTime2, '.6f'),end='')
    print()

    return testName + ',' + str(lowerLimit) +','+ str(upperLimit) +',' + str(numOfValues) + ',' + format(elapsedTime1, '.6f') + ',' + format(elapsedTime2, '.6f')




if __name__ == '__main__':

    
    num = int(input('Enter maxiumum number of test cases: '))
    output = '';

    #CREATING TEST CASES.

    #TEST C1.
    testC = 1
    lowerLimit = -35500
    upperLimit = 36600
    numOfValues = 50000
    fileName = "test_a1.txt"

    print("TEST\tlLimit\tULimit\tvalues\t\tSortTime\tSaveTime")
    
    

    #TESTS Cn
    i = 0
    testNumber = 1
    while numOfValues <= 80000:
        output += executeTestCase(lowerLimit,
                    upperLimit,
                    numOfValues,
                    1,
                    fileName,
                    "C"+str(testNumber)) + '\n'
        testNumber = testC + i + 1;
        numOfValues += int(30000 / num) 
        lowerLimit += int(21700 / num)
        upperLimit += int(60200 / num)
        fileName = "test_b"+str(testNumber)+".txt"
        i += 1

    #TEST D1.
    testD = 1
    lowerLimit = -35500
    upperLimit = 36600
    numOfValues = 50000
    fileName = "test_d1.txt"
    

    #TESTS Dn
    i = 0
    testNumber = 1
    while numOfValues <= 80000:
        output += executeTestCase(lowerLimit,
                    upperLimit,
                    numOfValues,
                    2,
                    fileName,
                    "D"+str(testNumber)) + '\n'
        testNumber = testD + i + 1;
        numOfValues += int(30000 / num) 
        lowerLimit += int(21700 / num)
        upperLimit += int(60200 / num)
        fileName = "test_d"+str(testNumber)+".txt"
        i += 1

    #SAVE CSV
    f = open('data2.csv','w+')
    f.write(output)
    f.close()
        
    
