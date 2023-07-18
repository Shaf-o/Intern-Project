#Import Libraries
import time
from plyer import notification



if __name__ == "__main__":
    while True:
        # Create Notifier Function
        notification.notify(
            title = "ALERT",
            message = "Sir Please take a Break 5m! It has been an Hour...!",
            timeout = 2
        )
        # Add your required sleep time
        time.sleep(3600)
