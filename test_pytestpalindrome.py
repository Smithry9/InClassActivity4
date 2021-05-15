import pytest
import palindrome

#normal palindrome test
def test_palindrome1():
    assert palindrome.isPalindrome("racecar") == True
#palindrome with numbers
def test_palindrome2():
    assert palindrome.isPalindrome("12321") == True
#not a palindrome
def test_palindrome3():
    assert palindrome.isPalindrome("Hello World!") == False
#invalid input
def test_palindrome4():
    assert palindrome.isPalindrome(10) == "Not a valid string"
#intentionally incorrect test, should fail
def test_palindrome5():
    assert palindrome.isPalindrome("Hello World!") == True


#if __name__ == "__main__":
#    test_palindrome1()
#    test_palindrome2()
#    test_palindrome3()
#    test_palindrome4()
#    test_palindrome5()
