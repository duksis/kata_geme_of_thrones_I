import unittest

def _uniq(string):
    return ''.join(set(string))

def is_key(key):
    if (len(key) < 1) or (len(key) > pow(10, 6)):
        return 'NO'
    for char in _uniq(key):
        if char not in list('abcdefghijklmnopqrstuvwxyz'):
            return 'NO'

    if sum([key.count(char) % 2 for char in _uniq(key)]) > (len(key) % 2):
        return 'NO'
    return 'YES'

class TestIncorrectInvocation(unittest.TestCase):

    def test_simple_correct_case(self):
        self.assertEqual(is_key('aaabbbb'), 'YES')
        # A palindrome permutation of the given string is bbaaabb.

    def test_simpe_incorrect_case(self):
        self.assertEqual(is_key('cdefghmnopqrstuvw'), 'NO')
        # You can verify that the given string has no palindrome permutation.

    def test_lowercase_character_constraint(self):
        self.assertEqual(is_key('A'), 'NO')

    def test_minimum_size_constraint(self):
        self.assertEqual(is_key(''), 'NO')
        self.assertEqual(is_key('a'), 'YES')

    def test_maximum_size_constraint(self):
        self.assertEqual(is_key('a' * (pow(10,6) + 1)), 'NO')
        self.assertEqual(is_key('a' * (pow(10,6))), 'YES')

if __name__ == '__main__':
    unittest.main()
