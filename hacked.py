import json

#  Create database of buildings and rooms
def create_db():
    study_spaces = {
	'Athabasca Hall':{'Vacant': ['ATH 2-27'],'Occupied': []},
	'Augustana Campus Library':{'Vacant': ['Zone 1', 'Zone 2 BYOD', 'Zone 2 Computers'], 'Occupied': []},
	'Cameron Library':{'Vacant': ['2nd Floor Area 1', 'Basement Knowledge Common B-14D'],'Occupied': []},
	'Edmonton Clinic Health Academy':{'Vacant': ['ECHA 1-152', 'ECHA  1-153', 'ECHA 1-163', 'ECHA 1-436', 'ECHA 1-464',
		'EHCA 1-472', 'ECHA L1-230'],'Occupied': []},
	'Education Building':{'Vacant': ['ED 1-126', 'ED 1-128', 'ED 1-130', 'ED 106', 'ED 206', 'ED 221', 'ED 262',
		'ED 265', 'ED 377', 'ED B18', 'ED B19'],'Occupied': []},
	'General Services Building':{'Vacant': ['GSB 7-11', 'GSB 8-11'],'Occupied': []},
	'Humanities Centre':{'Vacant': ['HC 2-17', 'HC 2-19', 'HC 2-21'],'Occupied': []},
	'John W. Scott Health Sciences Library':{'Vacant': ['Basement Area 1', 'Basement Area 2'],'Occupied': []},
	'Rutherford Library':{'Vacant': ['4th Floor Area 1', '4th Floor Area 2'],'Occupied': []},
	'South Academic Building':{'Vacant': ['SAB 325', 'SAB 326', 'SAB 311', 'SAB 336', 'SAB 436'],'Occupied': []},
	}
    with open('study_space.json', 'w') as outfile:
        json.dump(study_spaces, outfile)
    return outfile

#  Create database of user login information
def create_pass_db():
    credentials = {'Bot': 'Bot'}
    with open('credentials.json', 'w') as outfile:
        json.dump(credentials, outfile)
    return outfile

outfile = create_db()
outfile_2 = create_pass_db()
with open('study_space.json', 'r') as openfile:
    roomDatabase = json.load(openfile)

sign_in = False
with open('credentials.json', 'r') as openfile:
        userLoginDatabase = json.load(openfile)

#  Create a new account
def createAccount():
	global userLoginDatabase
	valid = False
	while not valid:
		username = input('Enter a username: ').strip()
		password = input('Enter a password: ').strip()
		usernameList = []
		for i in userLoginDatabase:
			usernameList.append(i)
		#  If the given username already exists, then sign in instead
		if username in usernameList:
			print('Error: username already exists. Please sign in')
			valid = True #  valid code to sign in instead
		#  If the given username does not already exist, set up a new user
		else:
			userLoginDatabase[username]=password
			with open('credentials.json', 'w') as outfile:
				json.dump(userLoginDatabase, outfile)
			print('Account successfully created! Please sign in:')
			valid = True
	return(signIn())

#  Sign in with an existing username and password
def signIn():
	global userLoginDatabase
	valid = False
	while not valid:
		username = input('Enter your username: ').strip()
		if username not in userLoginDatabase:
			print('Error: username does not exist.')
			continue
		else:
			valid = True
	valid = False
	while not valid:
		password = input('Enter your password: ').strip()
		for users in userLoginDatabase:
			if username == users:
				if password == userLoginDatabase[users]:
					print('Success! User {} logged in!'.format(username))
					valid = True
					return(True)
				else:
					print('Error: Incorrect password')


#  Reserve a room to study in
def bookRoom():
	global roomDatabase
	valid = False
	while not valid:
		for possibleBuilding in roomDatabase:
			print(possibleBuilding)
		building = input('Above are the available buildings.\nWhich building would you like to study in? ').strip()
		if building not in roomDatabase:
			print('Sorry, we couldn''t find that building in our database. Please try again, and double check your capitalization.')
			continue
		valid = True
	valid = False
	while not valid:
		for possibleRoom in roomDatabase[building]['Vacant']:
			print(possibleRoom)
		room = input('Above are the available rooms.\nWhich room would you like to study in? ').strip()
		if room not in roomDatabase[building]['Vacant']:
			print('Sorry, we couldn''t find that room in our database. Please try again, and double check your capitalization')
			continue
		valid = True
	valid = False
	while not valid:
		if room in (roomDatabase[building]['Vacant']):
			roomDatabase[building]['Vacant'].remove(room)
			roomDatabase[building]['Occupied'].append(room)
			print('Congrats! You have successfully booked {} in {}'.format(room, building))
			with open('study_space.json', 'w') as outfile:
				json.dump(roomDatabase, outfile)
			valid = True
		else:
			print('Sorry, that room is not available at this time. Please try again.')

#  Check yourself out of a room
def leaveRoom():
	global roomDatabase
	valid = False
	while not valid:
		building = input('Which building are you currently in? ').strip()
		if building not in roomDatabase:
			print('Sorry, we couldn''t find that building in our database. Please try again, and double check your capitalization')
			continue
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

#  Meat and potatoes
account_option = input('Please enter one of the following commands:\ncreate-account\nsign-in\n--> ').strip()
validCommand = False
while not validCommand:
	if account_option.lower() == 'create-account':
		success = createAccount()
		validCommand = True
	elif account_option.lower() == 'sign-in':
		success = signIn()
		validCommand = True
	else:
		print('Error: unrecognized command. Try again.')

#  Successfully signed in: book or leave room
if success:
	options = input('Please enter one of the following commands:\nbook-room\nleave-room\n--> ').strip()
	if options.lower() == 'book-room':
		bookRoom()
	elif options.lower() == 'leave-room':
		leaveRoom()