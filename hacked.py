import json

def create_db():
	study_spaces = {"Rutherford":{"Vacant": ["Room 1", "2", "3", "4", "5"], "Occupied": ["x", "y", "z"]}, "ECHA":{"Vacant": ["Room 1", "Room 2"], "Occupied": ["Room x", "Room y"]}} 
	with open("study_space.json", "w") as outfile:
		json.dump(study_spaces, outfile)
	return outfile

#class make_change(study_spaces):
#	return study_sp


outfile = create_db()

# ----------------------------------------------
with open('study_space.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
print(type(json_object))
for vars in json_object:
  print(vars)
a="Rutherford"
print(json_object["Rutherford"]["Vacant"])
json_object["Rutherford"]["Vacant"].remove("2")
print(json_object["Rutherford"]["Vacant"])
print(type(json_object))

# -----------------------------------------------

with open('study_space.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
for vars in json_object:
  print(vars) 
building = input("What is the building name?")

print(json_object[building]["Vacant"])
room = input("Which room would you like to study in?")

if room in (json_object[building]["Vacant"]):
  json_object[building]["Vacant"].remove(room)
  json_object[building]["Occupied"].append(room)
  print("You have successfully secured the "+room+" in the "+building+".")
  with open("study_space.json", "w") as outfile:
    json.dump(json_object, outfile)
else:
  print("Invalid output")
