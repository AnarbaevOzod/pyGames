import random
HANGMAN_PICS = ['''
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
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Цвета':'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(), 'Фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(), 'Фрукты':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(), 'Животные':'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()}

def getRandomWord(wordDict):
	wordKey = random.choice(list(wordDict.keys()))

	wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
	return [wordDict[wordKey][wordIndex], wordKey]

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

difficulty = ' '
while difficulty not in 'ЛСТ':
	print('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Трудный')
	difficulty = input().upper()

if difficulty == 'С':
	del HANGMAN_PICS[8]
	del HANGMAN_PICS[7]

if difficulty == 'Т':
	del HANGMAN_PICS[8]
	del HANGMAN_PICS[7]
	del HANGMAN_PICS[5]
	del HANGMAN_PICS[3]


missedLetters = ''
correctLeters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
	print('Секретное слово из набора: ' + secretSet)
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
			secretWord, secretSet = getRandomWord(words)
		else:
			break
