import time
from plyer import notification
while True:
  notification.notify(title="DeHydration Alert",
                      message="You need to drink some water")
  time.sleep(5)
