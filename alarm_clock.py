import datetime
import time

alarm_time=input("set alaram time (HH:MM in 24-hour format, e.g. 07:30):")
message=input("alarm message")
print("alarm set for",alarm_time)

while True:
    now=datetime.datetime.now().strftime("%H:%M")
    if now==alarm_time:
        print("\n⏰ ALARM!", message)
        for i in range(5):
            print("/a")
            time.sleep(1)
            break
        time.sleep(10)