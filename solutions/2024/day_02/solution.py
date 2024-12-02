# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        result = 0
        for line in self.input:
            numbers = line.split(" ")
            numbers = [int(x) for x in numbers]

            if self.check_sub_number_array(numbers):
                result += 1

        return result

    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        for line in self.input:
            numbers = line.split(" ")
            numbers = [int(x) for x in numbers]
            if self.check_sub_number_array(numbers):
                result += 1
            else:
                for i in range(len(numbers)):
                    if self.check_sub_number_array(numbers[:i] + numbers[i + 1 :]):
                        result += 1
                        break
        return result

    def check_sub_number_array(self, numbers):
        increase = True
        for i, n in enumerate(numbers):
            if i == 0:
                continue
            if i == 1:
                if numbers[i] < numbers[i - 1]:
                    increase = False

            if (
                abs(numbers[i] - numbers[i - 1]) > 3
                or abs(numbers[i] - numbers[i - 1]) < 1
            ):
                return False

            if increase == False and numbers[i] > numbers[i - 1]:
                return False

            if increase == True and numbers[i] < numbers[i - 1]:
                return False
        return True

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
