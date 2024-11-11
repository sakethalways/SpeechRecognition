import speech_recognition as sr

def convert_voice_to_text():
    recognizer = sr.Recognizer()
    
    # Use the microphone as the source for input.
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise
        recognizer.energy_threshold = 300
        print("Ready! Please speak something...")

        # Capture the audio
        audio = recognizer.listen(source)

    try:
        # Use Google's Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from the Google Speech Recognition service.")

# Run the function
convert_voice_to_text()
