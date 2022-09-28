import pygame
import sys
from tkinter import *
from tkinter import messagebox
from Parameters import WIDTH, HEIGHT, BACKGROUND, BORDERS, LINES, FONT, BLACK, GREEN, board

Tk().wm_withdraw()

def is_empty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return r, c
    return False

def is_valid(board, num, row, col):
    for c in range(len(board)):
        if board[row][c] == num:
            return False

    for r in range(len(board)):
        if board[r][col] == num:
            return False
    x = (row // 3) * 3
    y = (col // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board, win):
    if is_empty(board) == False:
        return True
    else:
        row, col = is_empty(board)

    for num in range(1, 10):

        if is_valid(board, num, row, col):
            board[row][col] = num
            value = FONT.render(str(num), True, GREEN)
            win.blit(value, ((50 * col + 55 + 12), (50 * row + 57)))
            pygame.display.update()
            pygame.time.delay(30)

            if solve(board, win):
                return True

            board[row][col] = 0
            pygame.draw.rect(
                win, BACKGROUND, (50 * col + 55, 50 * row + 55, 40, 40))
            pygame.display.update()

    return False

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill((BACKGROUND))

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, BORDERS, (50 + 50 * i, 50),
                             (50 + 50 * i, 500), 3)
            pygame.draw.line(win, BORDERS, (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 3)
        else:
            pygame.draw.line(win, LINES, (50 + 50 * i, 50),
                             (50 + 50 * i, 500), 2)
            pygame.draw.line(win, LINES, (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 2)

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                value = FONT.render(str(board[i][j]), True, BACKGROUND)
                win.blit(value, ((j + 1.15) * 50 + 10, (i + 1.15) * 50))

            else:
                value = FONT.render(str(board[i][j]), True, BLACK)
                win.blit(value, ((j + 1.15) * 50 + 10, (i + 1.15) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if solve(board, win) == True:
                        messagebox.showinfo('SOLVED!','The Sudoku has been solved!')
                        break

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
main()