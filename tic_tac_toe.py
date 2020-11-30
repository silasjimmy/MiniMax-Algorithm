#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:12:44 2020

@author: silasjimmy
"""

import tkinter as tk
import tkinter.messagebox as msg
import math, random

class Board:
    '''
    Represents the CLI part of the game.
    '''
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.winner = None
        
    def make_move(self, mark, pos):
        '''
        Makes a move on the board and sets the winner in case there is one.
        mark(str): mark of the player.
        pos (int): position on the board.
        '''
        if self.board[pos] == ' ':
            self.board[pos] = mark
            if self.win(pos, mark):
                self.winner = mark
    
    def win(self, pos, mark):
        '''
        Checks if the player has won.
        pos (int): current position of the move.
        mark (str): mark of the player.
        Returns True if the player has won, False otherwise.
        '''
        row_ind = math.floor(pos / 3)
        row = self.board[row_ind * 3: (row_ind+1) * 3]
        if all([s == mark for s in row]):
            return True
        
        col_ind = pos % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == mark for s in column]):
            return True
        
        if pos % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == mark for s in diagnol1]):
                return True
            diagnol2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == mark for s in diagnol2]):
                return True
            
        return False
    
    def empty_squares(self):
        '''
        Checks if the board has empty slots.
        Returns True if there is/are empty slots, False otherwise.
        '''
        return ' ' in self.board
    
    def available_moves(self):
        '''
        Checks for empty slots on the board.
        Returns (list) the intergers of the slots.
        '''
        return [i for i, x in enumerate(self.board) if x == " "]
    
class GameAI:
    '''
    Represents the Game AI.
    '''
    def __init__(self, mark):
        self.mark = mark
        self.other = 'X' if mark == 'O' else 'O'
        
    def get_move(self, board):
        '''
        Gets the move of the AI.
        Returns a random slot if no slot is currently marked, else 
        decides the best slot to make a move using the minimax algorithm.
        '''
        if len(board.available_moves()) == 9:
            return random.choice(board.available_moves())
        
        return self.maximize(board)[0]
    
    def minimize(self, board):
        '''
        The Minimize part of the algorithm.
        Returns the move with the minimum utility and the minimum utility.
        '''
        if not board.empty_squares() or board.winner:
            return None, self.calculate_utility(board)
        
        min_utility = math.inf
        move_with_min_utility = None
        
        for possible_move in board.available_moves():
            board.make_move(self.other, possible_move)
            sim_score = self.maximize(board)
            
            board.board[possible_move] = ' '
            board.winner = None
            
            if sim_score[1] < min_utility:
                move_with_min_utility = possible_move
                min_utility = sim_score[1]
                
        return move_with_min_utility, min_utility
    
    def maximize(self, board):
        '''
        The Maximize part of the algorithm.
        Returns the move iwht maximum utility and the maximum utility.
        '''
        # Check if the board is full or there is a winner.
        if not board.empty_squares() or board.winner:
            return None, self.calculate_utility(board)
        
        # Set max_utility to the lowest value so to maximize it.
        max_utility = -math.inf
        move_with_max_utility = None
        
        # For every possible move, moake a move then call minimize
        for possible_move in board.available_moves():
            board.make_move(self.mark, possible_move)
            sim_score = self.minimize(board)
            
            # Undo the move and set winner to none
            board.board[possible_move] = ' '
            board.winner = None
            
            # Check if the calculated utility is greater than max_utility
            if sim_score[1] > max_utility:
                # If so set that move as the 'best' move
                move_with_max_utility = possible_move
                max_utility = sim_score[1]
                
        return move_with_max_utility, max_utility
    
    def calculate_utility(self, board):
        '''
        Calculates the utility of every move.
        Returns the utility of each move.
        '''
        utility = 0
        
        if board.winner:
            utility = 1 if board.winner == self.mark else -1
            
        return utility

class TicTacToe(tk.Tk):
    '''
    Represents the GUI part of the game.
    '''
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        
        # Center the window to the screen
        self.geometry("%dx%d+%d+%d" % (625, 600, (self.winfo_screenwidth() / 2) - (625 / 2), (self.winfo_screenheight() / 2) - (600 / 2)))
        
        # Creae board
        self.btn1 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn1))
        self.btn2 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn2))
        self.btn3 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn3))
        self.btn4 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn4))
        self.btn5 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn5))
        self.btn6 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn6))
        self.btn7 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn7))
        self.btn8 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn8))
        self.btn9 = tk.Button(self, text=" ", font='Times 70 bold', width=4, height=2, bg='white', fg='black', command=lambda: self.btn_click(self.btn9))
        
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=1, column=0)
        self.btn5.grid(row=1, column=1)
        self.btn6.grid(row=1, column=2)
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        
        self.player_mark = tk.StringVar()
        self.comp_mark = tk.StringVar()
        
        player_decision = msg.askyesno("Choose mark", "Click Yes to choose player mark X or No for player mark O")
        
        self.set_player_mark(player_decision)
        
        self.board = Board()
        self.minimax = GameAI(self.comp_mark.get())
        
    def set_player_mark(self, player_decision):
        '''
        Sets the marks depending on the choice of the player.
        '''
        if player_decision:
            self.player_mark.set('X')
            self.comp_mark.set('O')
        else:
            self.player_mark.set('O')
            self.comp_mark.set('X')
        
    def btn_click(self, btn):
        '''
        Controls the moves of each player.
        '''
        if btn["text"] == " ":
            player_pos = self.match_btn_to_cell(btn)
            self.board.make_move(self.player_mark.get(), player_pos)
            btn["text"] = self.player_mark.get()
            
            if self.board.winner:
                self.game_over(self.player_mark.get())
            elif not self.board.empty_squares():
                self.game_over("T")
                
            self.btn_clicked = True
        else:
            msg.showerror("Marked cell", "Please click an unmarked cell to make your move!")
            
        if self.btn_clicked and self.board.empty_squares():
            comp_pos = self.minimax.get_move(self.board)
            self.board.make_move(self.comp_mark.get(), comp_pos)
            self.match_cell_to_btn(comp_pos)["text"] = self.comp_mark.get()
            
            if self.board.winner:
                self.game_over(self.comp_mark.get())
            elif not self.board.empty_squares():
                self.game_over("T")
                
        self.btn_clicked = False
            
    def game_over(self, mark):
        '''
        Called when game is over.
        Prompts the player for a new game.
        mark (str): The player's mark.
        '''
        if mark == self.player_mark.get():
            msg.showinfo("Game over", "Congratulations!! You win!")
        elif mark == self.comp_mark.get():
            msg.showinfo("Game over", "Aaw, you lost! Anyway, good game.")
        else:
            msg.showinfo("Game over", "It's a tie!")
            
        msg.showinfo("Tic Tac Toe", "Thanks for playing the game!")
        self.after(200, self.destroy)
        
    def match_btn_to_cell(self, btn):
        '''
        Matches the button to its cell position.
        btn: cell button.
        Returns (int) the position of the button.
        '''
        if btn == self.btn1:
            return 0
        elif btn == self.btn2:
            return 1
        elif btn == self.btn3:
            return 2
        elif btn == self.btn4:
            return 3
        elif btn == self.btn5:
            return 4
        elif btn == self.btn6:
            return 5
        elif btn == self.btn7:
            return 6
        elif btn == self.btn8:
            return 7
        elif btn == self.btn9:
            return 8
        
    def match_cell_to_btn(self, position):
        '''
        Matches the cell position to its button.
        position (int): position of the cell.
        Returns the cell button.
        '''
        if position == 0:
            return self.btn1
        elif position == 1:
            return self.btn2
        elif position == 2:
            return self.btn3
        elif position == 3:
            return self.btn4
        elif position == 4:
            return self.btn5
        elif position == 5:
            return self.btn6
        elif position == 6:
            return self.btn7
        elif position == 7:
            return self.btn8
        elif position == 8:
            return self.btn9

if __name__ == "__main__":      
    tic_tac_toe = TicTacToe()
    tic_tac_toe.mainloop()