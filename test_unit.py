import unittest
import textwrap

from text_wrap import text_break


class Test(unittest.TestCase):

    def testCase(self):
         textwrap.TextWrapper(13, break_long_words=True)
         test = "Four score and seven years ago our fathers brought forth upon this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal."
         splitted = text_break(test)
         excepted = ['Four score', 'and seven', 'years ago our', 'fathers', 'brought forth', 'upon this', 'continent a',
                     'new nation,', 'conceived in', 'liberty and', 'dedicated to', 'the', 'proposition', 'that all men',
                     'are created', 'equal.']
         self.assertEqual(splitted, excepted)
         print(*splitted, sep="\n")




if __name__ == '__main__':
    unittest.main()