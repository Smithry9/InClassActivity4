#wordCount.py

def numWords(inputString):
    words = 1
    if(type(inputString) is str):
        if(inputString == ""):
            return 0
        for i in inputString:
            if i == " ":
                words += 1
        return words
    else:
        return "Not a valid string"



