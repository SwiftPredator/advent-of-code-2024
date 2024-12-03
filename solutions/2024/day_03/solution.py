# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import StrSplitSolution, answer, TextSolution
import re


class Solution(TextSolution):
    _year = 2024
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        result = 0
        x = re.findall("mul\((\d+),(\d+)\)", self.input)
        print(x)
        for m in x:
            n1, n2 = int(m[0]), int(m[1])
            result += n1 * n2

        return result

    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        x = re.findall("mul\((\d+),(\d+)\)", self.input)
        poses_mul = [
            (m.start(0), m.end(0))
            for m in re.finditer("mul\((\d+),(\d+)\)", self.input)
        ]
        poses_do = [(m.start(0), m.end(0)) for m in re.finditer("do()", self.input)]
        poses_ndo = [(m.start(0), m.end(0)) for m in re.finditer("don't()", self.input)]

        for pm, numbers in zip(poses_mul, x):
            first_index = pm[0]
            curr_diff = 10000
            should_do = False
            for pnd in poses_ndo:
                if first_index - pnd[1] < curr_diff and first_index - pnd[1] > 0:
                    curr_diff = first_index - pnd[1]
            for pd in poses_do:
                if first_index - pd[1] < curr_diff and first_index - pd[1] > 0:
                    should_do = True
            if should_do == True or curr_diff == 10000:
                result += int(numbers[0]) * int(numbers[1])

        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
