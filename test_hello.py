"""Test suite for hello.py — TDD 第19课演示"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from hello import fibonacci, factorial, is_even

import pytest

# ====== 新功能 TDD: fibonacci ======

class TestFibonacci:
    """fibonacci(n) 返回第 n 个斐波那契数"""

    def test_fibonacci_0_returns_0(self):
        """fib(0) = 0"""
        assert fibonacci(0) == 0

    def test_fibonacci_1_returns_1(self):
        """fib(1) = 1"""
        assert fibonacci(1) == 1

    def test_fibonacci_2_returns_1(self):
        """fib(2) = 1"""
        assert fibonacci(2) == 1

    def test_fibonacci_5_returns_5(self):
        """fib(5) = 5"""
        assert fibonacci(5) == 5

    def test_fibonacci_10_returns_55(self):
        """fib(10) = 55"""
        assert fibonacci(10) == 55

    def test_fibonacci_negative_returns_0(self):
        """负数输入返回 0"""
        assert fibonacci(-1) == 0

    def test_fibonacci_large(self):
        """fib(20) = 6765"""
        assert fibonacci(20) == 6765


# ====== 已有功能验证 ======

class TestFactorial:
    def test_factorial_5(self):
        assert factorial(5) == 120

    def test_factorial_0(self):
        assert factorial(0) == 1

    def test_factorial_negative(self):
        assert factorial(-1) == 0

class TestIsEven:
    def test_even(self):
        assert is_even(42) == True

    def test_odd(self):
        assert is_even(7) == False
