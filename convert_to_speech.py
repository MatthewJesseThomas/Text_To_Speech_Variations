import pyttsx3

def convert_to_speech(text, lang='en', voice='default'):
    engine = pyttsx3.init()
    
    # Get all available voices
    voices = engine.getProperty('voices')
    
    # Set the desired language
    engine.setProperty('language', lang)
    
    # Select the desired voice
    selected_voice = None
    
    if voice == 'default':
        # Use the default voice for the selected language
        for v in voices:
            if v.languages[0] == lang:
                selected_voice = v
                break
    else:
        # Use the voice with the specified name
        for v in voices:
            if v.name == voice:
                selected_voice = v
                break
    
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
    else:
        print('Selected voice not found. Using the default voice.')
    
    engine.say(text)
    engine.runAndWait()

# Get all available voices
voices = pyttsx3.init().getProperty('voices')

# Display available voices
print("Available Voices:")
for v in voices:
    print(v.name)

# Prompt user input for the text to convert to speech
answer = input('What do you want to convert to speech: ')

# Prompt user input for the language (e.g., 'en' for English, 'fr' for French)
language = input('Enter the language code (default: en): ')

# Prompt user input for the voice name ('default' for default voice)
voice_name = input('Enter the voice name (default: default): ')

# Convert the input text to speech using the specified language and voice
convert_to_speech(answer, language, voice_name)
