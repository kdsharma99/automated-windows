import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui as pg
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
'''
set reminder
delete reminder
 mode
disk d
disk c
downloads
scroll
click
read screen
'''


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your virtual assistant.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def maail():
    qu=takeCommand()
    pg.write("a"+qu)
    pg.press("Enter",interval=0.25)


def open(b):
    speak(f"opening {b}") 
    pg.press("win")
    pg.write(b)
    pg.press("enter", interval=0.25)


def con():
    conn=takeCommand()
    pg.write("a"+conn)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "open" in query:
            query = query.replace("open", "")
            open(query)
        
        elif "setreminder" in query:
            pass
        
        elif "delete reminder" in query:
            pass
        
        elif "switch" in query:
            pg.hotkey("alt", "tab")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "copy" in query:
            pg.hotkey("ctrl", "c")
        
        elif "select" in query:
            pg.hotkey("ctrl", "a")
        
        elif "cut" in query:
            pg.hotkey("ctrl", "x")
        
        elif "paste" in query:
            pg.hotkey("ctrl", "v")
        
        elif "close" in query:
            pg.hotkey("alt", "f4") 
        
        elif "minimize" in query:
            pg.hotkey("win","down")
            pg.hotkey("win","down")
        
        elif "maximize" in query:
            pg.hotkey("win","up")
            pg.hotkey("win","up")
        
        elif "volume low" in query:
            pg.press("volumedown")
        
        elif "raise volume" in query:
            pg.press("volumeup")
        
        elif "battery saver" in query:
            pg.click(x=1181, y=756)
            time.sleep(0.5)
            pg.press("tab")
            pg.press("left")
            pg.press("left")
       
        elif "turn off battery saver" in query:
            pg.click(x=1181, y=756)
            time.sleep(0.5)
            pg.press("tab")
            pg.press("right")
            pg.press("right")
        
        elif "dim" in query:
            pg.hotkey('fn', "f9")
        
        elif "screenshot" in query:
            a=0
            pg.screenshot("screenshot"+str(a))
            a+=1
        
        elif "bright" in query:
            pg.hotkey("fn", "f10")
        
        elif "mute" in query:
            pg.press("volumemute")
        
        elif "unmute" in query:
            pg.press("volumemute")
        
        elif "send mail" in query:
            # query=query.replace("search","")
            open("chrome")
            pg.hotkey("ctrl", "t")
            pg.write("amail.google",interval =0.30)
            pg.press("tab")
            pg.press("enter", interval=0.25)
            # time.sleep(8)
            # pg.click(x=47, y=198)
            # speak("Whom you want to mail sir ?")
            # maail()
            # mm=True
            # # deff="Subject"
            # while mm:
            #     speak("Do you want to add more recivers sir ?")
            #     deeff=takeCommand()
            #     if "yes" in deeff:
            #         maail()
            #     else:
            #         mm=False    
            #         pg.press("tab")
            #         speak("Subject sir")
            #         sub=takeCommand()
            #         pg.write("a"+sub)
            #         pg.press("enter", interval=0.25)
            # speak("Any attachments sir?")
            # abc=takeCommand()
            # if "yes" in abc:
            #     pg.click(x=950, y=704)
            # speak("Please tell content sir")
            # pg.press("tab")
            # con()
            # coo=True
            # while coo:
            #     speak("Would you like to add more content sir?")
            #     check=takeCommand()
            #     if "yes" in check:
            #         con()
            #     else:
            #         coo=False
            # speak("May i send the mail sir?")
            # abg=takeCommand()
            # if "yes" in abg:
            #     pg.hotkey("ctrl"+"enter")
        
        
        elif "newfolder" in query:
            pg.hotkey("ctrl", "shift", "n")
        
        elif "incongintomode" in query:
            pg.hotkey("ctrl", "shift", "n")
        
        elif "history" in query:
            pg.hotkey("ctrl", "h")
        
        elif "download  " in query:
            pg.hotkey("ctrl", "j")
        
        elif "save" in query:
            pg.hotkey("ctrl", "s")
        
        elif "type" in query:
            query = query.replace("type", "")
            pg.write(query)
        
        elif "shutdown" in query:
            pg.keyDown("win")
            pg.keyDown("x")
            pg.keyUp("win")
            pg.keyUp("x")
            pg.press("up")
            pg.press("up")
            pg.press("right")
            pg.press("u")

        elif "restart" in query:
            pg.hotkey("ctrl","alt","del")
        
        elif "sleep" in query:
            pg.keyDown("win")
            pg.keyDown("x")
            pg.keyUp("win")
            pg.keyUp("x")
            pg.press("up")
            pg.press("up")
            pg.press("right")
            pg.press("s")
        
        elif "runcode" in query:
            pg.hotkey("ctrl", "alt", "z")
        
        elif "enter" in query:
            pg.press("enter")
        
        elif "airplanemode" in query:
            pg.click(x=1207, y=756)
            time.sleep(0.5)
            pg.click(x=1122, y=716)
            time.sleep(0.2)
            pg.click(x=1089, y=754)
        
        elif "downloads" in query:
            os.startfile("D:\\Downloads")
        
        elif "rename" in query:
            query.replace("rename", "")
            pg.press("f2")
            pg.write(query)
        
        elif "windows" in query:
            pg.hotkey("win", "tab")
           
        elif "caps" in query:
            pg.press("capslock")
        
        elif "tab" in query:
            pg.press("tab")
        
        elif "backspace" in query:
            pg.press("backspace")
        
        elif "delete" in query:
            pg.press("del")
        
        elif "pause" in query:
            pg.press("space")
        
        elif "play" in query:
            pg.press("space")
        
        elif "forward" in query:
            pg.press("right")
        
        elif "backward" in query:
            pg.press("left")
        
        elif "click" in query:
            pg.click()
        
        elif "left click" in query:
            pg.click(button="left")

        elif "right click" in query:
            pg.click(button="right")
        
        elif "scroll up" in query:
            pg.scroll(700)
        
        elif "scroll down" in query:
            pg.scroll(-700)
        
        elif "print" in query:
            pg.hotkey("ctrl", "p")
        
        elif "customselect" in query:
            pg.hotkey("ctrl", "f2")
        
        elif "hold" in query:
            query = query.replace("hold", "")
            pg.down(query)
        
        elif "release" in query:
            query = query.replace("hold", "")
            pg.up(query)
        
        elif "addcursor" in query:
            pg.hotkey("shift", "alt", "i")
        
        elif "where are you" in query:
            pass
        
        elif "back" in query:
            pg.press("backspace")
        
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'kaha h tu' in query:
            speak(f"Sir, i am in shastri nagar")
        
        elif 'DO you know hindi' in query:
            speak(f"Sir,mein hindi seekh raha hu")

        elif "Desktop" in query:
            pg.hotkey("win","d")

        elif "readscreen" in query:
            pass
        
        elif 'Sleep Kushal' in query:
            exit()
