# AFKBot
This is a simple AFK (Away From Keyboard) bot implemented in Python. The bot moves the mouse cursor to random positions on the screen at regular intervals to simulate user activity and prevent the computer from going into idle mode.

Features

	•	Moves the mouse cursor to random positions on the screen.
	•	Runs in a separate thread, allowing it to operate in the background.
	•	Listens for keyboard input to stop the bot.

Requirements

	•	Python 3.x
	•	pyautogui library
	•	pynput library

Installation

	1.	Clone this repository or download the script.
	2.	Install the required libraries using pip:
      		pip install pyautogui pynput

Usage

	1.	Run the script:
      		python afk_bot.py
  	2.	The bot will start moving the mouse cursor randomly on the screen and print “Bot is running…”.
	3.	To stop the bot, press any key. The bot will stop and print “AFK bot has stopped.”.


Detailed Explanation

	•	Imports:
	•	pyautogui: Used for moving the mouse cursor.
	•	random: Used for generating random coordinates for the mouse cursor.
	•	threading: Used for running the bot in a separate thread.
	•	time: Used for sleep intervals.
	•	pynput.keyboard: Used for listening to keyboard input.
	•	Global Variable:
	•	running: A boolean variable to control the bot’s running state.
	•	afk_bot Function:
	•	Continuously moves the mouse cursor to random positions on the screen every 0.5 seconds.
	•	on_press Function:
	•	Stops the bot when any key is pressed.
	•	Main Execution:
	•	Starts the afk_bot function in a separate thread.
	•	Starts the keyboard listener in another thread to listen for key presses.
	•	Waits for the bot to stop and then stops the keyboard listener.

