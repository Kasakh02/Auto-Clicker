import time
import threading
import os
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

onOff = KeyCode(char="b")

running = True
clicking = False
mouse = Controller()

def clicker():
    while running:
        if clicking:
            mouse.click(Button.left, 1)
            event.wait(timeout=5)
            event.clear()


def toggle_onOff(key):
	if key == onOff:
		global clicking
		clicking = not clicking
		if clicking:
			print("🟢 Clicking...")
			cmd = 'tell application "System Events" to display dialog "Clicking started. Press OK or close this window to stop." with title "Clicking" with icon note giving up after 864000'
			res = os.system(f"osascript -e '{cmd}'")
			if res == 0:
				clicking = False
				stop()
				event.set()
				clickThread.join()
				print("🛑 Clicking stopped.")



def stop():
    global running
    running = False

event = threading.Event()
clickThread = threading.Thread(target=clicker)
clickThread.start()

with Listener(on_press=toggle_onOff) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

stop()
event.set()
clickThread.join()
print("⛔️ Program stopped by user...!")