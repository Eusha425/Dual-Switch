import tkinter as tk
from tkinter import messagebox
import player_moves_management as pmm

turn_count = 0
button_status = [0,0,0,0,0,0,0,0,0]
winner_status = False

def match_result(player_symbol):   
    check_for_winner(player_symbol)
    check_draw()

def check_draw():
    if winner_status == False and turn_count == 9:
        messagebox.showinfo("Draw","It is a draw")

def check_for_winner(player_symbol):
    global turn_count

    # check all horizontal buttons  
    if button_1["text"] == button_2["text"] and button_2["text"] == button_3["text"] and button_3["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    if button_4["text"] == button_5["text"] and button_5["text"] == button_6["text"] and button_6["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    if button_7["text"] == button_8["text"] and button_8["text"] == button_9["text"] and button_9["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)

    # check all vertical buttons
    if button_1["text"] == button_4["text"] and button_4["text"] == button_7["text"] and button_7["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    if button_2["text"] == button_5["text"] and button_5["text"] == button_8["text"] and button_8["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    if button_3["text"] == button_6["text"] and button_6["text"] == button_9["text"] and button_9["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)

    # check all diagonal buttons
    if button_1["text"] == button_5["text"] and button_5["text"] == button_9["text"] and button_9["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    if button_3["text"] == button_5["text"] and button_5["text"] == button_7["text"] and button_7["text"] == player_symbol:
        winner_symbol = pmm.return_player_turn_symbol(turn_count)
        display_winner(winner_symbol)
    
def display_winner(winner_symbol):
    global winner_status
    if winner_symbol == "X":
        messagebox.showinfo("Congratulations", "Player 1 winner")
        winner_status = True
    else:
        messagebox.showinfo("Congratulations", "Player 2 winner")
        winner_status = True

def button_1_press():
    global button_status
    global turn_count
    get_status = pmm.check_button_already_pressed(button_status[0])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[0] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_1["text"] = player_symbol
        match_result(player_symbol)
    
def button_2_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[1])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[1] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_2["text"] = player_symbol
        match_result(player_symbol)

def button_3_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[2])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[2] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_3["text"] = player_symbol
        match_result(player_symbol)

def button_4_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[3])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[3] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_4["text"] = player_symbol
        match_result(player_symbol)

def button_5_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[4])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[4] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_5["text"] = player_symbol
        match_result(player_symbol)


def button_6_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[5])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[5] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_6["text"] = player_symbol
        match_result(player_symbol)


def button_7_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[6])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[6] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_7["text"] = player_symbol
        match_result(player_symbol)

def button_8_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[7])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[7] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_8["text"] = player_symbol
        match_result(player_symbol)

def button_9_press():
    global turn_count
    global button_status
    get_status = pmm.check_button_already_pressed(button_status[8])
    if get_status == 1:
        messagebox.showerror("Error", "Button Already Pressed")
    else:
        button_status[8] = 1
        turn_count += 1
        player_symbol = pmm.return_player_turn_symbol(turn_count)
        button_9["text"] = player_symbol
        match_result(player_symbol)

window = tk.Tk()

window.title("GUI TikTacToe")
window.geometry("250x350")

welcome_label = tk.Label(text="Welcome to Tic Tac Toe", relief="groove")
welcome_label.place(x = 60, y = 15)

button_1 = tk.Button(window, command=button_1_press)
button_1.place(x=45,y=50,width=50,height=50)

button_2 = tk.Button(window, command= button_2_press)
button_2.place(x=100,y=50,width=50,height=50)

button_3 = tk.Button(window,command=button_3_press)
button_3.place(x=155,y=50,width=50,height=50)

button_4 = tk.Button(window,command=button_4_press)
button_4.place(x=45,y=105,width=50,height=50)

button_5 = tk.Button(window,command=button_5_press)
button_5.place(x=100,y=105,width=50,height=50)

button_6 = tk.Button(window,command=button_6_press)
button_6.place(x=155,y=105,width=50,height=50)

button_7 = tk.Button(window,command=button_7_press)
button_7.place(x=45,y=160,width=50,height=50)

button_8 = tk.Button(window,command=button_8_press)
button_8.place(x=100,y=160,width=50,height=50)

button_9 = tk.Button(window,command=button_9_press)
button_9.place(x=155,y=160,width=50,height=50)



window.mainloop()