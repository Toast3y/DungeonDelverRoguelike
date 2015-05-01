import libtcodpy as libtcod

############################################################################################
#Room Cross pattern

def RoomCrossArray():
	pattern = [0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,3],[2,4],[3,1],[3,2],[3,3],[4,2]
	return pattern
	
	
def RoomCrossHeight():
	return 5
	
def RoomCrossWidth():
	return 5
	
##Outdated, rooms should only care about their exit points instead of the approximate centre
def RoomCrossCenter(prev_x, prev_y, center_x, center_y):
	#If previous room is in top left relative to new room
	if (prev_x < center_x and prev_y < center_y):
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y-2)
		else:
			return (center_x-2, center_y)
	#If room is in bottom right
	elif (prev_x >= center_x and prev_y >= center_y):
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y+2)
		else:
			return (center_x+2, center_y)
	#If room is in bottom left relative to new room
	elif (prev_x < center_x and prev_y >= center_y):
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y+2)
		else:
			return (center_x-2, center_y)
	#If old room is in top right
	elif (prev_x >= center_x and prev_y < center_y):
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y-2)
		else:
			return (center_x+2, center_y)
	else:
		return (center_x, center_y)
		
##Outdated, room scripts should dictate the start of the level
def RoomCrossCenterStart(center_x, center_y):
	if libtcod.random_get_int(0, 0, 1) == 1:
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y-2)
		else:
			return (center_x-2, center_y)
	else:
		if libtcod.random_get_int(0, 0, 1) == 1:
			return (center_x, center_y+2)
		else:
			return (center_x+2, center_y)
			
def RoomCrossHollow():
	return False
			
####################################################################################################
#Chapel room pattern

def RoomChapelArray():
	pattern = [3,2],[7,2],[3,4],[7,4],[3,6],[7,6],[3,8],[7,8],[3,10],[7,10]
	return pattern
	
def RoomChapelHeight():
	return 12
	
def RoomChapelWidth():
	return 10
	
##Outdated, rooms should only care about their exit points instead of the approximate centre
def RoomChapelCenter(prev_x, prev_y, center_x, center_y):
	return (center_x, center_y-3)
	
##Outdated, room scripts should dictate the start of the level
def RoomChapelCenterStart(center_x, center_y):
	return (center_x, center_y+3)

def RoomChapelHollow():
	return True
	
########################################################################
#Chapel sideways room pattern
def RoomChapelSideArray():
	pattern = [2,3],[2,7],[4,3],[4,7],[6,3],[6,7],[8,3],[8,7],[10,3],[10,7]
	return pattern
	
def RoomChapelSideHeight():
	return 10
	
def RoomChapelSideWidth():
	return 12
	
##Outdated, rooms should only care about their exit points instead of the approximate centre
def RoomChapelSideCenter(prev_x, prev_y, center_x, center_y):
	return (center_x - 3, center_y)
	
##Outdated, room scripts should dictate the start of the level
def RoomChapelSideCenterStart(center_x, center_y):
	return (center_x + 3, center_y)
	
def RoomChapelSideHollow():
	return True
	
#########################################################################
#Square Room pattern
def RoomSquareArray():
	pattern = [2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[4,2],[4,3],[4,4]
	return pattern
	
def RoomSquareHeight():
	return 6
	
def RoomSquareWidth():
	return 6
	
##Outdated, rooms should only care about their exit points instead of the approximate centre
def RoomSquareCenter(prev_x, prev_y, center_x, center_y):
	#TODO: Add calculation to corners of square
	#if (prev_x <= center_x):
	return (center_x, center_y)
	
##Outdated, room scripts should dictate the start of the level
def RoomSquareCenterStart(center_x, center_y):
	return (center_x, center_y)
	
def RoomSquareHollow():
	return True