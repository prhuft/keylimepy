"""
key listening with matplotlib

this only works if a matplotlib figure is displayed
"""

import matplotlib.pyplot as plt
import time

state = 0

def startKeyListen():
	fig = plt.figure()
	# ax = fig.add_subplot(111)
	# fig.add_axes(ax)
	conn_id = fig.canvas.mpl_connect('key_press_event',onKeyPress)
	plt.ion() 
	plt.show()
	print("key listening service started")
	return fig, conn_id
	
def onKeyPress(event):
	global conn_id
	key = event.key
	if key != "ctrl+c":
		print(f"key {key} pressed")
	else:
		fig.canvas.mpl_disconnect(conn_id)
		print("key listening terminated")
		state == 1
		
if __name__ == "__main__":
	fig, conn_id = startKeyListen()

	while True:
		time.sleep(0.1)
		fig.canvas.flush_events()
		if state != 0:
			break
		
