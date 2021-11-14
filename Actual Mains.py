import time
localtime = time.asctime( time.localtime(time.time()) )

with open('study_space.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
for vars in json_object:
    print(vars)

with open('credentials.json', 'r') as openfile:
    # Reading from json file
    json_credentials = json.load(openfile)

sign_in = False
#initializing sign_in boolean value

account_option = input("To create-account, press 0 \nTo sign-in, press 1?")
if account_option == "0":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    username_list = []
    for i in json_credentials:
        username_list.append(i)
    if username in username_list:
            #if it exists, sign in
        print("username already exists, please sign in")
    else:
            #if it doesn't exist, add it to user database
      json_credentials[username]=password
      with open("credentials.json", "w") as outfile:
            json.dump(json_credentials, outfile)
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
elif account_option == "1":
    #sign in function
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
    print("error")


#create an account
#sign in with username and pass word

if sign_in == True:
    #reserve room or sign out
    options = input("sign-in room or sign-out room?")
    if options == "sign-in":
        building = input("What is the building name?")

        print(json_object[building]["Vacant"])
        if (json_object[building]["Vacant"]) != []:
          room = input("Which room would you like to sign in?")
        else:
          print("Sorry, no study space is currently available in "+ building)

        if room in (json_object[building]["Vacant"]):
            json_object[building]["Vacant"].remove(room)
            json_object[building]["Occupied"].append(room)
            print(username+" has successfully secured the " + room + " in the " + building + " at "+ localtime)
            with open("study_space.json", "w") as outfile:
                json.dump(json_object, outfile)
        else:
            print("Invalid output")
    elif options == "sign-out":
        building = input("What is the building name?")

        print(json_object[building]["Occupied"])
        if (json_object[building]["Occupied"]) != []:
          room = input("Which room would you like to sign out?")
        else:
          print("All the study spaces are vacant in "+ building)

        if room in (json_object[building]["Occupied"]):
            json_object[building]["Occupied"].remove(room)
            json_object[building]["Vacant"].append(room)
            print(username+" has successfully signed out the " + room + " in the " + building + " at "+ localtime)
            with open("study_space.json", "w") as outfile:
                json.dump(json_object, outfile)
        else:
            print("Invalid output")
    else:
        print("Invalid input")

else:
    print("please sign in or create your account first")
