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
with open('statuses.json', 'r') as openfile:
        userStatuses = json.load(openfile)

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
			print('Account successfully created! Logging in as {}...'.format(username))
			time.sleep(2)
			return(True, username)
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
	if not userLoginDatabase:
		print('There are currently no users in the database. Please create an account first.')
		time.sleep(3)
		return(False, '')
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
			time.sleep(2)


#  Reserve a room to study in. Returning True will return the user to the previous menu.
def bookRoom(username):
	global roomDatabase
	valid = False
	if username in userStatuses.keys():
		print('You are currently signed into {}. Please sign out of this room before booking another one.'.format(userStatuses[username]))
		print('Returning to menu...')
		time.sleep(4)
		return(True)
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
	#  Valid building successfully chosen - proceed
	valid = False
	while not valid:
		cls()
		if not roomDatabase[building]['Vacant']:
			print('Sorry, all rooms in {} are currently occupied. Returning to menu...'.format(building))
			time.sleep(2)
			return(True)
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
			userStatuses[username] = room
			print('Congrats! You have successfully booked {} in {}'.format(room, building))
			print('Returning to menu...')
			time.sleep(2)
			with open('study_space.json', 'w') as outfile:
				json.dump(roomDatabase, outfile)
			with open('statuses.json', 'w') as outfile:
				json.dump(userStatuses, outfile)
			valid = True
			return(True)
		else:
			print('Sorry, that room is not available at this time. Please try again.')
			time.sleep(2)

#  Check yourself out of a room. Returning True will return the user back to the menu.
def leaveRoom(username):
	global roomDatabase
	global userStatuses
	valid = False
	menu = False
	if username not in userStatuses.keys():
		print('You are not currently signed into a room. Please book a room before trying to leave one.')
		print('Returning to menu...')
		time.sleep(4)
		return(True)
	while not valid:
		cls()
		for possibleBuilding in roomDatabase:
			print(possibleBuilding)
		building = input('\nAbove are all the buildings.\nWhich building are you currently in? ').strip()
		if building not in roomDatabase:
			print('Sorry, we couldn''t find that building in our database. Please try again, and double check your capitalization')
			time.sleep(4)
		elif not roomDatabase[building]['Occupied']:
			print('All rooms in {} are currently vacant. Returning to main menu.'.format(building))
			time.sleep(3)
			valid = True
			return(True)
		else:
			valid = True
	#  Valid room selected - proceed.
	valid = False
	while not valid:
		cls()
		for rooms in roomDatabase[building]['Occupied']:
			print(rooms)
		room = input('Above are the currently occupied rooms.\nWhich room would you like to sign out? ').strip()
		if room in (roomDatabase[building]['Occupied']):
			roomDatabase[building]['Occupied'].remove(room)
			roomDatabase[building]['Vacant'].append(room)
			userStatuses.pop(username)
			print('You have successfully signed out of {} in {}.'.format(room,building))
			time.sleep(2)
			with open('study_space.json', 'w') as outfile:
				json.dump(roomDatabase, outfile)
			with open('statuses.json', 'w') as outfile:
				json.dump(userStatuses, outfile)
			valid = True
			return(False)
		elif room in roomDatabase[building]['Vacant']:
			print('Sorry, that room appears to already be vacant. Please try again.')
			time.sleep(3)
		elif room not in roomDatabase[building]['Vacant'] or room not in roomDatabase[building]['Occupied']:
			print('Sorry, we couldn''t find that room in our database. Please try again, and double check your capitalization.')
			time.sleep(4)
		else:
			print('Other error. Please try again')
			time.sleep(2)

#  Where the functions are called from, and where the program starts.
def login():
	validCommand = False
	while not validCommand:
		cls()
		print('Welcome to the UofA Study Space Booking Tool!')
		account_option = input('\nPlease enter one of the following commands:\n\ncreate-account\ndelete-account\nsign-in\nexit\n--> ').strip()
		if account_option.lower() == 'create-account':
			cls()
			success, username = createAccount()
			validCommand = True
		elif account_option.lower() == 'sign-in':
			cls()
			success, username = signIn()
			validCommand = True
		elif account_option.lower() == 'delete-account':
			cls()
			success = deleteAccount()
			username = ''
			validCommand = True
		elif account_option.lower() == 'exit':
			print('Thanks for using the UofA Study Space Booking Tool!')
			return
		else:
			print('Error: unrecognized command. Try again.')
			time.sleep(2)
	# success = True
	# username = 'aidan'
	main(success, username)

#  Successfully signed in: book or leave room
def main(success, username):
	if success:
		validCommand = False
		while not validCommand:
			cls()
			options = input('Please enter one of the following commands:\nbook-room\nleave-room\nmain-menu\nexit\n--> ').strip()
			if options.lower() == 'book-room':
				cls()
				menu = bookRoom(username)
				if menu:
					main(True, username)
			elif options.lower() == 'leave-room':
				cls()
				menu = leaveRoom(username)
				if menu:
					main(True, username)
			elif options.lower() == 'main-menu':
				print('User {} logged out. Now returning to main menu.'.format(username))
				time.sleep(3)
				login()
			elif options.lower() == 'exit':
				print('Thanks for using the UofA Study Space Booking Tool!')
				return
			else:
				print('Error: unrecognized command. Try again.')
				time.sleep(2)
	else:
		login()

login()
