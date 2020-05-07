#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# from python.calc import Calc
print(sys.path)
#
# sys.exit()
sys.path.append('..')
from python.calc import Calc
import unittest


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    def test_a(self):
        print("aa")

    def test_add_1(self):
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)

    def test_add_2(self):
        result = self.calc.add(0.01, 0.02)
        self.assertEqual(0.03, result)


unittest.main(verbosity=2)

# unittest + HTMLTestRunner
