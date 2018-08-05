import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")

""" *** Memory *** """

board2 = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
a = ["X"]

""" *** Functions *** """
player = [True]
player[0] = messagebox.askyesno("1p vs", "Playing against another player?")
print("is there another player? ", player[0])

b = [0, 0, 0, 0]

def turn(pos1, board2, button, a):
    """ enter choice to memory and change the board and interface """
    print("playing with", a)
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            if board2[i][n] == str(pos1):
                board2[i][n] = str(a[0])

    # toggle button text

    if button["text"] == " ":
        button["text"] = str(a[0])

        # change a to new turn
        if player[0]:

            if a[0] == "X":
                a[0] = "O"
                print("changed x to o")

            else:
                a[0] = "X"
                print("changed o to x")

    else:
        print("cant, already taken")
        aiturn = True
        return aiturn

    # check win state
    aiturn = win()

    # Ai

    if not player[0]:

        print("fired ai")

        if not aiturn:
            board2, aiturn = checkatk(board2, aiturn)
            print("ai turn for atk is ", aiturn)

        if not aiturn:
            board2, aiturn = checkdef(board2, aiturn)
            print("ai turn for def is ", aiturn)

        if not aiturn:
            board2, pos1, a, button, aiturn = aiplay(board2, pos1, a, button, aiturn)
            print("ai turn for random is ", aiturn)

    # aiturn = False

    for i in range(3):
        print(board2[i][0], board2[i][1], board2[i][2])

    # check win state
    aiturn = win()

    return board2, pos1, button, a, aiturn


def aiplay(board2, pos1, a, button, aiturn):
    """ chose a random number and play it"""
    #pos1 = "".join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8"], 1))
    pos1=random.randrange(0,9)

    for i in range(len(board2)):
        for n in range(len(board2[i])):
            if str(board2[i][n]) == str(pos1):
                print(str(board2[i][n]), " is the changed value")
                board2[i][n] = "O"
                options[str(pos1)]()
                aiturn = True

                return board2, pos1, a, button, aiturn
    #else:
        # repeat if choice is taken
    board2, pos1, a, button, aiturn = aiplay(board2, pos1, a, button, aiturn)
    return board2, pos1, a, button, aiturn


def win():
    """check win state"""
    for i in range(3):

        if "XXX" == str("".join(board2[i][0:3])) or "XXX" == (board2[0][i] + board2[1][i] + board2[2][i]):
            b[0] += 1
            reset(1)
            aiturn = True
            if player[0]:
                a[0] = "X"
            return aiturn

    if (board2[0][0] + board2[1][1] + board2[2][2]) == "XXX" or (
                    board2[0][2] + board2[1][1] + board2[2][0]) == "XXX":
        b[0] += 1
        reset(1)
        aiturn = True
        if player[0]:
            a[0] = "X"
        return aiturn

    for i in range(3):
        if "OOO" == str("".join(board2[i][0:3])) or "OOO" == (board2[0][i] + board2[1][i] + board2[2][i]):
            if player[0]:
                b[1] += 1
            else:
                b[2] += 1
            reset(2)

    if (board2[0][0] + board2[1][1] + board2[2][2]) == "OOO" or (
                    board2[0][2] + board2[1][1] + board2[2][0]) == "OOO":
        if player[0]:
            b[1] += 1
        else:
            b[2] += 1
        reset(2)

    info = 0
    for i in range(3):
        for n in range(3):
            if board2[i][n] == "X":
                info += 1

            if board2[i][n] == "O":
                info += 1

    if info == 9:
        reset(0)
        b[3] += 1
        aiturn = True
        return aiturn


def reset(n):
    """ win state, reset board """
    if n == 0:
        messagebox.showinfo('No one won', 'No one won, restarting')
    elif n == 1:
        messagebox.showinfo('There is a winner!', 'Player ' + str(n) + ' is the winner!')
    elif n == 3:
        ans = messagebox.askquestion('Restart', "Are you sure?")
        if ans == 'yes':
            player1 = messagebox.askyesno("1p vs", "Playing against another player?")
            print("is there another player? ", player1)
            player[0] = player1
        else:
            return
    else:
        if(player[0]):
            messagebox.showinfo('There is a winner!', 'Player ' + str(n) + ' is the winner!')
        else:
            messagebox.showinfo('There is a winner!', 'Computer is the winner!')
    numb = 0
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            board2[i][n] = str(numb)
            numb += 1

    return board2


