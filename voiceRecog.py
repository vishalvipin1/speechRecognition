import speech_recognition as sr
import pyttsx3
import webbrowser as web

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# with sr.Microphone() as source1:
#     print("Silence please, calibrating microphone...")
#     r.adjust_for_ambient_noise(source1, duration=2)

#     print("Calibrated, listening...")
#     SpeakText("Calibrated, listening...")

#     audio = r.listen(source1)

#     MyText = r.recognize_google(audio)
#     MyText = MyText.lower()
#     print("Did you say "+MyText)
#     SpeakText("Did you say "+MyText)


if __name__ == "__main__":
    path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    r = sr.Recognizer()
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        print("Say Something...")
        SpeakText("Say Something...")

        audio = r.listen(source2)
        print("Recognizing Now...")

        try:
            dest = r.recognize_google(audio)
            print("You said: "+dest)
            web.get(path).open_new_tab(dest)
        except Exception as e:
            print("Error: "+str(e))
            print("Please try again")
