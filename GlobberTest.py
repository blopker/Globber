#!/usr/bin/env python

from Globber import match
import unittest


class TestGlobber(unittest.TestCase):

    def test_star(self):
        self.assertTrue(match('*', ''))
        self.assertTrue(match('*2*', '123'))
        self.assertTrue(match('*3', '123'))
        self.assertTrue(match('*', 'IOUJHG234*#$^%'))

        self.assertFalse(match('*2', '123'))
        self.assertFalse(match('*b', 'IOUJHG234*#$^%'))

    def test_question_mark(self):
        self.assertTrue(match('?', 'a'))
        self.assertTrue(match('?b', 'ab'))

        self.assertFalse(match('?', 'ab'))
        self.assertFalse(match('g?', 'ab'))

    def test_set(self):
        self.assertTrue(match('[ch]', 'c'))
        self.assertTrue(match('[ch]', 'h'))

        self.assertFalse(match('[ch]', 'g'))
        self.assertFalse(match('[^ch]', 'c'))

    def test_examples(self):
        self.assertTrue(match('bo*awesome', 'bo is awesome'))
        self.assertTrue(match('*.java', 'server.java'))
        self.assertTrue(match('*.java', 'server2.java'))
        self.assertTrue(match('*.[ch]', 'abc.c'))
        self.assertTrue(match('*.[ch]', 'abc.h'))
        self.assertTrue(match('*.?', 'abcd.d'))

        self.assertFalse(match('*.[ch]', 'abc.g'))

if __name__ == '__main__':
    unittest.main()
