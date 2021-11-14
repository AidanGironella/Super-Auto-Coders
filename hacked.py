import json
from bs4 import BeautifulSoup, NavigableString
import requests
import pandas as pd
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
	# URL = 'https://www.ualberta.ca/registrar/examinations/classroom-bookings/temporary-workspace-locations.html'
	# response = requests.get(URL)
	# html = response.content
	# soup = BeautifulSoup(html, 'html.parser')
	# table = soup.find('tbody')
	# for tr in table:
	# 	for td in tr:
	# 		print(td)
	# 	if isinstance(tr, NavigableString):
	# 		continue
	# 	print(tr.contents[1].text)
	# print(table)
	return outfile

outfile = create_db()
# create_db()
# with open('study_space.json', 'r') as openfile:
#     json_object = json.load(openfile)

# for vars in json_object:
# 	print(vars) 
# building = input('What is the building name?\n')

# print(json_object[building]['Vacant'])
# room = input('Which room would you like to study in?\n')

# if room in (json_object[building]['Vacant']):
# 	json_object[building]['Vacant'].remove(room)
# 	json_object[building]['Occupied'].append(room)
# 	print('You have successfully secured the '+room+' in the '+building+'.')
# 	with open('study_space.json', 'w') as outfile:
# 		json.dump(json_object, outfile)
# else:
# 	print('Invalid output')