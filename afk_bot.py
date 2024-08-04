import pyautogui as pgi
import random
import threading
import time
from pynput import keyboard


running = True
def afk_bot():
    while running:

            x = random.randint(50, 1200)
            y = random.randint(100, 600)
            pgi.moveTo(x, y, 0.50)
            time.sleep(0.5)

print("Bot is running...")
time.sleep(1)
def on_press(key):
    global running
    print(f"Key {key} pressed, stopping the bot.")
    running = False

bot_thread = threading.Thread(target=afk_bot)
bot_thread.start()

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

bot_thread.join()
keyboard_listener.stop()

print("AFK bot has stopped.")
if __name__ == "__main__":
    afk_bot()
