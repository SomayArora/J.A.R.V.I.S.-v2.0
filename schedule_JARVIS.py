from datetime import datetime
import os
from winotify import Notification, audio
from os import getcwd

weekly_schedule = {
    "Monday": ["School from 7:30 AM to 12:30 PM", "Tution at 4 PM", "Self Study at 6 PM to 9 PM"],
    "Tuesday": ["School from 7:30 AM to 12:30 PM", "Tution at 5 PM", "Self Study at 6 PM to 9 PM"],
    "Wednesday": ["No School", "Tution at 4 PM", "Self Study at 6 PM to 9 PM", "Code review at 10 PM"],
    "Thursday": ["School from 7:30 AM to 12:30 PM", "Tution at 5 PM", "Self Study at 6 PM to 9 PM"],
    "Friday": ["School from 7:30 AM to 12:30 PM", "Tution at 4 PM", "Self Study at 6 PM to 9 PM"],
    "Saturday": ["Allen from 9 AM to 4 AM", "Code review at 8 PM"],
    "Sunday": ["Allen from 9 AM to 4 AM", "Code review at 8 PM"]
}


def tell_schedule(day=None):
    if not day:
        day = datetime.now().strftime("%A")

    tasks = weekly_schedule.get(day, [])

    if tasks:
        schedule_message = f"Your schedule for {day} is:\n" + "\n".join(tasks)
    else:
        schedule_message = f"No tasks scheduled for {day}."

    print(schedule_message)
    Alert(schedule_message)



def Alert(Text):
    icon_path = r"D:\J.A.R.V.I.S\logo.jpg"

    toast = Notification(
        app_id="🟢 J.A.R.V.I.S.",
        title=Text,
        duration="long",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)
    # toast.add_actions(label="Click me", launch="https://www.google.com")
    # toast.add_actions(label="Dismiss", launch="https://www.google.com")
    toast.show()

tell_schedule("Monday")