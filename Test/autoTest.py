import subprocess
import os
import time
import re

from subprocess import Popen, PIPE


def processVectorFile(fileName):

    ins =[]
    headerList = []

    #  Process Test File Vectors.in

    with open(fileName,"r") as f1:
        
        firstLine = f1.readline()
        headerList = firstLine.split()
        
        for test in f1:

            if "#" in test:
                #Ignore Comments
                pass
            else:
                
                values = test.split()
                
                
                temp = {}

                for i,header in enumerate(headerList):
                    entry = {header: values[i]}
                    temp.update(entry)
                
                ins.append(temp)

    return ins, headerList        

               
def convertFileFormat(inputCases, newFileName,isInput=True):
    # Convert to expected file format
    seq  = []
    for test in inputCases:
            testIn = ""
            
            for key,value in test.items():
                value = value.lower()
                if value == "false":
                    continue
                elif value == "true":
                    testIn += (key+" ")
                    
                else:
                    testIn += key+"("+value+") "

            if isInput:
                testIn += ";"
        
            seq.append(testIn)

    with open(newFileName, "w+") as f2:
        for line in seq:
            f2.write(line+"\n")


def getProgramOutputList(stdoutConsole, outputHeaderList):
    consoleOutputList = []
    programOutputList = []

    outputString = (stdoutConsole.decode('utf-8'))
    arrayConsole = outputString.split("\n")

    for s in arrayConsole:
        # Index 1 onwards for each entry inside and put Key "outputName" for outputList 
        index = s.find("Output:")
        lastIndex = s.find(":", index)
        
        if index > 0:
            consoleOutputList.append(s[(lastIndex+1):-1].split())

   
    
    for i, signalList in enumerate(consoleOutputList):
        tmpValDict = {}

    
        if len(signalList) == 0:
            
            for headerName in outputHeaderList:
                tmpValDict.update({headerName:"Missing"})
                
        else:

            for signal in signalList:
                
                for signalName in outputHeaderList:
                    
                    tmpHeader = re.search(re.escape(signalName), signal)
                    
                    if tmpHeader:
                        missingKey = None
                        key = tmpHeader[0]
                        tmpVal = re.search(r'[\d\.\d]+', signal)

                        if tmpVal:

                            val = tmpVal[0]
                            
                        else:
                            val = "-*-"

                        tmp = {key  : val}
                        tmpValDict.update(tmp)
                        
                        break
                    else:
                        missingKey = signalName

                else:
                    if missingKey != None:
                        tmp = {missingKey  : "Missing"}
                        tmpValDict.update(tmp)

                
        programOutputList.append(tmpValDict)  

    return programOutputList

# 2 Options Press 1 to feed one by one, 2 to run whole test script
def fullTest(newFileName,outputFileName,desiredOutputFile):
    isFail = False
    testCnt = 1
    inputStream= ""

    expectedOutputList, outputHeaderList = processVectorFile(outputFileName)
    convertFileFormat(expectedOutputList, desiredOutputFile,isInput=False)
    
    workingDir = os.getcwd()
    p = subprocess.Popen(['./cruise'], stdin=PIPE, stdout=PIPE)


    with open(newFileName,"r")as f1:
    
        for line in f1:
            inputStream += line
            

    stdout, err = p.communicate(inputStream.encode('utf-8'))

    programOutputList = getProgramOutputList(stdout, outputHeaderList)

    latchValues = {}
    for header in outputHeaderList:
        latchValues[header] = None

    for i, entry in enumerate(programOutputList):
        
    
        for headerName in outputHeaderList:
            if (headerName in programOutputList[i]):
                latchValues[headerName] = programOutputList[i][headerName]

            if (latchValues[headerName] != expectedOutputList[i][headerName]):
                isFail = True
                    
        if isFail:
            print(("\033[1;31;40m Failed! Test # {}".format(testCnt)))
            print("\033[1;37;40m Expected Outputs: " + str(expectedOutputList[i]))
            print("\033[1;31;40m Actual Outputs: "+ str(latchValues) + '\n\n')
            break
        else:
            print("\033[1;32;40m Passed! Test #"+ str(testCnt))
            print("\033[1;37;40m Outputs: "+ str(latchValues) + '\n')
            testCnt += 1

    return p

def Test(fileName,newFileName,outputFileName,desiredOutputFile):
    # Get input from user if =1 one by one test, if 2 full test
    user = input("Press 1 for Interactive, 2 for All Test: ")
    print(user)
    inputList, inputHeaderList = processVectorFile(fileName)
    convertFileFormat(inputList, newFileName)
    # Find the expected outputs
   
    if user =="1":
        print("\033[1;37;40m #INTERACTIVE MODE\n")
        from subprocess import Popen, PIPE
        import os
        import time
        import sys

        workingDir = os.getcwd()
        p = subprocess.Popen(['./cruise'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        c=""
        output = []

        with open(newFileName,"r")as f1:
            allLines= f1.readlines()


        userInput = input("Press Enter to continue or q to exit:\n\n ")
        lineNo =1
        while (userInput != "q" and lineNo< len(allLines) ):
            
            if  userInput == "":
               
               
                c = allLines[lineNo-1]
                p.stdin.write(c.encode('utf-8'))
                
                p.stdin.flush()
                
                lineNo+=1
                
                userInput = input("Press Enter again to continue or q to exit:\n") 

               
                for line in p.stdout:
                    
                    line = line.decode('utf-8')

                    # print(line)

                    index = line.find("Output:") 
                    if (index>-1):
                        output.append(line[index:-1].split())
                        
                        print(str(line[index:-1].split()) + '\n\n')
                        # Compare to the desired output
                        # If matching say yes, if not say no

                        p.stdout.flush()

                        break

            else:
                continue
        print("\n\n\033[1;37;40m #INTERACTIVE MODE END")
                    
    elif user =="2":
        p = fullTest(newFileName,outputFileName,desiredOutputFile)
        print("\033[1;37;40m TESTS FINISHED")

    return p




fileName = "vectors.in"
newFileName = "inputSignals.txt" 
outputFileName = "vectors.out"
newOutputFileName = "expectedOutputs.txt" 
p = Test(fileName,newFileName,outputFileName,newOutputFileName)

time.sleep(2)
p.kill()