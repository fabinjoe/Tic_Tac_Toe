# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math
from tkinter import *
from time import sleep
#import pygame


#pygame.mixer.init()

# %%
class gameBoard():
    def __init__(self):
        self.board = [[-5 for x in range(3)] for y in range(3)]
        self.buttons = [[0 for x in range(3)] for y in range(3)]

    # This Functions sets up the canvas of the application
    def environment(self): 
        canvas.title("TIC - TAC - TOE")
        
        def close_win():
            self.soundEffects(1)
            canvas.destroy()

        #photo = PhotoImage(file = "volume-on.png") 
        music = Button(win, anchor='center', text="🎵", font=('Courier', '18','bold'), bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101')
        music.place(anchor="center", x=383, rely=0.155, width=30, height=30)        
        
        sound = Button(win, anchor='center', text="🔊", font=('Courier', '16','bold'), bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=lambda: self.soundEffects(0, sound))
        sound.place(anchor="center", x=383, rely=0.255, width=30, height=30)        
        
        background = Frame(win, bg='#d60b0b')
        background.place(anchor='center', relx=0.5, rely=0.45, relwidth=0.82, relheight=0.82)

        game = Frame(win, bg='#134852')
        game.place(anchor='center', relx=0.5, rely=0.45, relwidth=0.8, relheight=0.8)

        close = Button(win, text="EXIT", font=('Courier', '27','bold'), anchor='center', bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=close_win)
        close.place(anchor='center', relx=0.7, rely=0.925, width=150, height=45)
        
        global replay
        replay = Button(win, text="REPLAY", font=('Courier', '27','bold'), anchor='center', bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=lambda: self.startRound())

    # This funstion prints the intro
    def introScreen(self):
        intro = Label(win, text="WELOME TO\nTIC-TAC-TOE", font=('Courier', '27','bold'), bg='#d98314')
        intro.place(anchor='center', relx=0.5, rely=0.37, width=300, height=200)
        intro = Label(win, text="-FABIN JOE", font=('Courier', '18','bold'), bg='#d98314', fg='#613a07')
        intro.place(anchor='center', relx=0.62, rely=0.5, width=160, height=45)
        
        start = Button(win, text="CLICK HERE TO CONTINUE", font=('Courier', '15','bold'), anchor='center', bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=lambda: self.startRound() )
        start.place(anchor='center', relx=0.5, rely=0.7, width=300, height=45)
        #sleep(5)
    
    def gameMode(self):
        options = Label(win, text="CHOOSE GAMEMODE", font=('Courier', '24','bold'), bg='#d98314')
        options.place(anchor='center', relx=0.5, rely=0.3, width=300, height=100)

        option1 = Button(win, text="SINGLEPLAYER", font=('Courier', '15','bold'), anchor='center', bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=lambda: self.startRound(2) )
        option1.place(anchor='center', relx=0.5, rely=0.52, width=300, height=45)     

        option2 = Button(win, text="MULTIPLAYER", font=('Courier', '15','bold'), anchor='center', bg='#d60b0b', activebackground='#ed2f2f', activeforeground='#910101', command=lambda: self.startRound() )
        option2.place(anchor='center', relx=0.5, rely=0.65, width=300, height=45)   

    # This function prints a unique text relevent to the progress of the game
    def printTitle(self, message):
        chat = Label(win, text=message, font=('Courier', '15','bold'), bg='#d98314')
        chat.place(anchor='center', relx=0.5, rely=0.15, width=300, height=35)

    # This functions prints the score of the players
    def printScore(self, s1, s2, default=0):
        score1 = Label(win, text=f"P1 SCORE:{s1}", font=('Courier', '15','bold'), bg='#028fa8', relief=RAISED)
        score1.place(anchor='center', relx=0.3, rely=0.052, width=150, height=30)
        
        text = "P2"
        if default:
            text = "AI"
        score2 = Label(win, text=text+f" SCORE:{s2}", font=('Courier', '15','bold'), bg='#028fa8', relief=RAISED)
        score2.place(anchor='center', relx=0.7, rely=0.052, width=150, height=30)

        if s1 > s2:
            score1["bg"] = "#039145"
        elif s2 > s1:
            score2["bg"] = "#039145"

    # This function prints out the main active component(The Table) of the application
    def startRound(self, player=1):
        global level
        game = Frame(win, bg='#134852')

        if not (level == 0):
            self.soundEffects(1)
        if player == 2:
                game.place(anchor='center', relx=0.5, rely=0.45, relwidth=0.8, relheight=0.8)
                aiGame(self)
        elif level == 0:
            self.introScreen()
        elif level == 1:
            game.place(anchor='center', relx=0.5, rely=0.45, relwidth=0.8, relheight=0.8)
            self.gameMode()
        else:
            if level == 2:
                game.place(anchor='center', relx=0.5, rely=0.45, relwidth=0.8, relheight=0.8)
                self.printScore(0,0)

            global turn
            global roundCount
            global replay
            replay["text"] = "REPLAY"
            replay.place(anchor='center', relx=0.3, rely=0.925, width=150, height=45)
            turn = 0
            self.board = [[-5 for x in range(3)] for y in range(3)]
            self.printTitle(f"P{2-((roundCount+turn)%2)}(X) - Turn")       

            game = Frame(win, bg='BLACK')
            game.place(anchor='center', x=203, y=210, width=248, height=248)

            for row in range(3):
                for col in range(3):
                    self.buttons[row][col] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', height=(10*row)+col, command=lambda r=(10*row)+col: self.setValue(r/10,r%10))
                    self.buttons[row][col].place(anchor='center', x=121 + 82*col, y=128 + 82*row, width=80, height=80)

        level += 1

    # This function is called when a player plays a move
    def setValue(self, r, c, player=1):
        row = int(r)
        col = int(c)
        global turn
        global roundCount
        self.printTitle(f"P{2-((roundCount+turn+1)%2)}(O) - Turn")
        if turn%2:
            player = (player+(-2)) + 1
            self.printTitle(f"P{2-((roundCount+turn+1)%2)}(X) - Turn")
        turn += 1

        self.board[row][col] = player
        self.buttons[row][col]["state"] = "disabled"
        self.buttons[row][col]["font"] = ('Courier', '40','bold')

        if player:
            self.buttons[row][col]["text"] = "X"
        else:
            self.buttons[row][col]["text"] = "O"

        winner = self.checkWinner()
        if not(winner == -1):
            if winner == 1:
                self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
            elif winner == 0:
                self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
            global score
            score[1-((roundCount+winner+1)%2)] += 1
            self.printScore(score[0], score[1])
            roundCount += 1
            self.endGame()
            self.soundEffects(2)
        elif turn == 9:
            self.printTitle("This Round is a Draw")      
            self.endGame()      


    # This function checks if there is a winner of the round
    def checkWinner(self):
        for row in self.board:
            if all(cell == row[0] for cell in row) and (row[0] != -5):
                return row[0]

        for col in range(3):
            if all(row[col] == self.board[0][col] for row in self.board) and (self.board[0][col] != -5):
                return self.board[0][col]

        if(self.board[1][1] == -5): 
            return -1

        if (self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        if (self.board[2][0] == self.board[1][1]) and (self.board[0][2] == self.board[2][0]):
            return self.board[2][0]
        return -1

    # This function is envoked when a round is ended
    def endGame(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"
        global replay
        replay["text"] = "AGAIN"

    def music(self, button={}):
        '''
        global music
        music = 1 - music
        
        if music:
            button["text"] = "🗙"
        else:
            button["text"] = "🎵"
            pygame.mixer.music.load("Game_Environment/theme.mp3")
            pygame.mixer.music.play()
        '''

    # Plays the various tunes of the game
    def soundEffects(self, tune, button={}):
        '''
        global mute
        if tune == 0: # Mute all soundEffects
            mute = 1 - mute
        
        if mute:
            button["text"] = "🔇"
        else:
            button["text"] = "🔊"
    
        if not mute:
            if tune == 1: # Button Click
                pygame.mixer.music.load("Game_Environment/Sound.mp3")
                pygame.mixer.music.play()
            elif tune == 2: # Victory Theme
                pygame.mixer.music.load("Game_Environment/victory.mp3")
                pygame.mixer.music.play()
    '''




# %%
def aiSetValue(self, row, col, player=1):
    global turn
    global roundCount

    if turn%2:
        player = (player+(-2)) + 1
    turn += 1

    self.board[row][col] = player
    self.buttons[row][col]["font"] = ('Courier', '40','bold')

    for row1 in range(3):
        for col1 in range(3):
            self.buttons[row1][col1]["state"] = "disabled"

    if player:
        self.buttons[row][col]["text"] = "X"
    else:
        self.buttons[row][col]["text"] = "O"

    winner = self.checkWinner()
    if not(winner == -1):
        if winner == 1:
            self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
        elif winner == 0:
            self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
        global score
        score[1-((roundCount+winner+1)%2)] += 1
        self.printScore(score[0], score[1], 2)
        roundCount += 1
        self.endGame()
    elif turn == 9:
        self.printTitle("This Round is a Draw")      
        self.endGame()      

    aiMove(self)


# %%

def aiMove(self, player=1):
    global turn
    global roundCount
    
    if turn%2:
        player = (player+(-2)) + 1
    turn += 1

    corner[(0,0), (2,2), (0,2), (2,0)]
    side[((0,1),(1,0),(1,2),(2,1))]
    center[(1,1)]

    if turn == 1:
        self.buttons[row][col]["font"] = ('Courier', '40','bold')
    if player:
        self.buttons[row][col]["text"] = "X"
    else:
        self.buttons[row][col]["text"] = "O"
    
    winner = self.checkWinner()
    if not(winner == -1):
        if winner == 1:
            self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
        elif winner == 0:
            self.printTitle(f"P{2-((roundCount+winner+1)%2)} wins this Round")
        global score
        score[1-((roundCount+winner+1)%2)] += 1
        self.printScore(score[0], score[1], 2)
        roundCount += 1
        self.endGame()
    elif turn == 9:
        self.printTitle("This Round is a Draw")      
        self.endGame()      



# %%
def aiGame(self):
    global level
    if level == 2:
        self.printScore(0,0,1)

    global turn
    global roundCount

    player = (roundCount+turn)%2

    if not player:
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"



    game = Frame(win, bg='BLACK')
    game.place(anchor='center', x=203, y=210, width=248, height=248)

    self.buttons[0][0] = Button(win, bg="#134852", fg=f"{0}{0}", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,0,0))
    self.buttons[0][0].place(anchor='center', x=121, y=128, width=80, height=80)

    self.buttons[0][1] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,0,1))
    self.buttons[0][1].place(anchor='center', x=203, y=128, width=80, height=80)

    self.buttons[0][2] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,0,2))
    self.buttons[0][2].place(anchor='center', x=285, y=128, width=80, height=80)

    self.buttons[1][0] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,1,0))
    self.buttons[1][0].place(anchor='center', x=121, y=210, width=80, height=80)

    self.buttons[1][1] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,1,1))
    self.buttons[1][1].place(anchor='center', x=203, y=210, width=80, height=80)

    self.buttons[1][2] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,1,2))
    self.buttons[1][2].place(anchor='center', x=285, y=210, width=80, height=80)

    self.buttons[2][0] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,2,0))
    self.buttons[2][0].place(anchor='center', x=121, y=292, width=80, height=80)

    self.buttons[2][1] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,2,1))
    self.buttons[2][1].place(anchor='center', x=203, y=292, width=80, height=80)

    self.buttons[2][2] = Button(win, bg="#134852", activebackground="#1f8da1", relief='flat', command=lambda: aiSetValue(self,2,2))
    self.buttons[2][2].place(anchor='center', x=285, y=292, width=80, height=80)


# %%
def main():
    game = gameBoard()
    game.environment()
    game.startRound()

    canvas.mainloop()


# %%
if __name__ == "__main__":
    canvas = Tk()
    back_ground = Canvas(canvas, width=500, height=500)
    back_ground.pack()
    border = Frame(canvas, width=500, height=500, bg="BLACK")
    border.place(anchor="center", relx=0.5, rely=0.5, height=500, width=500)
    win = Frame(canvas, width=400, height=400, bg="BLACK")
    win.place(anchor="center", relx=0.5, rely=0.5, height=400, width=400)

    score = [0, 0]
    turn = 0
    replay = 0
    roundCount = 1
    level = 0
    mute = 0
    music = 1

    main()


# %%



