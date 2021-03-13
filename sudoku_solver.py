import copy

class SudokuSolver:
    def __init__(self, file_name):
        if file_name == None:
            self._grid = [[None for col in range(9)] for row in range(9)]
        else:
            self._grid = []
            f = open(file_name, 'r')
            for line in f.read().splitlines():
                self._grid.append([int(x) if int(x) != 0 else None for x in line.split('\t')])

    def _is_valid(self):
        # check no duplicates in rows
        for row in range(9):
            values_found = set()
            for col in range(9):
                value = self._grid[row][col]
                if value == None:
                    continue
                if value in values_found:
                    return False
                values_found |= {value}
        # check no duplicates in cols
        for col in range(9):
            values_found = set()
            for row in range(9):
                value = self._grid[row][col]
                if value == None:
                    continue
                if value in values_found:
                    return False
                values_found |= {value}
        # check no duplicates in boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values_found = set()
                for row_offset in range(3):
                    for col_offset in range(3):
                        value = self._grid[box_row + row_offset][box_col + col_offset]
                        if value == None:
                            continue
                        if value in values_found:
                            return False
                        values_found |= {value}
        return True

    # back-tracking algorithm
    def attempt_solve(self):
        if not self._is_valid():
            return False
        for row in range(9):
            for col in range(9):
                if self._grid[row][col] == None:
                    for n in range(1, 10):
                        self._grid[row][col] = n
                        # recursive call here:
                        success = self.attempt_solve()
                        if success:
                            # our child call found a solution, so bubble success without touching grid
                            return True
                    # we tried all values with no success, so there is an error in a parent call
                    self._grid[row][col] = None
                    return False
        # the Sudoku is valid, and none of the cells are blank, so we solved it
        return True

    def get_grid(self):
        return copy.deepcopy(self._grid)
