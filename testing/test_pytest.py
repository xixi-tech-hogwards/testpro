#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pytest + allure
import pytest

import sys

sys.path.append('..')
print(sys.path)
from python.calc import Calc


class TestCal:
    def setup(self):
        self.calc = Calc()

    def test_add_2(self):
        result = self.calc.add(0.01, 0.02)
        assert 0.03 == result

    def test_add_1(self):
        result = self.calc.add(1, 2)
        assert 3 == result

# if __name__ == '__main__':
#     pytest.main(['-vs','test_pytest.py::TestCal::test_add_1'])
