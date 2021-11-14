import json


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
    with open("study_space.json", "w") as outfile:
        json.dump(study_spaces, outfile)
    return outfile
#creating library database

# class make_change(study_spaces):
#	return study_sp
def create_pass_db():
    credentials = {"Bot": "Bot"}
    with open("credentials.json", "w") as outfile:
        json.dump(credentials, outfile)
    return outfile
#creating username info database

outfile = create_db()
outfile_2 = create_pass_db()

# --------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------

with open('study_space.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
for vars in json_object:
    print(vars)

sign_in = False
#initializing sign_in boolean value

account_option = input("create-account or sign-in?")
if account_option == "create-account":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('credentials.json', 'r') as openfile:
        # Reading from json file
        json_credentials = json.load(openfile)
        username_list = []
        for i in json_credentials:
            username_list.append(i)
        if username in username_list:
            #if it exists, sign in
            print("username already exists, please sign in")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username not in json_credentials:
                print("username doesn't exist")
            for m in json_credentials:
                if username == m:
                    if password == json_credentials[m]:
                        sign_in = True
                    else:
                        print("wrong password")
        else:
            #if it doesn't exist, add it to user database
            json_credentials[username]=password
            with open("credentials.json", "w") as outfile:
                json.dump(json_object, outfile)
            print("account created, please sign in")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username not in json_credentials:
                print("username doesn't exist")
            for m in json_credentials:
                if username == m:
                    if password == json_credentials[m]:
                        sign_in = True
                    else:
                        print("wrong password")

    #check if the key already exists
elif account_option == "sign-in":
    #sign in function
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('credentials.json', 'r') as openfile:
        # Reading from json file
        json_credentials = json.load(openfile)
        if username not in json_credentials:
            print("username doesn't exist")
        for m in json_credentials:
            if username == m:
                if password == json_credentials[m]:
                    sign_in = True
                else:
                    print("wrong password")

else:
    print("error")


#create an account
#sign in with username and pass word

if sign_in == True:
    #reserve room or sign out
    options = input("sign-in room or sign-out room?")
    if options == "sign-in":
        building = input("What is the building name?")

        print(json_object[building]["Vacant"])
        room = input("Which room would you like to study in?")

        if room in (json_object[building]["Vacant"]):
            json_object[building]["Vacant"].remove(room)
            json_object[building]["Occupied"].append(room)
            print("You have successfully secured the " + room + " in the " + building + ".")
            with open("study_space.json", "w") as outfile:
                json.dump(json_object, outfile)
        else:
            print("Invalid output")
    elif options == "sign-out":
        building = input("What is the building name?")

        print(json_object[building]["Occupied"])
        room = input("Which room would you like to sign out?")

        if room in (json_object[building]["Occupied"]):
            json_object[building]["Occupied"].remove(room)
            json_object[building]["Vacant"].append(room)
            print("You have successfully signed out the " + room + " in the " + building + ".")
            with open("study_space.json", "w") as outfile:
                json.dump(json_object, outfile)
        else:
            print("Invalid output")
    else:
        print("Invalid input")

else:
    print("please sign in or create your account first")
