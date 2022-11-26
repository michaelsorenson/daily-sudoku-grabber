cd /home/pi/daily-sudoku-grabber
git pull origin master
python3 dailySudokuGrabber.py
pdflatex ang_mon_sudoku_puzzle.tex
pdflatex gma_sudoku_puzzle.tex
pdflatex gma_friend_sudoku_puzzle.tex
pdflatex gpa_sudoku_puzzle.tex
#lp ang_mon_sudoku_puzzle.pdf
lp gma_sudoku_puzzle.pdf
#lp gpa_sudoku_puzzle.pdf
lp gma_friend_sudoku_puzzle.pdf
rm *sudoku_puzzle.*
