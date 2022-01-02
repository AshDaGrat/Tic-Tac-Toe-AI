import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

def button_click(m):
    if win() == False:
        if board[m] == " ":
            insert_letter("O", m)
            if draw() == False:
                comp_move()
            game()

def reset():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, board, z
    button_1 = tk.Button(root, command = lambda m = 1: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[1])
    button_2 = tk.Button(root, command = lambda m = 2: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[2])
    button_3 = tk.Button(root, command = lambda m = 3: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[3])
    button_4 = tk.Button(root, command = lambda m = 4: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[4])
    button_5 = tk.Button(root, command = lambda m = 5: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[5])
    button_6 = tk.Button(root, command = lambda m = 6: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[6])
    button_7 = tk.Button(root, command = lambda m = 7: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[7])
    button_8 = tk.Button(root, command = lambda m = 8: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[8])
    button_9 = tk.Button(root, command = lambda m = 9: button_click(m), font = ("Helvetica, 20"), bg = "snow", height = 3, width = 6, text = board[9])

    button_1.grid(row=0, column=0)
    button_2.grid(row=0, column=1)
    button_3.grid(row=0, column=2)
    button_4.grid(row=1, column=0)
    button_5.grid(row=1, column=1)
    button_6.grid(row=1, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)

    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    winner.config(text = " ")
    game()

def game():
        button_1.config(text = board[1])
        button_2.config(text = board[2])
        button_3.config(text = board[3])
        button_4.config(text = board[4])
        button_5.config(text = board[5])
        button_6.config(text = board[6])
        button_7.config(text = board[7])
        button_8.config(text = board[8])
        button_9.config(text = board[9])
        if (draw()):
            winner.config(text = "Draw")
        if win():
            winner.config(text = "X Wins")
            on_win(win())

def insert_letter(letter, position):
    board[position] = letter
    game()

def win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return 1
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return 2
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return 3
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return 4
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return 5
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return 6
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return 7
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return 8
    else:
        return False

def is_winner(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def on_win(win_case):
    if win_case == 1:
        button_1.config(bg = "pale green")
        button_2.config(bg = "pale green")
        button_3.config(bg = "pale green")
        winner.config(text = board[1] + " Wins")
    elif win_case == 2:
        button_4.config(bg = "pale green")
        button_5.config(bg = "pale green")
        button_6.config(bg = "pale green")
        winner.config(text = board[5] + " Wins")
    elif win_case == 3:
        button_7.config(bg = "pale green")
        button_8.config(bg = "pale green")
        button_9.config(bg = "pale green")
        winner.config(text = board[9] + " Wins")
    elif win_case == 4:
        button_1.config(bg = "pale green")
        button_4.config(bg = "pale green")
        button_7.config(bg = "pale green")
        winner.config(text = board[1] + " Wins")
    elif win_case == 5:
        button_2.config(bg = "pale green")
        button_5.config(bg = "pale green")
        button_8.config(bg = "pale green")
        winner.config(text = board[5] + " Wins")
    elif win_case == 6:
        button_3.config(bg = "pale green")
        button_6.config(bg = "pale green")
        button_9.config(bg = "pale green")
        winner.config(text = board[9] + " Wins")
    elif win_case == 7:
        button_1.config(bg = "pale green")
        button_5.config(bg = "pale green")
        button_9.config(bg = "pale green")
        winner.config(text = board[5] + " Wins")
    elif win_case == 8:
        button_3.config(bg = "pale green")
        button_5.config(bg = "pale green")
        button_7.config(bg = "pale green")
        winner.config(text = board[5] + " Wins")

def draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True
    
def comp_move():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = "X"
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    insert_letter("X", bestMove)

def minimax(board, depth, isMaximizing):
    if (is_winner("X")):
        return 1
    elif (is_winner("O")):
        return -1
    elif (draw()):
        return 0
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "X"
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "O"
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

button_restart = tk.Button(root, command = reset, font = ("Helvetica, 20"), bg = "snow", height = 1, width = 6, text = "Restart")
button_restart.grid(row = 3, column = 0)
winner = tk.Label(root, borderwidth=5, text = " ", font = ("Helvetica, 20") )
winner.grid(row=3, column=1, columnspan=2)
reset()
root.mainloop()
