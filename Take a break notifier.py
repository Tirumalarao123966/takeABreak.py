## "Take a Break" Notification system in Python

from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\\Ampeross-Qetto-2-Timer.ico",
        timeout = 10,
    )






if __name__ == '__main__':
    while True:
        notifyMe("Hey User, take a break now !!", "You should follow the 20-20-20 rule to keep your eyes healthy")
        time.sleep(1200)

    
        