def checkatk(board2, aiturn):
    """win the game on the next move"""
    danger = 0
    danger2 = 0
    danger3 = 0
    danger4 = 0

    for n in range(3):
        for i in range(3):
            if i == 0:
                danger = 0
            if board2[n][i] == "O":
                danger += 1

        if danger == 2:
            for i in range(3):
                if board2[n][i] != "O" and board2[n][i] != "X" and not aiturn:
                    options[board2[n][i]]()
                    print("Ai played")
                    board2[n][i] = "O"
                    danger = 0
                    aiturn = True

        for i in range(3):
            if i == 0:
                danger2 = 0
            if board2[i][n] == "O":

                danger2 += 1

        if danger2 == 2:
            for i in range(3):
                if board2[i][n] != "O" and board2[i][n] != "X" and not aiturn:
                    options[board2[i][n]]()
                    print("Ai played")
                    board2[i][n] = "O"
                    danger2 = 0
                    aiturn = True

    if board2[1][1] == "O":
        danger3 += 1
        danger4 += 1

    if board2[0][0] == "O":
        danger3 += 1
    if board2[2][2] == "O":
        danger3 += 1

    if board2[2][0] == "O":
        danger4 += 1
    if board2[0][2] == "O":
        danger4 += 1

    if danger3 == 2 and not aiturn:
        if board2[0][0] != "O" and board2[0][0] != "X":
            options[board2[0][0]]()
            print("Ai played")
            board2[0][0] = "O"
            aiturn = True

        if board2[1][1] != "O" and board2[1][1] != "X":
            options[board2[1][1]]()
            print("Ai played")
            board2[1][1] = "O"
            aiturn = True

        if board2[2][2] != "O" and board2[2][2] != "X":
            options[board2[2][2]]()
            print("Ai played")
            board2[2][2] = "O"
            aiturn = True

    if danger4 == 2 and not aiturn:
        if board2[0][2] != "O" and board2[0][2] != "X":
            options[board2[0][2]]()
            print("Ai played")
            board2[0][2] = "O"
            aiturn = True

        if board2[1][1] != "O" and board2[1][1] != "X":
            options[board2[1][1]]()
            print("Ai played")
            board2[1][1] = "O"
            aiturn = True

        if board2[2][0] != "O" and board2[2][0] != "X":
            options[board2[2][0]]()
            print("Ai played")
            board2[2][0] = "O"
            aiturn = True

    return board2, aiturn


def checkdef(board2, aiturn):
    """block player in the next move"""
    danger = 0
    danger2 = 0
    danger3 = 0
    danger4 = 0

    for n in range(3):
        for i in range(3):
            if i == 0:
                danger = 0
            if board2[n][i] == "X":
                danger += 1

        if danger == 2:
            for i in range(3):
                if board2[n][i] != "O" and board2[n][i] != "X" and not aiturn:
                    options[board2[n][i]]()
                    print("Ai played")
                    board2[n][i] = "O"
                    danger = 0
                    aiturn = True

        for i in range(3):
            if i == 0:
                danger2 = 0
            if board2[i][n] == "X":
                danger2 += 1

        if danger2 == 2:
            for i in range(3):
                if board2[i][n] != "O" and board2[i][n] != "X" and not aiturn:
                    options[board2[i][n]]()
                    print("Ai played")
                    board2[i][n] = "O"
                    danger2 = 0
                    aiturn = True

    if board2[1][1] == "X":
        danger3 += 1
        danger4 += 1

    if board2[0][0] == "X":
        danger3 += 1
    if board2[2][2] == "X":
        danger3 += 1

    if board2[2][0] == "X":
        danger4 += 1
    if board2[0][2] == "X":
        danger4 += 1

    if danger3 == 2 and not aiturn:
        if board2[0][0] != "O" and board2[0][0] != "X":
            options[board2[0][0]]()
            print("Ai played")
            board2[0][0] = "O"
            aiturn = True

        if board2[1][1] != "O" and board2[1][1] != "X":
            options[board2[1][1]]()
            print("Ai played")
            board2[1][1] = "O"
            aiturn = True

        if board2[2][2] != "O" and board2[2][2] != "X":
            options[board2[2][2]]()
            print("Ai played")
            board2[2][2] = "O"
            aiturn = True

    if danger4 == 2 and not aiturn:
        if board2[0][2] != "O" and board2[0][2] != "X":
            options[board2[0][2]]()
            print("Ai played")
            board2[0][2] = "O"
            aiturn = True

        if board2[1][1] != "O" and board2[1][1] != "X":
            options[board2[1][1]]()
            print("Ai played")
            board2[1][1] = "O"
            aiturn = True

        if board2[2][0] != "O" and board2[2][0] != "X":
            options[board2[2][0]]()
            print("Ai played")
            board2[2][0] = "O"
            aiturn = True

    return board2, aiturn


