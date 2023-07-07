import pyttsx3
from gtts import gTTS
import os

def convert_to_speech(text, lang='en', voice='default'):
    engine = pyttsx3.init()
    
    # Get all available voices for pyttsx3
    pyttsx3_voices = engine.getProperty('voices')
    
    # Set the desired language for pyttsx3
    engine.setProperty('language', lang)
    
    # Select the desired voice for pyttsx3
    selected_voice = None
    
    if voice == 'default':
        # Use the default voice for the selected language for pyttsx3
        for v in pyttsx3_voices:
            if v.languages[0] == lang:
                selected_voice = v
                break
    else:
        # Use the voice with the specified name for pyttsx3
        for v in pyttsx3_voices:
            if v.name == voice:
                selected_voice = v
                break
    
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
    else:
        print('Selected voice not found for pyttsx3. Using the default voice.')
    
    engine.say(text)
    engine.runAndWait()

# Get all available voices for pyttsx3
pyttsx3_voices = pyttsx3.init().getProperty('voices')

# Display available voices for pyttsx3
print("Available Voices for pyttsx3:")
for v in pyttsx3_voices:
    print(v.name)

# Prompt user input for the text to convert to speech
answer = input('What do you want to convert to speech: ')

# Prompt user input for the language (e.g., 'en' for English, 'fr' for French)
language = input('Enter the language code (default: en): ')

# Prompt user input for the voice name ('default' for default voice)
voice_name = input('Enter the voice name (default: default): ')

# Convert the input text to speech using pyttsx3
convert_to_speech(answer, language, voice_name)

# Convert the input text to speech using gTTS
tts = gTTS(text=answer, lang=language)
tts.save("output.mp3")
os.system("mpg123 output.mp3")  # Use a media player to play the audio file
