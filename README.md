# Keystroke Monitoring Tool (Project 3)

## Description

A Python-based keystroke monitoring tool that captures keyboard input and organizes it into structured sessions using inactivity-based detection.

This project focuses on understanding how input events are handled at the system level and how raw data can be transformed into meaningful behavioral logs.

---

## Features

* Session-based logging using inactivity timing
* Backspace handling for accurate reconstruction
* Noise filtering (ignores single-key logs)
* Duration tracking for each session
* Auto-save to prevent data loss on crash
* Structured and readable output format

---

## How It Works

* A session starts on the first key press
* Keystrokes are continuously recorded
* If no key is pressed for 10 seconds → session ends
* The session is saved with:

  * Start time
  * End time
  * Duration
  * Final reconstructed text

---

## Example Output

```
[18:47:56 - 18:48:33] (37s) hello im testing my key logger
```

---

## Project Structure

```
key-logger/
│── key-logger.py   # Main script
│── README.md       # Project documentation
│── .gitignore      # Ignored files (venv, logs, etc.)
```

---

## How to Run

```
git clone https://github.com/Ritzz-09/Key-logger.git
cd Key-logger

python3 -m venv venv
source venv/bin/activate

pip install pynput

python key-logger.py
```

---

## Tech Stack

* Python
* pynput (keyboard input handling)
* threading (background monitoring)

---

## Learning Outcomes

* Event-driven programming
* Handling system input events
* Threading and background processes
* File handling and structured logging
* Basic behavioral analysis concepts

---

## Future Improvements

* Log rotation to handle large files
* Active window tracking
* Encryption of stored logs
* Clipboard activity monitoring
* Export logs to structured formats (JSON/CSV)

---

## Disclaimer

This project is built strictly for educational purposes.
Do not use this tool on systems without proper authorization.
Unauthorized monitoring of user activity is illegal and unethical.
