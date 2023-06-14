import unittest
from translator import english_to_french,french_to_english

class test_translator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('blue'), 'bleu')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('bleu'), 'blue')

unittest.main()