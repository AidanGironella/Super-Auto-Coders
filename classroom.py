import json

class classroom:
	def __init__(self, room_number, whiteboard, chair, desk, computer, cafe):
		self.room_number = room_number
		self.whiteboard = whiteboard
		self.chair = chair
		self.desk = desk
		self.computer = computer
		self.cafe = cafe
		
	def print_features(self):
		print(room_number)
		print("whiteboard: "+whiteboard)
		print("chair: "+chair)
		print("desk: "+desk)
		print("computer: "+computer)
		print("cafe: "+cafe)
  
  rm_1 = classroom("Rutherford RM_1", "YES", "YES", "YES", "YES", "Tim Hortons")
  rm_2 = classroom("Rutherford RM_2", "NO", "YES", "YES", "NO", "Tim Hortons")
  rm_3 = classroom("Rutherford RM_3", "YES", "YES", "YES", "NO", "Tim Hortons")

  eroom_1 = classroom("ECHA RM_1", "YES", "YES", "YES", "NO", "Tim Hortons")
  eroom_2 = classroom("ECHA RM_2", "NO", "YES", "YES", "YES", "Tim Hortons")
  eroom_3 = classroom("ECHA RM_3", "YES", "YES", "YES", "NO", "Tim Hortons")