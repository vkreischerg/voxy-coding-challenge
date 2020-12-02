import unittest
from .utils import count_words


class TestWordCount(unittest.TestCase):

    def test_empty_string(self):
        fixture = ''
        result = count_words(fixture)
        expected = 0
        self.assertEqual(result, expected)

    def test_right_datatype(self):
        fixture = 'working at Voxy is cool'
        result = count_words(fixture)
        expected = 5
        self.assertEqual(result, expected)

    def test_long_string(self):
        fixture = '''
        This is a somewhat long string 
        with newlines and   tabs. How many words 
        do 

            I have?
        '''
        result = count_words(fixture)
        expected = 16
        self.assertEqual(result, expected)

    def test_input_int(self):
        fixture = 10
        self.assertRaises(TypeError, count_words, fixture)

    def test_input_list(self):
        fixture = ['a', 'b', 'c']
        self.assertRaises(TypeError, count_words, fixture)
