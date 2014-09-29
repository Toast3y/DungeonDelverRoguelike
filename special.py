import libtcodpy as libtcod

############################################################################################
#Room Cross pattern

def RoomCrossArray():
	pattern = [0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,3],[2,4],[3,1],[3,2],[3,3],[4,2]
	return pattern
	
	
def RoomCrossHeight():
	h = 5
	return h
	
def RoomCrossWidth():
	w = 5
	return w
	
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
	return