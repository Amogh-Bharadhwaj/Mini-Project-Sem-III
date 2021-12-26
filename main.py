from tictactoe import *
from hangman import *
from quiz import *
import random
import numpy as np
choice = int(input("1.TicTacToe\n2.Hangman\n3.Quiz\n0.Exit\nEnter your choice: "))
while(choice != 0):
	if choice == 1:
		ticcer()
	elif choice == 2:
		hangman()
	elif choice == 3:
		quizgame()
	choice = int(input("\n1.TicTacToe\n2.Hangman\n3.Quiz\n0.Exit\nEnter your choice: "))
