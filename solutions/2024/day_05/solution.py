# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    # @answer(1234)
    def part_1(self) -> int:
        result = 0
        splitter_idx = self.input.index("")
        rules, p_orders = self.input[:splitter_idx], self.input[splitter_idx + 1 :]
        rd = [(int(s.split("|")[0]), int(s.split("|")[1])) for s in rules]
        for p_ord in p_orders:
            numbers = [int(i) for i in p_ord.split(",")]
            isvalid = True
            for i, n in enumerate(numbers):
                for p in numbers[i + 1 :]:
                    if not self.check_rule(n, p, rd):
                        isvalid = False
                        break
                if not isvalid:
                    break
            if isvalid:
                result += numbers[int(len(numbers) / 2)]

        return result

    def check_rule(self, pre, post, r):
        return (pre, post) in r

    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        splitter_idx = self.input.index("")
        rules, p_orders = self.input[:splitter_idx], self.input[splitter_idx + 1 :]
        rd = [(int(s.split("|")[0]), int(s.split("|")[1])) for s in rules]
        for p_ord in p_orders:
            numbers = [int(i) for i in p_ord.split(",")]
            t_numbers = [int(i) for i in p_ord.split(",")]
            skip = False
            is_wrong_order = False
            while not skip:
                tskip = True
                i = 0
                j = 1
                while j < len(numbers) and i < len(numbers) - 1:
                    n1, n2 = numbers[i], numbers[j]
                    if not self.check_rule(n1, n2, rd):
                        tn = numbers[i]
                        numbers[i] = numbers[j]
                        numbers[j] = tn
                        tskip = False
                        is_wrong_order = True
                    if j == len(numbers) - 1:
                        i += 1
                        j = i + 1
                    else:
                        j += 1
                        
                if tskip:
                    skip = True

            if is_wrong_order:
                result += numbers[int(len(numbers) / 2)]

        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