# functions to change the buttons the ai chose

def ch1():
    button1["text"] = "O"


def ch2():
    button2["text"] = "O"


def ch3():
    button3["text"] = "O"


def ch4():
    button4["text"] = "O"


def ch5():
    button5["text"] = "O"


def ch6():
    button6["text"] = "O"


def ch7():
    button7["text"] = "O"


def ch8():
    button8["text"] = "O"


def ch9():
    button9["text"] = "O"


# dictionary

options = {"0": ch1,
           "1": ch2,
           "2": ch3,
           "3": ch4,
           "4": ch5,
           "5": ch6,
           "6": ch7,
           "7": ch8,
           "8": ch9,
           }

""" *** Menu Item def *** """

def abc():
    fw=open("rules.txt", 'r')
    st=fw.read()
    fw.close()
    r2=Tk()
    r2.title("Rules")
    l1=Label(r2, text=st)
    l1.pack(side=TOP)
    r2.mainloop()

def efg():
    messagebox.showinfo("Version", "Version 2.0 \n Name: Tic Tac Toe \n Developed By: Dot_Bot \n Developed on: 13/03/18 \n Last modified: 17/04/18")

def qgame():
    ans2=messagebox.askquestion('Quit', "Do you really want to quit?")
    if ans2 == 'yes':
        b[0] = 0
        b[1] = 0
        b[2] = 0
        b[3] = 0
        quit()
    else:
        return

def lmn():
    text1 = "P1 Won: " + str(b[0]) + "\nP2 won: " + str(b[1]) + "\nComputer won: " + str(b[2]) + "\nDraw: " + str(b[3])
    messagebox.showinfo('History', text1)

def re():
    ans3 = messagebox.askquestion('Reset', "Reset game data?")
    if ans3 == 'yes':
        b[0] = 0
        b[1] = 0
        b[2] = 0
        b[3] = 0

    else:
        return

""" *** Layout *** """

menu1=Menu(root)
root.config(menu=menu1)
gamemenu=Menu(menu1)
menu1.add_cascade(label="Game", menu=gamemenu)
gamemenu.add_command(label="New Game", command=lambda: reset(3))
gamemenu.add_separator()
gamemenu.add_command(label="Quit", command=qgame)
view=Menu(menu1)
menu1.add_cascade(label="View", menu=view)
view.add_command(label="History", command=lmn)
view.add_command(label="Reset", command=re)
helpmenu=Menu(menu1)
menu1.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Rules", command=abc)
helpmenu.add_command(label="Version", command=efg)

button1 = ttk.Button(root, text=" ", command=lambda: turn("0", board2, button1, a))
button2 = ttk.Button(root, text=" ", command=lambda: turn("1", board2, button2, a))
button3 = ttk.Button(root, text=" ", command=lambda: turn("2", board2, button3, a))
button4 = ttk.Button(root, text=" ", command=lambda: turn("3", board2, button4, a))
button5 = ttk.Button(root, text=" ", command=lambda: turn("4", board2, button5, a))
button6 = ttk.Button(root, text=" ", command=lambda: turn("5", board2, button6, a))
button7 = ttk.Button(root, text=" ", command=lambda: turn("6", board2, button7, a))
button8 = ttk.Button(root, text=" ", command=lambda: turn("7", board2, button8, a))
button9 = ttk.Button(root, text=" ", command=lambda: turn("8", board2, button9, a))

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

button1.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
button2.grid(row=0, column=1, sticky="nsew", padx=4, pady=4)
button3.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
button4.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
button5.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)
button6.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)
button7.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
button8.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)
button9.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)

root.mainloop()
