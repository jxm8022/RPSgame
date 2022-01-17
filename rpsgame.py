import tkinter as tk
from numpy import random

class RPSgame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Rock - Paper - Scissors")
        self.geometry("250x400")

        self.moves = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }

        self.score = [0,0] # [p1,comp]
        self.data = [0,0,0] # comp numbers for rock, paper, scissors

        labelTitle = tk.Label(self, text="Rock, Paper, or Scissors?")
        labelTitle.pack(pady=10, padx=10) # side="top", fill="x"?

        labelComp = tk.Label(self, text="Computer chose n/a")
        labelRes = tk.Label(self, text="")
        labelScore = tk.Label(self, text="P1: "+str(self.score[0])+" --- Comp: "+str(self.score[1]))

        rockButton = tk.Button(self, text="Rock", pady=10, padx=10, width=5,
            command=lambda: self.result(labelComp, labelRes, 0, labelScore))
        rockButton.pack(pady=10, padx=10)

        paperButton = tk.Button(self, text="Paper", pady=10, padx=10, width=5,
            command=lambda: self.result(labelComp, labelRes, 1, labelScore))
        paperButton.pack(pady=10, padx=10)

        scissorsButton = tk.Button(self, text="Scissors", pady=10, padx=10, width=5,
            command=lambda: self.result(labelComp, labelRes, 2, labelScore))
        scissorsButton.pack(pady=10, padx=10)

        labelComp.pack(pady=10, padx=10)
        labelRes.pack(pady=10, padx=10)
        labelScore.pack(pady=10, padx=10)

        resetButton = tk.Button(self, text="Reset Score", pady=10, padx=10,
            command=lambda: self.reset(labelScore))
        resetButton.pack(pady=10, padx=10)

    def computer(self):
        print("getting computer choice")
        guess = random.randint(0,99)
        if guess <= 33: # rock
            self.data[0] += 1
            return 0
        elif guess <= 66: # paper
            self.data[1] += 1
            return 1
        elif guess <= 99: # scissors
            self.data[2] += 1
            return 2

    def check(self, comp, res, choice):
        print("checking your choice: ", self.moves[choice])
        if choice == comp:
            res.config(text="Its a tie!")
        if choice == 0:
            if comp == 1:
                self.score[1] += 1
                res.config(text="You lose!")
            elif comp == 2:
                self.score[0] += 1
                res.config(text="You win!")
        if choice == 1:
            if comp == 0:
                self.score[0] += 1
                res.config(text="You win!")
            elif comp == 2:
                self.score[1] += 1
                res.config(text="You lose!")
        if choice == 2:
            if comp == 0:
                self.score[1] += 1
                res.config(text="You lose!")
            elif comp == 1:
                self.score[0] += 1
                res.config(text="You win!")

    def reset(self, labelScore):
        self.score = [0,0]
        labelScore.config(text="P1: "+str(self.score[0])+" --- Comp: "+str(self.score[1]))

    def result(self, label, res, choice, labelScore):
        comp = self.computer()
        print("Computer chose: ",self.moves[comp])
        label.config(text="Computer chose "+self.moves[comp])
        self.check(comp, res, choice)
        labelScore.config(text="P1: "+str(self.score[0])+" --- Comp: "+str(self.score[1]))

if __name__ == "__main__":
    app = RPSgame()
    app.mainloop()