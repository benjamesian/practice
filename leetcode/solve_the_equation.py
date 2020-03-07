#!/usr/bin/env python3
"""Basic arithmetic checker."""
import re


class Solution:
    """https://leetcode.com/problems/solve-the-equation/"""

    def solveEquation(self, equation: str) -> str:
        """Solve for x."""
        lhs, rhs = equation.split('=')

        def helper(expression) -> (int, int):
            splt = re.split(r'([-+]?[0-9]*x)|([-+]?[0-9]*)', expression)
            num_xs = 0
            value = 0
            for expr in splt:
                if not expr:
                    continue
                if expr == '-x':
                    num_xs -= 1
                elif expr in {'+x', 'x'}:
                    num_xs += 1
                elif 'x' in expr:
                    num_xs += int(expr[:-1])
                else:
                    value += int(expr)
            return (num_xs, value)

        left_xs, left_value = helper(lhs)
        right_xs, right_value = helper(rhs)

        total_xs = left_xs - right_xs
        total = right_value - left_value

        if total_xs == 0:
            return "Infinite solutions" if total == 0 else "No solution"

        return f"x={total // total_xs}"
