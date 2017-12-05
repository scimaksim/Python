import words

import unittest


class TestWords(unittest.TestCase):
    def test_longest(self):
        """ test the longest function """
        # Missing code goes here
        self.assertEqual(words.longest('hi', 'hello', 'python'), 'python')
        self.assertEqual(words.longest('hi'), 'hi')
        self.assertIsNone(words.longest())
        self.assertIn(words.longest('hi', 'cat', 'hat', 'rat'),
                      {'cat', 'hat', 'rat'})


new_test = TestWords()
new_test.test_longest()





