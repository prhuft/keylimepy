"""
test the key listener class
"""

from keylistener import KeyListener
import time

def on_key_press(key):
	"""handle keys other than the assigned quit key in the keylistener"""
	print(f"key {key} was pressed")
	
	if key == 'q':
		print("quitting")
	
if __name__ == "__main__":
	state = 0 
	
	keylistener = KeyListener(on_key_press)
	keylistener.start()
	
	while state == 0:
		time.sleep(0.1)
		if not keylistener.running:
			print("exiting loop")
			state = 1
		
		