# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        result = 0
        rows = len(self.input)
        cols = len(self.input[0])
        target = "XMAS"
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    x, y = i, j
                    valid = True
                    for k in range(len(target)):
                        if (
                            x < 0
                            or x >= rows
                            or y < 0
                            or y >= cols
                            or self.input[x][y] != target[k]
                        ):
                            valid = False
                        x += dx
                        y += dy
                    if valid:
                        result += 1

        return result

    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        rows = len(self.input)
        cols = len(self.input[0])
        for i in range(rows):
            for j in range(cols):
                if (
                    (
                        self.check_dia(i, j, 1, 1, "MAS", rows, cols)
                        and self.check_dia(i, j + 2, 1, -1, "SAM", rows, cols)
                    )
                    or (
                        self.check_dia(i, j, 1, 1, "SAM", rows, cols)
                        and self.check_dia(i, j + 2, 1, -1, "MAS", rows, cols)
                    )
                    or (
                        self.check_dia(i, j, 1, 1, "MAS", rows, cols)
                        and self.check_dia(i, j + 2, 1, -1, "MAS", rows, cols)
                    )
                    or (
                        self.check_dia(i, j, 1, 1, "SAM", rows, cols)
                        and self.check_dia(i, j + 2, 1, -1, "SAM", rows, cols)
                    )
                ):
                    result += 1
        return result

    def check_dia(self, x, y, dx, dy, target, rows, cols):
        for k in range(len(target)):
            if (
                x < 0
                or x >= rows
                or y < 0
                or y >= cols
                or self.input[x][y] != target[k]
            ):
                return False
            x += dx
            y += dy
        return True

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
