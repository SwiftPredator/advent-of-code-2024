# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import copy
from tqdm import tqdm


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    # @answer(1234)
    def part_1(self) -> int:
        self.directions = ["^", ">", "v", "<"]
        self.dir_x = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 1
        field = [list(x) for x in self.input]
        while True:
            pos_y, pos_x, dir, sym = self.find_pos(field)
            if pos_y == "end" or pos_x == "end":
                break
            if field[pos_y + dir[0]][pos_x + dir[1]] == "#":
                field[pos_y][pos_x] = self.directions[
                    (
                        self.directions.index(sym) + 1
                        if self.directions.index(sym) < len(self.directions) - 1
                        else 0
                    )
                ]
                continue
            if field[pos_y + dir[0]][pos_x + dir[1]] != "X":
                result += 1
            field[pos_y + dir[0]][pos_x + dir[1]] = sym
            field[pos_y][pos_x] = "X"

        return result

    def find_pos(self, field):
        for i in range(len(field)):
            if "^" in field[i]:
                if i - 1 < 0:
                    return "end", "", "", ""
                return i, field[i].index("^"), (-1, 0), "^"
            if ">" in field[i]:
                j = field[i].index(">")
                if j + 1 >= len(field[i]):
                    return "end", "", "", ""
                return i, field[i].index(">"), (0, 1), ">"
            if "<" in field[i]:
                j = field[i].index("<")
                if j - 1 < 0:
                    return "end", "", "", ""
                return i, field[i].index("<"), (0, -1), "<"
            if "v" in field[i]:
                if i + 1 >= len(field):
                    return "end", "", "", ""
                return i, field[i].index("v"), (1, 0), "v"

    # @answer(1234)
    def part_2(self) -> int:
        self.directions = ["^", ">", "v", "<"]
        self.dir_x = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 0
        field = [list(x) for x in self.input]
        sy, sx, _, sym = self.find_pos(field)
        for i in tqdm(range(len(field))):
            for j in range(len(field[0])):
                if (i, j) == (sy, sx) or field[i][j] == "#":
                    continue

                field[i][j] = "#"
                if self.check_loop(field, sy, sx):
                    result += 1
                field[i][j] = "."

        return result

    def check_loop(self, field, sy, sx):
        pos_dict = set()
        d = 0
        height = len(field)
        width = len(field[0])
        while True:
            dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            syy = sy + dxy[0]
            sxx = sx + dxy[1]
            if not (0 <= syy < height and 0 <= sxx < width):
                break
            if field[syy][sxx] == "#":
                d = (d + 1) % 4
                continue

            if (sy, sx, d) in pos_dict:
                return True

            pos_dict.add((sy, sx, d))
            sy = syy
            sx = sxx

        return False

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
