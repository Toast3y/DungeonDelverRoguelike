import libtcodpy as libtcod
import special as roomPatterns

#Switch statements to fetch rooms and patterns as needed.

def fetchRoomPattern(roomNumber):
	def cross():
		return (roomPatterns.RoomCrossArray())
		
	def chapel():
		return (roomPatterns.RoomChapelArray())
		
		
	options = {0: cross,
				1: chapel,
	}
	
	pattern = options[roomNumber]()
	
	return pattern
	
	
		
###########################################################
	
def fetchRoomWidth(roomNumber):
	def cross():
		return int(roomPatterns.RoomCrossWidth())
		
	def chapel():
		return int(roomPatterns.RoomChapelWidth())
	
	options = {0: cross,
				1: chapel,
	}
	
	width = options[roomNumber]()
	
	return width
	
	
		
##############################################################
	
def fetchRoomHeight(roomNumber):
	def cross():
		return int(roomPatterns.RoomCrossHeight())
	
	def chapel():
		return int(roomPatterns.RoomChapelHeight())
		
		
	options = {0: cross,
				1: chapel,
	}
	
	height = options[roomNumber]()
	
	return height
	
	
		
################################################################
	
def fetchRoomHollow(roomNumber):
	def cross():
		return (roomPatterns.RoomCrossHollow())
		
	def chapel():
		return (roomPatterns.RoomChapelHollow())

	options = {
		0: cross,
		1: chapel,
	}
	
	hollow = options[roomNumber]()
	
	return hollow
	
	
	
#################################################################
##TODO: Fetch room centres, implement system to dictate whether it needs a special centre
def fetchRoomCenter(roomNumber, prev_x, prev_y, new_x, new_y):
	def cross(prev_x, prev_y, new_x, new_y):
		return (roomPatterns.RoomCrossCenter(prev_x, prev_y, new_x, new_y))
		
	def chapel(prev_x, prev_y, new_x, new_y):
		return (roomPatterns.RoomChapelCenter(prev_x, prev_y, new_x, new_y))
		
	options = {
		0: cross,
		1: chapel,
	}
	
	(return_x, return_y) = options[roomNumber](prev_x, prev_y, new_x, new_y)
	
	return (return_x, return_y)
	
	
#################################################################
##TODO: Fetch Room Center starts for player starts.
def fetchRoomCenterStart(roomNumber, center_x, center_y):
	def cross(center_x, center_y):
		return (roomPatterns.RoomCrossCenterStart(center_x, center_y))
	
	def chapel(center_x, center_y):
		return (roomPatterns.RoomChapelCenterStart(center_x, center_y))
		
	options = {
		0: cross,
		1: chapel,
	}
	
	(return_x, return_y) = options[roomNumber](center_x, center_y)
	
	return(return_x, return_y)