from sudoku_solver import SudokuSolver

for file_name in ['easy.csv', 'hard.csv', 'worlds_most_difficult.csv']:
    sudoku_solver = SudokuSolver('easy.csv')

    success = sudoku_solver.attempt_solve()

    if success:
        print('Found solution to the Sudoku in:', file_name)
        for row in sudoku_solver.get_grid():
            print(row)
        print()
    else:
        print('There is no solution to the Sudoku in:', file_name)
        print()

pass
