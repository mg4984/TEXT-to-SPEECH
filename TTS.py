from gtts import gTTS
import os

# Set the text to be spoken
text = "Hello, how are you doing?"

# Create a gTTS object with the text and language
language = 'en'
tts = gTTS(text=text, lang=language)

# Save the speech as an MP3 file
filename = 'output.mp3'
tts.save(filename)

# Play the MP3 file using the default media player
if os.name == 'nt':
    os.startfile(filename)
else:
    os.system('xdg-open ' + filename)
