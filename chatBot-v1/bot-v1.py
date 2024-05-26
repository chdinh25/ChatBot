import pyttsx3
import speech_recognition
from datetime import date, datetime

# Initialize the speech recognizer
bot_ear = speech_recognition.Recognizer()
# Initialize the text-to-speech engine
speak = pyttsx3.init()
# Variable to store the response of the chat bot
thought = ""

# Use while loop to keep the bot running and listening
while True:
    # Listening
    with speech_recognition.Microphone() as mic:
        # Display a message of chat bot is working
        print("Robot: I'm listening")
        # Capturing the audio from the microphone
        audio = bot_ear.listen(mic)
    # DIsplay a message show that the bot is processing the speech
    print("Robot: ...")
    # Use try to catch any exceptions
    try:
        you = bot_ear.recognize_google(audio)
    except:
        you = ""
    # PDisplay user input
    print("You: " + you)

    # Understanding and generating a response based on the user's input
    # Use if-else to check text content and display the correspond
    if you == "":
        # If nothing was heard, prompt the user to try again
        thought = "I can't hear you, please try again"
    elif "hello" in you:
        # Respond to message contain the word "hello"
        thought = "Hello"
    elif "today" in you:
        # Respond to message contain the word "today"
        # Get today's date
        today = date.today()
        # Format the date in a readable way and store it in variable thought
        thought = today.strftime("%B %d, %Y")
    elif "time" in you:
        # Respond to message contain the word "time"
        # Get current time
        now = datetime.now()
        # Format the time and store it in variable thought
        thought = now.strftime("%H hours %M minutes %S second")
    elif "president" in you:
        # Respond to message contain the word "president"
        thought = "Joe Biden"
    elif "bye" in you:
        # Respond to "bye" and break the loop to stop the bot
        thought = "Good bye!"
        # Display the response
        print("Robot: " + thought)
        # Use the text-to-speech engine to say the response
        speak.say(thought)
        speak.runAndWait()
        # Break the loop to stop the chat bot
        break
    else:
        thought = "I'm good. How are you?"
    # Display the chat bot's response
    print("Robot: " + thought)

    # Speaking the response using the text-to-speech engine
    speak.say(thought)
    speak.runAndWait()