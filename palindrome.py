#palindrome.py

def isPalindrome(inputString):
    if(type(inputString) is str):
        for i in range(len(inputString)//2):
            if(inputString[i] != inputString[len(inputString)-i-1]):
                return False
        return True
    else:
        return "Not a valid string"

