import speech_recognition as sr
import datetime
import webbrowser
import time
import geocoder as geol
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print("You said : "+voice_data)
            SpeakText("You said : "+voice_data)
        except sr.UnknownValueError():
            print("Sorry, could not recognize your voice")
            SpeakText("Sorry could not recognize your voice")
        except sr.RequestError():
            print("Sorry, my spech service is down")
            SpeakText("Sorry, my speech service is down")
        return voice_data


def webSearch():
    search = record_audio('What do you want to search for?')
    SpeakText('What do you want to search for?')
    url = 'https://google.com/search?q='+search
    webbrowser.get().open(url)
    SpeakText('Here is what I found for '+search)
    print('Here is what I found for '+search)


def findLocation():
    location = record_audio('What is the location?')
    SpeakText('What is the location?')
    if(location == 'my location') or (location == 'current location'):
        g = geol.ip('me')
        url = 'https://google.com/maps/place/' + \
            g.latlng[0]+','+g.latlng[1] + '/&amp;'
        SpeakText('Here is the location of '+location)
        webbrowser.get().open(url)
        print('Here is the location of '+location)
    else:
        url = 'https://google.com/maps/place/'+location + '/&amp;'
        SpeakText('Here is the location of '+location)
        webbrowser.get().open(url)
        print('Here is the location of '+location)


def respond(voice_data):

    voice_commands = {
        'what is your name': 'My name is Jarvis',
        'what is your age': 'I am a computer program',
        'what is your job': 'I am a virtual assitant',
        'what is your favourite colour': 'I like black, just like darkness',
        'what is your favourite food': 'I like pizza',
        'what is your favourite thing to play': 'I like to play with your mom',
        'what time is it': 'It is now '+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute),
        'what day is it': 'Today is '+str(datetime.datetime.now().day)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)
    }
    if voice_data in voice_commands:
        SpeakText(voice_commands[voice_data])
        print(voice_commands[voice_data])
    if 'search now' in voice_data:
        webSearch()
    if 'locate now' in voice_data:
        findLocation()
    if 'exit' in voice_data:
        print('Goodbye')
        exit()


time.sleep(1)
while(1):
    print("Hello, what can I do for you?")
    SpeakText("Hello, what can I do for you?")
    voice_data = record_audio()
    respond(voice_data)

# Stopped at 20:00, continue from there
