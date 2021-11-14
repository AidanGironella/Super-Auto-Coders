import json
with open('credentials.json', 'r') as openfile:
        userLoginDatabase = json.load(openfile)
user = input('User: ')
print(userLoginDatabase[user])
# password = input('Password: ')