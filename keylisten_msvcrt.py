import msvcrt
import time

num = 0
done = False
while not done:
	time.sleep(.1)
	print(num)
	num += 1

	if msvcrt.kbhit():
		key = msvcrt.getch()
		print(f"you pressed {msvcrt.getch()} so now i will quit")
		done = True