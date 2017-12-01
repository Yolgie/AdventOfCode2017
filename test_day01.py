import unittest
from day01 import process

# class day0101Tests(unittest.TestCase):
#     def test_sunshine(self):
#         self.assertEqual(process("1122"), 3)
#
#     def test_all_same(self):
#         self.assertEqual(process("1111"), 4)
#
#     def test_all_different(self):
#         self.assertEqual(process("1234"), 0)
#
#     def test_wrap_around(self):
#         self.assertEqual(process("91212129"), 9)

class day0102Tests(unittest.TestCase):
    def test_sunshine(self):
        self.assertEqual(process("123425"), 4)
        self.assertEqual(process("12131415"), 4)

    def test_all_same(self):
        self.assertEqual(process("123123"), 12)
        self.assertEqual(process("1212"), 6)

    def test_all_different(self):
        self.assertEqual(process("1221"), 0)
