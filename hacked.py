import json
from os import system
import time

sign_in = False
tryAgain = False
cls = lambda: system('cls')
localTime = time.asctime(time.localtime(time.time()))

#  Read in our databases for both the rooms and the existing user login info
with open('study_space.json', 'r') as openfile:
    roomDatabase = json.load(openfile)
with open('credentials.json', 'r') as openfile:
        userLoginDatabase = json.load(openfile)

#  Create a new account
def createAccount():
	global userLoginDatabase
	cls()
	valid = False
	while not valid:
		username = input('Enter a new username: ').strip()
		#  If the given username already exists, then sign in to that account instead
		if username in userLoginDatabase.keys():
			cls()
			print('Sorry, that username already exists. Please use a different username.')
		#  If the given username does not already exist, set up a new user
		else:
			password = input('Enter a new password: ').strip()
			userLoginDatabase[username]=password
			with open('credentials.json', 'w') as outfile:
				json.dump(userLoginDatabase, outfile)
			cls()
			print('Account successfully created! Please sign in:')
			valid = True
	return(signIn())

#  Delete an existing account
def deleteAccount():
	global userLoginDatabase
	global tryAgain
	if not tryAgain:
		username = input('Enter a username to delete: ').strip()
	else:
		cls()
		print('Sorry, we couldn''t find that username in our database. Please try again.')
		username = input('Enter a username to delete: ').strip()
	#  If the given username already exists, then prompt the password before deleting the account
	if username in userLoginDatabase.keys():
		valid = False
		while not valid:
			cls()
			print('Username to delete: {}'.format(username))
			password = input('WARNING: This action cannot be reversed.\nEnter your password: ')
			if password == userLoginDatabase[username]:
				valid = True
			else:
				print('Sorry, that password is incorrect. Please try again.')
				time.sleep(2)
		userLoginDatabase.pop(username)
		with open('credentials.json', 'w') as outfile:
				json.dump(userLoginDatabase, outfile)
		print('Success! User {} deleted. Returning to main menu.'.format(username))
		time.sleep(2)
		return(False)
	else:
		tryAgain = True
		deleteAccount()

#  Sign in with an existing username and password
def signIn():
	global userLoginDatabase
	valid = False
	while not valid:
		username = input('Enter your username: ').strip()
		if username not in userLoginDatabase:
			cls()
			print('Sorry, that username does not exist. Please try again.')
			continue
		else:
			valid = True
	valid = False
	while not valid:
		cls()
		print('Username to login: {}'.format(username))
		password = input('Enter your password: ').strip()
		if password == userLoginDatabase[username]:
			print('Success! User {} logged in!'.format(username))
			time.sleep(2)
			valid = True
			return(True, username)
		else:
			cls()
			print('Sorry, that password is incorrect. Please try again.')


#  Reserve a room to study in
def bookRoom():
	global roomDatabase
	valid = False
	while not valid:
		cls()
		for possibleBuilding in roomDatabase:
			print(possibleBuilding)
		building = input('\nAbove are the available building(s).\nWhich building would you like to study in? ').strip()
		if building not in roomDatabase:
			print('Sorry, we couldn''t find that building in our database. Please try again, and double check your capitalization.')
			time.sleep(4)
			continue
		valid = True
	valid = False
	while not valid:
		cls()
		for possibleRoom in roomDatabase[building]['Vacant']:
			print(possibleRoom)
		room = input('\nAbove are the available room(s) in {}.\nWhich room would you like to study in? '.format(building)).strip()
		if room not in roomDatabase[building]['Vacant']:
			print('Sorry, we couldn''t find that room in our database. Please try again, and double check your capitalization')
			time.sleep(4)
			continue
		valid = True
	valid = False
	while not valid:
		if room in (roomDatabase[building]['Vacant']):
			roomDatabase[building]['Vacant'].remove(room)
			roomDatabase[building]['Occupied'].append(room)
			print('Congrats! You have successfully booked {} in {}'.format(room, building))
			time.sleep(2)
			with open('study_space.json', 'w') as outfile:
				json.dump(roomDatabase, outfile)
			valid = True
		else:
			print('Sorry, that room is not available at this time. Please try again.')
			time.sleep(2)

#  Check yourself out of a room
def leaveRoom():
	global roomDatabase
	valid = False
	while not valid:
		building = input('Which building are you currently in? ').strip()
		if building not in roomDatabase:
			print('Sorry, we couldn''t find that building in our database. Please try again, and double check your capitalization')
			time.sleep(4)
		else:
			valid = True
	room = input('Which room would you like to sign out? ').strip()
	while not valid:
		if room in (roomDatabase[building]['Occupied']):
			roomDatabase[building]['Occupied'].remove(room)
			roomDatabase[building]['Vacant'].append(room)
			print('You have successfully signed out of {} in {}.'.format(room,building))
			with open('study_space.json', 'w') as outfile:
				json.dump(roomDatabase, outfile)
			valid = True
		else:
			print('Sorry, that room appears to already be vacant. Please try again.')

#  Where the functions are called from, and where the program starts.
def main():
	# validCommand = False
	# while not validCommand:
	# 	cls()
	# 	account_option = input('Please enter one of the following commands:\ncreate-account\ndelete-account\nsign-in\n--> ').strip()
	# 	if account_option.lower() == 'create-account':
	# 		cls()
	# 		success = createAccount()
	# 		validCommand = True
	# 	elif account_option.lower() == 'sign-in':
	# 		cls()
	# 		success, username = signIn()
	# 		validCommand = True
	# 	elif account_option.lower() == 'delete-account':
	# 		cls()
	# 		success = deleteAccount()
	# 		validCommand = True
	# 	else:
	# 		print('Error: unrecognized command. Try again.')
	# 		time.sleep(2)
	success = True
	username = 'aidan'

	#  Successfully signed in: book or leave room
	if success:
		validCommand = False
		while not validCommand:
			cls()
			options = input('Please enter one of the following commands:\nbook-room\nleave-room\nmain-menu\n--> ').strip()
			if options.lower() == 'book-room':
				cls()
				bookRoom()
			elif options.lower() == 'leave-room':
				cls()
				leaveRoom()
			elif options.lower() == 'main-menu':
				print('User {} logged out. Now returning to main menu.'.format(username))
				time.sleep(3)
				main()
			else:
				print('Error: unrecognized command. Try again.')
				time.sleep(2)
	else:
		main()

main()