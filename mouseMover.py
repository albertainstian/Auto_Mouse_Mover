import pyautogui
import time
import random


def auto_mouse_mover(interval=5):
    print("Auto Mouse Mover started. Press CTRL+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()

            # Move mouse slightly (random small offset)
            new_x = x + random.randint(-500, 500)
            new_y = y + random.randint(-50, 50)

            pyautogui.moveTo(new_x, new_y, duration=0.5)

            # Return back to original position
            pyautogui.moveTo(x, y, duration=0.5)

            time.sleep(interval)  # wait before next move
    except KeyboardInterrupt:
        print("\nStopped by user.")


if __name__ == "__main__":
    auto_mouse_mover(interval=5)