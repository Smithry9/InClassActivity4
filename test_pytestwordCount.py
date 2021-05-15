import pytest
import wordCount

#1 word
def test_wordCount1():
    assert wordCount.numWords("Hi") == 1
#2 words
def test_wordCount2():
    assert wordCount.numWords("Hello World!") == 2
#empty string
def test_wordCount3():
    assert wordCount.numWords("") == 0
#invalid input
def test_wordCount4():
    assert wordCount.numWords(10) == "Not a valid string"
#intentionally incorrect test, should fail
def test_wordCount5():
    assert wordCount.numWords("Hello World!") == 5
