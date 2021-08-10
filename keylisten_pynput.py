from pynput import keyboard
import time

def on_key_press(key):
	try:
		print(f'alphanumeric key {key.char} pressed')
	except AttributeError:
		print(f'special key {key} pressed')
		
def on_release(key):
	global state
	print('{key} released')
	if key == keyboard.Key.esc:
		# update the loop state
		state = 1
		# Stop listener
		return False
		
if __name__ == "__main__":
	
	state = 0 # running state

	listener = keyboard.Listener(on_press=on_key_press, on_release=on_release)
	listener.start()
	
	while True:
		time.sleep(0.1)
		
		if state != 0:
			break