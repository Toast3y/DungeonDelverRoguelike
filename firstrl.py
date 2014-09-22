import libtcodpy as libtcod

#Handle screen size and fps
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#Handle map size for displays
MAP_WIDTH = 80
MAP_HEIGHT = 45

#Handle room size and number
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

#Handle FOV and Light Radius
FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

#tile colours
colour_dark_wall = libtcod.Color(0, 0, 100)
colour_light_wall = libtcod.Color(130, 110, 50)
colour_dark_ground = libtcod.Color(50, 50, 150)
colour_light_ground = libtcod.Color(200, 180, 50)


class Tile:
	#A map tile
	def __init__(self, blocked, block_sight = None):
		self.blocked = blocked
		
		#If a tile is blocked, it also blocks sight
		if block_sight is None: block_sight = blocked
		self.block_sight = block_sight
		

class Object:
	#Generic object to represent any thing in the game world
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		
	def move(self, dx, dy):
		#Move by the given amount as long as square is not blocked
		if not map[self.x + dx][self.y + dy].blocked:
			self.x += dx
			self.y += dy
		
	def draw(self):
		if (libtcod.map_is_in_fov(fov_map, self.x, self.y)):
			libtcod.console_set_default_foreground(con, self.color)
			libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
		
	def clear (self):
		#Deletes the object in the game space
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
		

class Rect:
	#Rectangle on the map, used to characterize a room
	def __init__(self, x, y, w, h):
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h
		
	def center(self):
		center_x = (self.x1 + self.x2) / 2
		center_y = (self.y1 + self.y2) / 2
		return (center_x, center_y)
		
	def intersect(self, other):
		#returns true if this rectangle intersects another one by accident
		return (self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1)
		
		
def create_room(room):
	global map
	#Go through the tiles in the rectangle and make them passable.
	for x in range(room.x1 + 1, room.x2):
		for y in range(room.y1 + 1, room.y2):
			map[x][y].blocked = False
			map[x][y].block_sight = False
			
			
def create_h_tunnel(x1, x2, y):
	#Horizontal tunnel
	global map
	for x in range(min(x1, x2), max(x1, x2) + 1):
		map[x][y].blocked = False
		map[x][y].block_sight = False
		
		
def create_v_tunnel(y1, y2, x):
	#Vertical tunnel
	global map
	for y in range(min(y1, y2), max(y1, y2) + 1):
		map[x][y].blocked = False
		map[x][y].block_sight = False
		
		
def make_map():
	global map
	
	#Fill map with "blocked tiles"
	map = [[ Tile(True)
		for y in range(MAP_HEIGHT) ]
			for x in range(MAP_WIDTH) ]
			
	#Randomly generate a list of rooms
	rooms = []
	num_rooms = 0
	
	for r in range(MAX_ROOMS):
		#random width and height
		w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		#random position within boundaries of the map
		x = libtcod.random_get_int(0, 0, MAP_WIDTH - w - 1)
		y = libtcod.random_get_int(0, 0, MAP_HEIGHT - h - 1)
		
		#Use Rect to create a new room
		new_room = Rect(x, y, w, h)
		
		#Check if the new room intersects an old one
		failed = False
		for other_room in rooms:
			if new_room.intersect(other_room):
				failed = True
				break
				
		if not failed:
			#If the room is valid and doesn't intersect
			create_room(new_room)
			
			#center coordinates of new room
			(new_x, new_y) = new_room.center()
			
			if num_rooms == 0:
				#First room generated, player start here
				player.x = new_x
				player.y = new_y
			else:
				#All rooms after the first, connect to previous room with a tunnel
				(prev_x, prev_y) = rooms[num_rooms-1].center()
				
				if libtcod.random_get_int(0, 0, 1) == 1:
					create_h_tunnel(prev_x, new_x, prev_y)
					create_v_tunnel(prev_y, new_y, new_x)
				else:
					create_v_tunnel(prev_y, new_y, prev_x)
					create_h_tunnel(prev_x, new_x, new_y)
					
			rooms.append(new_room)
			num_rooms += 1
	
	
def render_all():
	global fov_map, colour_dark_wall, colour_light_wall, colour_dark_ground, colour_light_ground, fov_recompute

	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			visible = libtcod.map_is_in_fov(fov_map, x, y)
			wall = map[x][y].block_sight
			
			if not visible:
			#Can't be seen by the player
				if wall:
					libtcod.console_set_char_background(con, x, y, colour_dark_wall, libtcod.BKGND_SET )
				else:
					libtcod.console_set_char_background(con, x, y, colour_dark_ground, libtcod.BKGND_SET )
			else:
				if wall:
					libtcod.console_set_char_background(con, x, y, colour_light_wall, libtcod.BKGND_SET)
				else:
					libtcod.console_set_char_background(con, x, y, colour_light_ground, libtcod.BKGND_SET)
				
	#Draw all objects in the object list
	for object in objects:
		object.draw()
	
	#Blit the contents of con to root console
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	
	
	
#Handle all keys in the game.
def handle_keys():
	global playerx, playery
	
	key = libtcod.console_wait_for_keypress(True)
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		#Alt + Enter: Toggle Fullscreen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
		
	elif key.vk == libtcod.KEY_ESCAPE:
		#Exit the game
		return True
	
	#movement keys
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)
		fov_recompute = True
		#playery -= 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
		fov_recompute = True
		#playery += 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
		fov_recompute = True
		#playerx -= 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)
		fov_recompute = True
		#playerx += 1


#############
#Init and Main loop
#############

#Load fonts
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

#Initialize window
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutes', False)

con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#Make the player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
#Make an NPC
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
#Define all objects to be rendered
objects = [npc, player]
#Create the map
make_map()

#Create an FOV map according to generated map
fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        libtcod.map_set_properties(fov_map, x, y, not map[x][y].block_sight, not map[x][y].blocked)
		
fov_recompute = True
		
#Main display loop
while not libtcod.console_is_window_closed():
	render_all()	
	
	libtcod.console_flush()
	
	for object in objects:
		object.clear()
	
	exit = handle_keys()
	if exit:
		break
		
