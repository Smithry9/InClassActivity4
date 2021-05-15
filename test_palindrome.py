#test_palindrome
import unittest
import palindrome

class testCaseAdd(unittest.TestCase):
    #normal palindrome test
    def test_palindrome1(self):
        self.assertEqual(palindrome.isPalindrome("racecar"), True)
    #palindrome with numbers
    def test_palindrome2(self):
        self.assertEqual(palindrome.isPalindrome("12321"), True)
    #not a palindrome
    def test_palindrome3(self):
        self.assertEqual(palindrome.isPalindrome("Hello World!"), False)
    #invalid input
    def test_palindrome4(self):
        self.assertEqual(palindrome.isPalindrome(10), "Not a valid string")
    #intentionally incorrect test, should fail
    def test_palindrome5(self):
        self.assertEqual(palindrome.isPalindrome("Hello World!"), True)


if __name__ == "__main__":
    unittest.main()
