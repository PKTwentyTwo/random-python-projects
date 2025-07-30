# Sudoku Solver
A basic program that can solve Sudoku puzzles in a fraction of a second.
## How to use
Open infile.txt and enter your puzzle in a nine-row format like this:

230497080
095006407
060580012
078304009
040000050
002819370
086200000
000070000
700031065

Zeroes represent blank squares, and numbers represent filled in squares.
Then run the script, solver.py, and its output will resemble the following:

Succeeded in 3 iterations and 0.0588 seconds.
Solved without trial and error!
231497586
895126437
467583912
178354629
943762158
652819374
386245791
519678243
724931865

The first line tells you how many iterations of the algorithm were used and how long it took, the second tells you whether or not the program resorted to trial and error, and the third through eleventh represent the program's solution.

## How it works
The main loop can be summarised in pseudocode as the following:
While the puzzle is not solved:
	Apply basic logic to determine possibilities for each square
	If there is only one possibility for a square, fill it in.
	Apply semi-advanced logic, determining where a number can be in a row, column, or 3x3 square.
	If there is only one possibility, fill it in.
	If there is a contradiction:
		Load the most recent saved grid.
	If no progress has been made:
		Save a copy of the grid, if no saving has been done at all.
		Select a random unknown square.
		Fill in a random number from the list of possibilities for that square.

The trial and error involves a depth first approach, reverting back to before any is attempted if it goes wrong. Selecting a random value succeeds more than 11% of the time on average (because there are only 9 possible values, and it is usually selecting from <9 values), but the random approach has no regard for how much information can be gained from a guess and does not keep track of errors, so it can take hundreds of iterations for the hardest puzzles, but this still typically takes less than a second. 
