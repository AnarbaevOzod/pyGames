import random
HANGMAN_PICS = ('''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
     ===''')
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLeters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print('Ошибочные буквы:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()

	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)):
		if secretWord[i] in correctLeters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	for letter in blanks:
		print(letter, end=' ')
	print()

def getGuess(alreadyGuessed):
	while True:
		print('Введите букву.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Пожалуйста, введите одну букву.')
		elif guess in alreadyGuessed:
			print('Вы уже называли эту букву. Назовите другую.')
		elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
			print('Пожалуйста, введите БУКВУ')
		else:
			return guess


def playAgain():
	print('Хотите сыграть еще? (да или нет)')
	return input().lower().startswith('д')



print('В И С Е Л И Ц А')
missedLetters = ''
correctLeters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:

	displayBoard(missedLetters, correctLeters, secretWord)


	guess = getGuess(missedLetters + correctLeters)

	if guess in secretWord:
		correctLeters = correctLeters + guess


		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLeters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
			gameIsDone = True

	else:
		missedLetters = missedLetters + guess


		if len(missedLetters) == len(HANGMAN_PICS) -1:
			displayBoard(missedLetters, correctLeters, secretWord)
			print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв:' + str(len(correctLeters)) + '.Было загадаго слово "' + secretWord + '".')
			gameIsDone = True

		
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLeters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break
