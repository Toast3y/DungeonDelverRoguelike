#include PySFML
from PySFML import sf

#Create the main window
window = sf.RenderWindow(sf.VideoMode(1024, 768), "PySFML test")

#Create a string to display
text = sf.String("Hello SFML")

#Start the game loop
running = True
while running:
	event=sf.Event()
	while window.GetEvent(event):
		if event.Type == sf.Event.Closed:
			running = False
	
	#Clear screen, draw text, update window
	window.Clear()
	window.Draw(text)
	window.Display()