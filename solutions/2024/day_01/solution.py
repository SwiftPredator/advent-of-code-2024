# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        list_1, list_2 = sorted([int(i.split("  ")[0]) for i in self.input]), sorted(
            [int(i.split("  ")[1]) for i in self.input]
        )
        result = sum([abs(a_i - b_i) for a_i, b_i in zip(list_1, list_2)])
        return result

    # @answer(1234)
    def part_2(self) -> int:
        list_1, list_2 = [int(i.split("  ")[0]) for i in self.input], [
            int(i.split("  ")[1]) for i in self.input
        ]
        result = 0
        for n in list_1:
            count = list_2.count(n)
            result += n * count

        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
