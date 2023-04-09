import random
import time

def displayIntro():
	print('''Вы находитись в землях, заселенных драконами.
Перед собой вы видите две пещеры.В одной из них - дружелюный дракон,
который готов поделиться с вами своими сокровицами. Во второй - 
жадный и голодный дракон, который мигом сьест.''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('В какую пещеру вы войдете? (нажмите клавищу 1 или 2)')
		cave = input()

	return cave 

def checkCave(chosenCave):
	print('Вы приблежаетесь к пещере...')
	time.sleep(2)
	print('Ее темнота заставляет вас дрожать от страха...')
	time.sleep(2)
	print('Большой дракон выпригивает перед вами! Он раскрывает свою пасть и...')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('...делится с вами своими сокровицами!')
	else:
		print('...моментально вас сьедает!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print('Попытаете удачу еще раз? (да или нет)')
	playAgain = input()