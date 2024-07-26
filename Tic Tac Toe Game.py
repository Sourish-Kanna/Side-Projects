import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    """Create Common Variables"""
    fontd: tuple[str,int] = ("arial",15)
    current_player: str = "X"
    board: list[list[str]] = [[ " " for _ in range(3)] for _ in range(3)]
    buttons: list[list[None]] = [[None for _ in range(3)] for _ in range(3)]
    mode = None
    board_location = {0:(0,0),1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.mode_label = tk.Label(self.window, font=self.fontd, text="Choose mode:")
        self.mode_label.grid(row=0, columnspan=3)
        self.player_button = tk.Button(self.window, text="Player Vs Player", font=self.fontd, command=lambda: self.set_mode("player"))
        self.player_button.grid(row=1, column=0)
        self.computer_button_easy = tk.Button(self.window, text="Computer Easy", font=self.fontd, command=lambda: self.set_mode("Computer Easy"))
        self.computer_button_easy.grid(row=1, column=1)
        self.computer_button_hard = tk.Button(self.window, text="Computer Hard", font=self.fontd, command=lambda: self.set_mode("Computer Hard"))
        self.computer_button_hard.grid(row=1, column=2)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", width=10, font=("arial",20), height=3,  # type: ignore
                                               command=lambda row=i, col=j: self.click(row, col))
                if j in (0,3,6):
                    self.buttons[i][j].grid(row=2+i, column=j, sticky="E") # type: ignore
                elif j in (1,4,7):
                    self.buttons[i][j].grid(row=2+i, column=j) # type: ignore
                else:
                    self.buttons[i][j].grid(row=2+i, column=j, sticky="W") # type: ignore

        self.restart_button = tk.Button(self.window, text="Restart", font=self.fontd, command=self.restart_game)
        self.restart_button.grid(row=5, columnspan=3)

        self.set_mode("player")

    def click(self, row, col) -> None:
        if self.mode == "Computer Easy" and self.current_player == "O":
            return  # Prevent the computer from making moves when it's not its turn

        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.mode == "player":
                if self.check_winner(row, col):
                    messagebox.showinfo("Winner!", f"{self.current_player} wins!")
                    self.restart_game()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
            elif self.mode == "Computer Easy":
                self.computer_move()
                if self.check_winner(row, col):
                    messagebox.showinfo("Winner!", f"{self.current_player} wins!")
                    self.restart_game()
                else:
                    self.current_player = "X"
            elif self.mode == "Computer Hard":
                self.current_player = "O"
                self.computer_move_hard()
                self.current_player = "X"

            if self.check_draw():
                messagebox.showinfo("Draw!", f"Game is Draw!")
                self.restart_game()

    def check_draw(self) -> bool:
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def check_winner(self, row, col) -> bool:
        symbol = self.board[row][col]
        
        if all(self.board[row][c] == symbol for c in range(3)): # check rows
            return True
        elif all(self.board[r][col] == symbol for r in range(3)): # check columns
            return True
        elif row == col and all(self.board[i][i] == symbol for i in range(3)): # check diagonal
            return True
        elif row + col == 2 and all(self.board[i][2-i] == symbol for i in range(3)): # check anti diagonal
            return True
        else:
            return False

    def restart_game(self) -> None:
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ") # type: ignore
        self.current_player = "X"

    def set_mode(self,typ) -> None:
        self.restart_game()
        messagebox.showinfo("Mode", f"{typ.title()} mode is Selected")
        self.mode = typ

    def computer_move(self) -> None:
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O") # type: ignore

    def computer_move_hard(self) -> None:
        boards = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=="X":
                    boards.append(-1)
                elif self.board[i][j]=="O":
                    boards.append(1)
                elif self.board[i][j]==" ":
                    boards.append(0)
                else:
                    boards.append(0)

        def minmax(board , player ):
            x = analyzeboard(board)
            if (x!=0):
                return(x*player)
            pos = -1
            value = -2
            for i in range (0,9):
                if (board [i]==0):
                    board[i]=player
                    score = -minmax(board , player*-1)
                    board [i] =0
                    if (score> value):
                        value= score
                        pos = i
            if (pos ==-1):
                return 0
            return value
    
        def analyzeboard (board):
            cb = [[ 0, 1, 2] , [3, 4, 5], [6 ,7 ,8], [0, 3, 6] , [1, 4, 7],[2, 5, 8],[0, 4 ,8 ],[ 2, 4, 6]] 
            for i in range (0,8):
                if (board[cb [i][0]]!=0 and 
                    board[cb [i][0]]==board[cb [i][1]] and
                    board[cb [i][0]]==board[cb [i][2]]):
                    return board [cb [i][0]]
            return 0

        pos = -1
        value = -2
        for i in range (0,9):
            if (boards [i]==0):
                boards[i]=1
                score = -minmax(boards , -1)
                boards [i] =0
                if (score> value):
                    value= score
                    pos = i
        boards[pos] = 1
        value = self.board_location.get(pos)
        if value!=None:
            row,col= value
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O") # type: ignore   
            if self.check_winner(row, col):
                messagebox.showinfo("Winner!", f"{self.current_player} wins!")
                self.restart_game()
            elif self.check_draw():
                messagebox.showinfo("Draw!", f"Game is Draw!")
                self.restart_game()     

    def run(self) -> None:
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
