#test_palindrome
import unittest
import wordCount

class testCaseAdd(unittest.TestCase):
    #1 word
    def test_wordCount1(self):
        self.assertEqual(wordCount.numWords("Hi"), 1)
    #2 words
    def test_wordCount2(self):
        self.assertEqual(wordCount.numWords("Hello World!"), 2)
    #empty string
    def test_wordCount3(self):
        self.assertEqual(wordCount.numWords(""), 0)
    #invalid input
    def test_wordCount4(self):
        self.assertEqual(wordCount.numWords(10), "Not a valid string")
    #intentionally incorrect test, should fail
    def test_wordCount5(self):
        self.assertEqual(wordCount.numWords("Hello World!"), 5)


if __name__ == "__main__":
    unittest.main()
