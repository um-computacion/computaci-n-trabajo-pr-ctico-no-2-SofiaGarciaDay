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

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Allí va Ramón y no maravilla"))
        self.assertTrue(is_palindrome("Alí tomó tila"))
        self.assertTrue(is_palindrome("Ana la galana"))
        self.assertTrue(is_palindrome("Allí ves Sevilla"))
        self.assertTrue(is_palindrome("Amor a Roma"))
        self.assertTrue(is_palindrome("Ella te dará detalle"))
        self.assertTrue(is_palindrome("Ese bello sol le besé"))
        self.assertTrue(is_palindrome("La ruta natural"))
        self.assertTrue(is_palindrome("La moral, claro, mal"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("caballo"))
        self.assertFalse(is_palindrome("princesa"))
        self.assertFalse(is_palindrome("castillo"))
        self.assertFalse(is_palindrome("animal"))
        self.assertFalse(is_palindrome("flor"))
        self.assertFalse(is_palindrome("maquillaje"))
        self.assertFalse(is_palindrome("chile"))
        self.assertFalse(is_palindrome("cafe"))
        self.assertFalse(is_palindrome("churro"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("12321")) 
        self.assertFalse(is_palindrome("123a321")) 

if __name__ == '__main__':
    unittest.main()