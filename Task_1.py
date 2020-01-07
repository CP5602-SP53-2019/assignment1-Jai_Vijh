import time
import main

def executeTestCase(lowerLimit, upperLimit, numOfValues, noDuplicates, fileName, testName):

    print(testName+'\t',end='')

    #PRINT TEST CASE:
    print(lowerLimit,'\t',end='')
    print(upperLimit,'\t',end='')
    if (numOfValues < 1000000):
        print(numOfValues,'\t\t',end='')
    else:
        print(numOfValues,'\t',end='')
    print(noDuplicates,'\t',end='')

    #TIME TAKEN TO GENERATE NUMBERS.
    startTime = time.process_time()
    numbers = main.rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)    
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

    #TEST A1.
    testA = 1
    lowerLimit = -35500
    upperLimit = 36600
    numOfValues = 50000
    noDuplicates = False
    fileName = "test_a1.txt"

    print("TEST\tlLimit\tULimit\tvalues\t\tnoDups\tGenerateTime\tSaveTime")

    #TESTS An

    i = 0
    testNumber = 1
    while numOfValues <= 80000:
        output += executeTestCase(lowerLimit,
                    upperLimit,
                    numOfValues,
                    noDuplicates,
                    fileName,
                    "A"+str(testNumber)) + '\n'
        testNumber = testA + i + 1;
        numOfValues += int(30000 / num) 
        lowerLimit += int(21700 / num)
        upperLimit += int(60200 / num)
        fileName = "test_a"+str(testNumber)+".txt"
        i += 1

    #TEST B1.
    testB = 1
    lowerLimit = -35500
    upperLimit = 36600
    numOfValues = 50000
    noDuplicates = True
    fileName = "test_b1.txt"


    #TESTS Bn
    i = 0
    testNumber = 1
    while numOfValues <= 80000:
        output += executeTestCase(lowerLimit,
                    upperLimit,
                    numOfValues,
                    noDuplicates,
                    fileName,
                    "B"+str(testNumber)) + '\n'
        testNumber = testB + i + 1;
        numOfValues += int(30000 / num) 
        lowerLimit += int(21700 / num)
        upperLimit += int(60200 / num)
        fileName = "test_b"+str(testNumber)+".txt"
        i += 1

    #SAVE CSV
    f = open('data.csv','w+')
    f.write(output)
    f.close()
        
    
