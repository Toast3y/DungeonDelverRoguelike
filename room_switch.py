import libtcodpy as libtcod
import special.py as roomPatterns

#Switch statements to fetch rooms and patterns as needed.

def fetchRoomPattern(roomNumber):
	options = {0: cross,
				1: chapel,
	}
	
	options[roomNumber]()
	
	def cross():
		return (roomPatterns.RoomCrossArray)
		
	def chapel():
		return (roomPatterns.RoomChapelArray)
		
###########################################################
	
def fetchRoomWidth(roomNumber):
	options = {0: cross,
				1: chapel,
	}
	
	options[roomNumber]()
	
	def cross():
		return (roomPatterns.RoomCrossWidth)
		
	def chapel():
		return (roomPatterns.RoomChapelWidth)
		
##############################################################
	
def fetchRoomHeight(roomNumber):
	options = {0: cross,
				1: chapel,
	}
	
	options[roomNumber]()
	
	def cross():
		return (roomPatterns.RoomCrossHeight)
		
	def chapel():
		return (roomPatterns.RoomChapelHeight)
		
################################################################
	
def fetchRoomHollow(roomNumber):
	options = {0: cross,
				1: chapel,
	}
	
	options[roomNumber]()
	
	def cross():
		return (roomPatterns.RoomCrossHollow)
		
	def chapel():
		return (roomPatterns.RoomChapelHollow)
	
#################################################################
##TODO: Fetch room centres, implement system to dictate whether it needs a special centre
#def fetch