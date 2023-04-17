import unittest
from translator import frenchToEnglish, englishToFrench


class testMyModule(unittest.TestCase):
    def test_french_to_english_oui(self):
        self.assertEqual(frenchToEnglish('Oui'), 'Yes')

    def test_french_to_english_no(self):
        self.assertEqual(frenchToEnglish('Non'), 'No')

    def test_french_to_english_null(self):
        self.assertEqual(frenchToEnglish(None), None)


    def test_french_to_english_bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_english_to_french_yes(self):
        self.assertEqual(englishToFrench('Yes'), 'Oui')

    def test_english_to_french_no(self):
        self.assertEqual(englishToFrench('No'), 'Non')

    def test_english_to_french_hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


if __name__ =="__main__":
    unittest.main()





