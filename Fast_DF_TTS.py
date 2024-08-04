import os 
import subprocess
import tempfile
from playsound import playsound
import threading
# female voice :en-CA-ClaraNeural
# male voice: en-CA-LiamNeural
# male hindi voice : hi-IN-MadhurNeural
# female hindi voice : hi-IN-SwaraNeural
def speak(text:str,voice:str='en-CA-LiamNeural')->None:
    try:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as tmpfile:
            output_file=tmpfile.name
        command=f'edge-tts --voice {voice} --text "{text}" --write-media {output_file}'
        subprocess.run(command,shell=True,check=True)
        threading.Thread(target=playsound,args=(output_file,)).start()
    except Exception as e:
        print(e)

