# reverse Engeneering : it includes using request module to automate website and use its cookie to bypass and store its voice and use it.
import requests
from playsound import playsound
from typing import Union
import os
def generate_audio(message : str ,voice : str = "Brian"):
    url:str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"
    headers = {'User-Agent':'Mizilla/5.0(Maciontosh;intel Mac OS X 10_15_7)AppleWebkit/537.36(KHTM,like Gecoko)Chrome/119.0.0.0 Safari/537.36'}
    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None
def speak(message:str, voice: str = "Brian", folder: str = "" , extension: str = ".mp3") -> Union [None,str] :
    try:
        result_content=generate_audio(message,voice)
        file_path=os.path.join(folder,f"{voice}{extension}")
        with open(file_path,"wb") as file:
            file.write(result_content)
        playsound(file_path,"wb")
        os.remove(file_path)
        return None
    except Exception as e:
        print(e)

