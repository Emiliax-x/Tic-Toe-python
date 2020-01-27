#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def display_board(board):  #STEP 1
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-- --')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-- --')
    print(board[1] + '|' + board[2] + '|' + board[3])
    if ' ' in board:
      return 'next turn'

#Funcion correcta

def player_input():    #STEP 2
    count = 0
    while count == 0:
        player_1 = input('Hello! Choose a X or O: ')
        if player_1 == 'X' or player_1 == 'O':
          count += 1
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return player_1,player_2

#Funcion correcta

def place_marker(board, marker, position):   #STEP 3
    board[position] = marker
    return display_board(board)

#Funcion correcta 

def win_check(board,mark):   #STEP 4
    if board[1] == board[4] == board[7] == mark or board[4] == board[5] == board[6] == mark or  board[8] == board[5] == board[2] == mark or board[9] == board[6] == board[3] == mark or  board[7] == board[8] == board[9] == mark or board[1] == board[2] == board[3] == mark or board[1] == board[5] == board[9] == mark:
        return True
    return False


#Funcion correcta 

def choose_first():   #STEP 5
    print('The player that stars is: ')
    azar = random.randint(1,2)
    if azar == 1:
        return 'player_1'
    return 'player_2'

#Funcion correcta

def space_check(board, position):          #STEP 6
    if board[position] == ' ':
        return True
    return False


def  player_choice (board):   #STEP 7
    print('Choose a position between 1 and 9: ')
    count = 0
    while count == 0:
        position = int(input())
        space = space_check(board,position)
        if space == True:
            count += 1
        else:
          print('Ups, this position is already occupied, choice another one')
    return position
        
#Funcion correcta

def replay():    #STEP 9
    question = input('Wanna play again (yes/no) ? ')
    if question == 'yes':
        return True
    return False

#Funcion correcta

print('Welcome to Tic Tac Toe!')
game = 0
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
while game == 0:
    players = player_input()
    player_1 = players[0]
    player_2 = players[1]
    print('Player_1: ', player_1)
    print('Player_2: ', player_2)
    first = choose_first()
    print(first)
    display_board(board)
    for i in range(9):
        if first == 'player_1':    
            position = player_choice(board)
            marker = player_1
            print(place_marker(board,marker,position))
            if win_check(board,marker) == True:
                print('You won {}! Congratulations'.format('player_1'))
                break
            else:
                first = 'player_2'
        else:            
            position = player_choice(board)
            marker = player_2
            print(place_marker(board,marker,position))
            if win_check(board,marker) == True:
                print('You won {}! Congratulations'.format('player_2'))
                break
            else:
                first = 'player_1'
    again = replay()
    if again == True:
        pass
    else:
        game += 1

