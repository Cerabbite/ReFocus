import keyboard
from pathlib import Path
from datetime import datetime


pressed = False
count = 0


def update_fugax():
    global count
    count += 1
    cur_time = datetime.now()
    filename = f"days/{datetime.today().strftime('%Y-%m-%d')}.refocus"
    if Path(filename).is_file():
        with open(filename, "a") as f:
            f.write(f"{cur_time}\n")
    else:
        print(f"Creating file {filename}")
        if count > 1:
            print(count)
        count = 1
        with open(filename, "w") as f:
            f.write(f"{cur_time}\n")
    print(cur_time)


keyboard.add_hotkey("f9", update_fugax)

try:
    keyboard.wait()
except:
    print(count)
