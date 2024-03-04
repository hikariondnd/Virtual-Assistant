VirtualHikari.py
print("Welcome to your Virtual Office, (' + name + ') How may i assist you? ") 
pip install speechrecognition
sudo apt-get instal python3-pyaudio
pip install pyaudio
pip install pyttsx3
name in query = ""
def speak(audio):
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say(audio)
engine.runAndWait()

python3 -m venv <DIR>
source <DIR>/bin/activate

python3 -m virtualenv <DIR>
source <DIR>/bin/activate

    

def Take_query():
    Hello()
    while(True):
        query = takeCommand().lower()
        if "open google" in query:
            speak("Opening Gooogle ")
            webbrowser.open("www.google.com")
            continue
        elif  "Which day it is" in query:
            tellDay()
            continue
        elif "Tell me the time"
        tellTime()
        continue
        elif "bye" in query:
        speak("Bye! See you soon ")
        exit()
        elif "from Encyclopedia Britannica Online "
        speak("Checking Encyclopedia Britannica ")
        query = query.replace("Encyclopedia Britannica", "")
        result = encyclopediabritannica.summary(query, sentences=4)
        speak("According to Encyclopedia Britannica ")
        speak(result)

        elif "Tell me your name" in query:
            speak("I am Hikari. Your desktop Assistant")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            audio = r.listen(source)
            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language='en-in')
                print("The command is printed=", Query)
            except Exception as e:
                print(e)
                print("Could you repeat that for me, please?")
                return "None"
        return Query


def Hello():
    speak("Hello I am your desktop assistant Hikari. / How may I help you")
if __name__ == '__main__':
    Take_query()

# importing speech recognition from google api
import speech_recognition as sr 
import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver

num = 1
def assistant_speaks(output):
    global num
    num += 1
    print("Person : ", output)
    toSpeak = gTTS(text = output, lang='en', slow = False)
    file = str(num)+".mp3
    toSpeak.save(file)

def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")
        
        audio = rObject.listen(source, phrase_time_limit = 5)
    print("Stop.")

    try:
        
        text = rObject.recognize_google(audio, language ='en-US')
        print("You: ", text)
        return text

    except:
    
        assistant_speaks("Sorry. I didn't quite hear what you said. Could you repeat that again ?")
        return 0

 
 
# Driver Code
if __name__ == "__main__":
    assistant_speaks("What's your name, Human?")
    name ='Human'
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')
     
    while(1):
 
        assistant_speaks("What can i do for you?")
        text = get_audio().lower()
 
        if text == 0:
            continue
 
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "+ name+'.')
            break

        process_text(text)

   def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            search_web(input)
            return
 
        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Hikari. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return
 
        elif "who made you" in input or "created you" in input:
            speak = "I was refined and programmed by Gwyneth Mori."
            assistant_speaks(speak)
            return
 
 
        elif "calculate" in input.lower():
             
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id)
 
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
 
        elif 'open' in input:

            open_application(input.lower()) 
            return
 
        else:
 
            assistant_speaks("I can search the web for you, Would you like to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except :
 
        assistant_speaks("I don't understand, I can search the web for you, Would you like to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)     

def search_web(input):
    driver = webdriver.GoogleChrome()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():
        assistant_speaks("Opening in Youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query =" + '+'.join(query))
        return
    elif 'wikipedia' in input.lower()
        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
        elif 'search' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
            return
def open_application(input):
    if "chrome"in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Application\chrome.exe')
        return
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.starfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    else:
        assistant_speaks("Application not available")
        return

