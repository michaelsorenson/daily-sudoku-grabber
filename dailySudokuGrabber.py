import json
from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    # get headless browser driver
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    # get todays medium puzzle
    driver.get('https://www.nytimes.com/puzzles/sudoku/medium')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='lxml')
    # get medium puzzle and create latex string
    game = soup.findAll('div', {'class': 'pz-game-screen'})[0].find('script').text
    puzzles = json.loads(game[game.find('{'):game.rfind('}') + 1])
    todays_puzzle = puzzles['medium']['puzzle_data']['puzzle']
    tex_str = get_tex_str(puzzle_to_latex(todays_puzzle))
    # write to file
    puzzle_file = open("puzzle.tex", "w")
    puzzle_file.write(tex_str)
    puzzle_file.close()

def puzzle_to_latex(puzzle_data):
    puzzle_str = ''
    for i in range(9):
        for j in range(9):
            cur_entry = puzzle_data[9 * i + j]
            cur_entry = str(cur_entry) if cur_entry != 0 else ' '
            puzzle_str += '|' + cur_entry
        puzzle_str += '|.\n'
    return puzzle_str

def get_tex_str(sudoku_string):
    return '\\documentclass{article}\n\\usepackage{sudoku}\n\\usepackage{graphicx}\n\\graphicspath{ {./images/} }\n' +\
    '\\title{\\includegraphics{icons/nytimes-icon.png} NYTimes Daily Sudoku}\n\\author{}\n\\begin{document}\n' +\
    '\\maketitle\n\n\\begin{sudoku}\n' +\
    sudoku_string + '\\end{sudoku}\n\n\\end{document}'

main()