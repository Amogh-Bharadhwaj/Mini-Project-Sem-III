'''HANGMAN'''
import random
def hangman():
	HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
	words = [line.rstrip() for line in open('hangmanwords.txt')]
	for i in range(len(words)):
		words[i] = words[i].lower()
	index = random.randint(0,len(words)-1)
	word_chosen = words[index]
	word_iterate = word_chosen[:]
	hangman = 'Hangman'
	print("Welcome to HANGMAN")
	count = 0
	word_to_show = []
	for i in word_chosen:
		word_to_show.append('_')
		count += 1
	lives = 6
	print(f"\nYou have to guess a {count} letter word")
	print(f"You have {lives} lives remaining")
	while(lives > 0):
		char = input("Guess a letter: ").lower()
		if char not in word_iterate:
			lives -= 1
		if char in word_iterate:
			indices = []
			for i in range(len(word_iterate)):
				if word_iterate[i] == char:
					indices.append(i)
					word_iterate[i] == '_'
			for i in indices:
				word_to_show[i] = char
			if word_chosen == ''.join(word_to_show):
				break
		print(f"You have {lives} lives remaining")
		print(f"The word now is \n  ",end = '')
		for i in word_to_show:
			print(i,end=' ')
		print("\n")
		print(HANGMANPICS[6-lives])
	if lives == 0:
		print(f'Better luck next time, the word was {word_chosen}')
	else:
		print(f"Congratulations you guessed the word. The word was {word_iterate}")
