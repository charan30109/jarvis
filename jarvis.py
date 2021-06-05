import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()

speaker =  pyttsx3.init()
""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 130)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female





def speak(text):
    speaker.say('yes boss '+text)
    speaker.runAndWait()
def speak_2(text):
    speaker.say(text)
    speaker.runAndWait()


va_name = 'jarvis'

speak_2("i am your " + va_name +  " tell me boss")

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
               # print(command)
               # speak(command)

    except:
        print("check your microphone")
    return command

while True:
    user_comand = take_command()
    if 'quit'  in user_comand or 'close' in user_comand:
        print("see you again boss. i will be there when ever you call me.")
        speak("see you again boss. i will be there when ever you call me.")
        break
    elif 'time' in user_comand:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif 'play ' in user_comand:
        user_comand = user_comand.replace('play ', '')
        print("playing" + user_comand)
        speak("playing " +  user_comand + ' enjoy boss')
        pk.playonyt(user_comand)
        break
    elif 'search for' in user_comand or 'google' in user_comand or 'search' in user_comand:
        user_comand = user_comand.replace('search for', '')
        user_comand = user_comand.replace('search', '')
        user_comand = user_comand.replace('google ', '')
        speak("searching for " + user_comand)
        pk.search((user_comand))
    elif 'who is' in user_comand:
        user_comand = user_comand.replace('who is ', '')
        info = wiki.summary(user_comand, 2)
        print(info)
        speak(info)
    elif 'what are you doing' in user_comand:
        user_comand = user_comand .replace('what are you doing ','')
        speak_2("nothing boss just doing my works")
    elif 'who are you' in user_comand:
        speak_2("boss i am your virtual voice assistant names as jarvis versoin 1 ")
    elif 'what is your name' in user_comand:
        speak_2("my name is jarvis boss")
    elif 'who made you' in user_comand:
        speak_2("kuracha charan sai sagar build me son of k kalyan sagar")
    elif 'open youtube' in user_comand:
        user_comand = user_comand.replace('open', '')
        speak("onpening" + user_comand)
        pk.playonyt("SAGAR BHAI GAMING Yt")
        speak_2("boss this is my brothers youtube channel please subscribe him")
    elif 'send message' in user_comand or "whatsapp" in user_comand:
        user_comand = user_comand.replace('send message', '')
        user_comand = user_comand.replace('whatsapp', '')
        speak("to whom boss")
        phone = 0
        phone = input("pls enter mobile no.")
        speak("please write the message")
        message = str(input("write message here"))
        pk.sendwhatmsg_instantly(f"+91{phone}" , message)
        speak_2("ok boss bye boss i have small work boss")
        break
    elif "shutdown" in user_comand:
        speak("shutting down boss")
        pk.shutdown(time = 100)
    elif "cancel" in user_comand:
        speak("cancelling shutdown function boss")
        pk.cancelShutdown();
    elif "discord" in user_comand:
        speak("boss these is python bulders discord boss let us also jion boss")
        pk.join_discord()
    elif "give me" in user_comand:
        speak("giving you suit mark 95 is ready to launch")

    else:
        speak_2("please say it again boss")


