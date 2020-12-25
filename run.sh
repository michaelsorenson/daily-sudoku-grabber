git pull origin master
python dailySudokuGrabber.py
pdflatex puzzle.tex
lp puzzle.pdf -n 2
rm puzzle.*
