from time_manager import time_finder #import the time finder function

def count(textFilePath):
    wordsCount = 0

    #Read the file and count the words
    try:
        with open(textFilePath, 'r') as textFile:
            lines = textFile.readlines()
            for line in lines:
                words = line.split()
                wordsCount += len(words)

        #Append the file and time counted to the file
        with open(textFilePath, 'a') as textFile:
            textFile.write(f"\nAmount of words: {wordsCount} {time_finder()}")

        print(f"\nAmount of words: {wordsCount}\n")
    except:
        count(input("\nInvalid relative path, what is the relative file path for your document? (needs to be in the project files)\nChoice: "))