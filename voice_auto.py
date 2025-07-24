import speech_recognition as sr
import pyautogui
import os
import webbrowser
import time

# Function to recognize speech and return the command
def recognize_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Function to open applications based on the command
def open_application(command):
    if 'notepad' in command:
        os.system('notepad')
    elif 'calculator' in command:
        os.system('calc')
    elif 'browser' in command:
        os.system('start chrome')  # Change 'chrome' to your preferred browser
    elif 'word' in command:
        os.system('start winword')  # For Microsoft Word
    elif 'youtube' in command and 'play' in command:
        song = command.split("play")[-1].strip()
        play_youtube_song(song)
    elif 'open' in command:
        site = command.split("open")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={site}")
    elif 'close' in command:
        close_application(command)
    else:
        print("Command not recognized. Please try again.")

# Function to close applications based on the command
def close_application(command):
    if 'notepad' in command:
        os.system('taskkill /im notepad.exe /f')
    elif 'calculator' in command:
        os.system('taskkill /im calc.exe /f')
    elif 'chrome' in command:
        os.system('taskkill /im chrome.exe /f')
    elif 'word' in command:
        os.system('taskkill /im winword.exe /f')
    elif 'youtube' in command:
        os.system('taskkill /im chrome.exe /f')  # Assuming YouTube is opened in Chrome
    else:
        print("No application matched to close.")

# Function to play a song on YouTube
def play_youtube_song(song):
    url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
    webbrowser.open(url)
    print(f"Playing {song} on YouTube.")
    time.sleep(5)  # Wait for a few seconds before listening for the close command
    while True:
        command = recognize_command()
        if command and 'close' in command:
            print("Closing YouTube.")
            os.system('taskkill /im chrome.exe /f')  # Close Chrome or the browser used
            break

# Main loop
if __name__ == "__main__":
    while True:
        command = recognize_command()
        if command:
            open_application(command)

