"""
Below is a Python script that listens to the users voice input daily, asks
for their tasks, and updates the schedule. If no changes are mentioned, the user can say
"no changes to the schedule."
"""

# Requirements:
# 1. Install necessary libraries:
# pip install SpeechRecognition pyttsx3 datetime pyaudio

# 2. Script:
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up a speech recognizer
recognizer = sr.Recognizer()

# Sample task manager to store tasks
tasks = {}


# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen for speech input
def listen_for_task():
    with sr.Microphone() as source:
        print("Listening for your task...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google's speech recognition API
            task = recognizer.recognize_google(audio)
            print(f"You said: {task}")
            return task
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError as e:
            speak("Could not request results; check your internet connection.")
            return ""


# Function to update today's tasks
def update_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Hello, today is {today}. What tasks do you have for today?")
    print(f"Please speak your tasks for {today}.")

    # Get the task list from the user
    tasks_today = listen_for_task()

    if tasks_today.lower() == "no changes to the schedule":
        speak("No changes to the schedule today.")
        print("No changes to the schedule.")
    else:
        # Add or update tasks for today
        tasks[today] = tasks_today
        speak(f"Your tasks for today are: {tasks_today}")
        print(f"Tasks for {today}: {tasks_today}")


# Function to display today's tasks
def display_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if today in tasks:
        speak(f"Here are your tasks for today: {tasks[today]}")
        print(f"Today's tasks: {tasks[today]}")
    else:
        speak("You don't have any tasks for today.")
        print("No tasks for today.")


# Main loop to manage the task manager
def main():
    while True:
        speak("Would you like to update your tasks for today?")
        print("Would you like to update your tasks for today?")

        user_input = listen_for_task()

        if "yes" in user_input.lower():
            update_tasks()
        elif "no" in user_input.lower():
            speak("Okay, I'll check your tasks.")
            display_tasks()
        elif "exit" in user_input.lower():
            speak("Goodbye! Have a great day!")
            print("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Please say yes or no.")


if __name__ == "__main__":
    main()
