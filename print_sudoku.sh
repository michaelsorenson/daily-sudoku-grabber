cd /home/pi/daily-sudoku-grabber
git pull origin master
python3 dailySudokuGrabber.py
pdflatex gma_sudoku_puzzle.tex
pdflatex gpa_sudoku_puzzle.tex
lp gma_sudoku_puzzle.pdf
lp gpa_sudoku_puzzle.pdf
rm *sudoku_puzzle.*
