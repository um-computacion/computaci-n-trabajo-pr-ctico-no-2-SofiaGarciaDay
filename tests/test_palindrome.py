import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("ana"))
        self.assertTrue(is_palindrome("aibofobia"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("salas"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("ojo"))
        self.assertTrue(is_palindrome("arenera"))
        self.assertTrue(is_palindrome("menem"))
        self.assertTrue(is_palindrome("reconocer"))

if __name__ == '__main__':
    unittest.main()