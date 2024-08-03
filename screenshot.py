#takes a screenshot when you press the 'k' key. Press 'q' to quit.
#no errors here!

import pyautogui
import keyboard
import datetime

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot_{timestamp}.png")
    print(f"Screenshot saved as screenshot_{timestamp}.png")

def main():
    print("Press 'k' to take a screenshot. Press 'q' to quit.")
    
    while True:
        try:
            if keyboard.is_pressed('k'):
                take_screenshot()
                # Wait for the 'k' key to be released to avoid multiple screenshots on a single press
                keyboard.release('k')
            elif keyboard.is_pressed('q'):
                print("Exiting the program.")
                break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
