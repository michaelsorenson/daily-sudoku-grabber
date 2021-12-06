import json
from bs4 import BeautifulSoup
from selenium import webdriver
import random


# Taken from https://www.keepinspiring.me/funny-quotes/, modified to be sudoku humor
SOLUTIONS_STRINGS = [
    'Checking your answers is for losers. Does it really matter if your puzzle is correct?',
    'I hope you aren\'t cheating... Just kidding, work smarter not harder',
    'People say sudoku is impossible, but my grandparents do sudoku every day.',
    'Better not to solve the sudoku puzzle and be thought a fool than to attempt it and remove all doubt.',
    'All the things I really like to do are either immoral, illegal or fattening. Or sudoku',
    'At every sudoku puzzle solving session there are two kinds of people – those who want to look at the solutions and those who don’t. The trouble is, they are usually married to each other.',
    'To be sure of hitting the target, shoot first, and call whatever you hit the target.',
    'The world is full of magical things patiently waiting for our wits to grow sharper.',
    'Before you judge a man, walk a mile in his shoes. After that who cares?… He’s a mile away and you’ve got his shoes!',
    'I’ve always wanted to go to Switzerland to see what the army does with those wee red knives.',
    'My favorite machine at the gym is the vending machine.',
    'A stockbroker urged me to buy a stock that would triple its value every year. I told him, \'At my age, I don’t even buy green bananas.\'',
    'It is a scientific fact that your body will not absorb cholesterol if you take it from another person’s plate.',
    'I refuse to solve a sudoku puzzle on the grounds that I don’t know the solution. - Kacey',
    'My grandmother started walking five miles a day when she was sixty. She’s ninety-seven now, and we don’t know where the hell she is.',
    'A computer once beat me at chess, but it was no match for me at kick boxing.',
    'I asked God for a bike, but I know God doesn’t work that way. So I stole a bike and asked for forgiveness.',
    'If you live to be one hundred, you’ve got it made. Very few people die past that age.'
]
def main():
    # get headless browser driver
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    # get todays medium puzzle
    driver.get('https://www.nytimes.com/puzzles/sudoku/easy')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='lxml')
    # get medium puzzle and create latex string
    game = soup.findAll('div', {'class': 'pz-game-screen'})[0].find('script').text
    puzzles = json.loads(game[game.find('{'):game.rfind('}') + 1])
    todays_puzzle = puzzles['easy']['puzzle_data']['puzzle']
    todays_puzzle_solutions = puzzles['easy']['puzzle_data']['solution']
    puzzle_tex_str = puzzle_to_latex(todays_puzzle)
    ang_mon_puzzle_tex_str = get_tex_file_str(puzzle_tex_str, 'Angela/Monica\'s Puzzle \\heart')
    gma_puzzle_tex_str = get_tex_file_str(puzzle_tex_str, 'Grandma\'s Puzzle \\heart')
    gpa_puzzle_tex_str = get_tex_file_str(puzzle_tex_str, 'Grandpa\'s Puzzle \\heart')
    solutions_tex_str = get_tex_file_str(puzzle_to_latex(todays_puzzle_solutions), random.choice(SOLUTIONS_STRINGS))
    # write puzzles to file
    ang_mon_puzzle_file = open("ang_mon_sudoku_puzzle.tex", "w")
    ang_mon_puzzle_file.write(ang_mon_puzzle_tex_str)
    ang_mon_puzzle_file.close()
    gma_puzzle_file = open("gma_sudoku_puzzle.tex", "w")
    gma_puzzle_file.write(gma_puzzle_tex_str)
    gma_puzzle_file.close()
    gpa_puzzle_file = open("gpa_sudoku_puzzle.tex", "w")
    gpa_puzzle_file.write(gpa_puzzle_tex_str)
    gpa_puzzle_file.close()
    # write solutions to file
    solutions_file = open("sudoku_solutions.tex", "w")
    solutions_file.write(solutions_tex_str)
    solutions_file.close()

def puzzle_to_latex(puzzle_data):
    puzzle_str = ''
    for i in range(9):
        for j in range(9):
            cur_entry = puzzle_data[9 * i + j]
            cur_entry = str(cur_entry) if cur_entry != 0 else ' '
            puzzle_str += '|' + cur_entry
        puzzle_str += '|.\n'
    return puzzle_str

def get_tex_file_str(sudoku_string, subtitle):
    return '\\documentclass{article}\n\\usepackage{sudoku}\n\\usepackage{graphicx}\n' +\
    '\\newcommand{\heart}{\ensuremath\heartsuit}\n\\graphicspath{ {./images/} }\n' +\
    '\\title{Michael\'s Sudoku Mania || \\includegraphics{icons/nytimes-icon.png} NYTimes Daily Sudoku || ' +\
    subtitle + '}\n\\author{}\n\\begin{document}\n' +\
    '\\maketitle\n\n\\begin{sudoku}\n' +\
    sudoku_string + '\\end{sudoku}\n\n\\end{document}'

main()
