#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python.calc import Calc


class TestCalc:

    def test_a(self):
        print("aa")
    def test_add_1(self):
        result = Calc().add(1, 2)
        assert 3 == result

    def test_add_2(self):
        result = Calc().add(0.01, 0.02)
        assert 0.03 == result
