#JNDABD002
#Abdul-Kader Jainoodien
#Program that takes the given file and removes or adds tracer statements where required.
#30 April 2024

def fileHandler(fileName: str, mode="r", content: list[str]=[])->list[str]:
    """Handles all file operations. Opens the specified file and reads its contents where required.
    Otherwise the content is written to the specified file.
    It is assumed that the given file exists."""
    fileToTrace=open(fileName, mode)
    #We read or write depending on the mode.
    if mode=="r": content=fileToTrace.readlines()
    else: fileToTrace.writelines(content)
    fileToTrace.close()
    return content #Content is always returned, but can be ignored when writing to file.

def tracerHandler(originalList: list[str]):
    """Handles the addition or removal of tracer elements from a list of sting lines.
    The list presumably comes from a file."""
    outputList=[]
    originalLines=len(originalList)
    traceRemoving=False #A flag to check if tracing must be added or removed. Added is default.
    for lineIndex in range(originalLines):
        #We check if the first line has tracing elements. If yes, we remove tracing only.
        if '"""DEBUG"""' in originalList[lineIndex] and (lineIndex==0 or traceRemoving):
            traceRemoving=True
            continue
        #If the first line had no tracing, we add tracing only.
        if lineIndex==0:
            outputList=['"""DEBUG"""\n']
        #If the previous line had the keyword for a new function.
        if "def " in originalList[lineIndex-1] and not traceRemoving:
                whiteSpace="" #This is a string that will comprise the whitespaces.
                #The name of the function must be added to the tracing element.
                functionName=originalList[lineIndex-1][4:]#We take the line after "def "
                functionName=functionName[:functionName.find("(")]#And end where "(" is found
                #Check if every character is a space or tab space (ascii value 9)
                for character in originalList[lineIndex]:
                    #Adds the white space to the start string.
                    if character==" " or character==chr(9):
                        whiteSpace+=character
                    else: break
                #We add this tracing to the output list.
                #The function name is stripped in the event spaces were added.
                outputList.append(f'{whiteSpace}"""DEBUG""";print(\'{functionName.strip()}\')\n')
        #We add the current line, even after the tracing was added. Skipped if tracing to be removed.
        outputList.append(originalList[lineIndex])
    #We return the list with the modified tracing state, alongside if tracing was added ore removed.
    return outputList, traceRemoving


def main():
    """The main function for tracer, taking the input file name and showing all the outputs."""
    print("***** Program Trace Utility *****")
    fileName=input("Enter the name of the program file:\n")
    originalFileList=fileHandler(fileName)#Gets the content of the file.
    outputFileList, tracesFound=tracerHandler(originalFileList)#Tracing modified
    #Output to display if tracing was added or removed.
    if tracesFound:print("Program contains trace statements\nRemoving...Done")
    else:print("Inserting...Done")
    fileHandler(fileName, "w", outputFileList)#Overwrites the file with the modified tracing.

if __name__=="__main__":
    main()