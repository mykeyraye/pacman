# -*- coding: utf-8 -*-
"""pacman.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1upIJ0FbyQT-iNmO2r25TscsACDDpO2mg
"""

# prompt: a pac man game

import random
import time
import curses

# Set up the screen
curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()

# Create the colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Create the board
width = 80
height = 25
board = [[' ' for i in range(width)] for j in range(height)]

# Create the player
player = {
    'x': 1,
    'y': 1,
    'direction': 'right',
    'color': curses.COLOR_RED
}

# Create the ghosts
ghosts = []
for i in range(4):
    ghosts.append({
        'x': random.randint(1, width - 2),
        'y': random.randint(1, height - 2),
        'direction': 'right',
        'color': curses.COLOR_YELLOW
    })

# Create the food
food = []
for i in range(100):
    food.append({
        'x': random.randint(1, width - 2),
        'y': random.randint(1, height - 2)
    })

# Draw the board
for i in range(height):
    for j in range(width):
        curses.mvaddch(i, j, board[i][j])

# Draw the player
curses.mvaddch(player['y'], player['x'], curses.ACS_DIAMOND, curses.color_pair(player['color']))

# Draw the ghosts
for ghost in ghosts:
    curses.mvaddch(ghost['y'], ghost['x'], curses.ACS_DIAMOND, curses.color_pair(ghost['color']))

# Draw the food
for piece of food:
    curses.mvaddch(piece['y'], piece['x'], curses.ACS_DIAMOND, curses.color_pair(7))

# Update the board
def update_board():
    # Move the player
    if player['direction'] == 'right':
        player['x'] += 1
    elif player['direction'] == 'left':
        player['x'] -= 1
    elif player['direction'] == 'up':
        player['y'] -= 1
    elif player['direction'] == 'down':
        player['y'] += 1

    # Check if the player hit a wall
    if player['x'] < 1 or player['x'] > width - 2 or player['y'] < 1 or player['y'] > height - 2:
        player['x'] = 1
        player['y'] = 1

    # Check if the player ate a piece of food
    for piece in food:
        if piece['x'] == player['x'] and piece['y'] == player['y']:
            food.remove(piece)

    # Move the ghosts
    for ghost in ghosts:
        if ghost['direction'] == 'right':
            ghost['x'] += 1
        elif ghost['direction'] == 'left':
            ghost['x'] -= 1
        elif ghost['direction'] == 'up':
            ghost['y'] -= 1
        elif ghost['direction'] == 'down':
            ghost['y'] += 1

        # Check if the ghost hit a wall
        if ghost['x'] < 1 or ghost['x'] > width - 2 or ghost['y'] < 1 or ghost['y'] > height - 2:
            ghost['x'] = random.randint(1, width - 2)
            ghost['y'] = random.randint(1, height - 2)

        # Check if the ghost ate the player
        if ghost['x'] == player['x'] and ghost['y'] == player['y']:
            curses.endwin()
            print("You lose!")
            exit()

# Get the input from the user
def get_input():
    key = curses.getch()
    if key == curses.KEY_RIGHT:
        player['direction'] = 'right'
    elif key == curses.KEY_LEFT:
        player['direction'] = 'left'
    elif key == curses.KEY_UP:
        player['direction'] = 'up'
    elif key == curses.KEY_DOWN:
        player['direction'] = 'down'

# The main loop
while True:
    # Update the board
    update_board()

    # Draw the board
    for i in range(height):
        for j in range(width):
            curses.mvaddch(i, j, board[i][j])

    # Draw the player
    curses.mvaddch(player['y'], player['x'], curses.ACS_DIAMOND, curses.color_pair(player['color']))

    # Draw the ghosts
    for ghost in ghosts:
        curses.mvaddch(ghost['y'], ghost['x'], curses.ACS_DIAMOND, curses.color_pair(ghost['color']))

    # Draw the food
    for piece in food:
        curses.mvaddch(piece['y'], piece['x'], curses.ACS_DIAMOND, curses.color_pair(7))

    # Get the input from the user
    get_input()

    # Refresh the screen
    curses.refresh()

    # Wait for a short amount of time
    time.sleep(0.1)
