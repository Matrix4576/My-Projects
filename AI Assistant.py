import pyttsx3
import datetime
import speech_recognition as sr
import random
import os
import wikipedia
import webbrowser

def speak(audio):
     engine = pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[1].id)
     engine.say(audio)
     engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour <= 0 and hour >= 12:
          print("Good Morning Mintplay")
          speak("Good Morning Mintplay")
     else:
          print("Welcome back Mintplay")
          speak("Welcome back Mintplay")

def recognizer():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 0.9
          audio = r.listen(source)
          try:
               print("Recognizing..")
               query = r.recognize_google(audio, lang="en-in")
          except Exception as e:
               list_b = ["Would you mind repeting that one?", "Sorry I could not hear what you said", "Pardon Please"]
               responce = random.choice(list_b)
               print(responce)
               speak(responce)
               return "None"
          return query

if __name__ == "__main__":
     wishMe()
     recognizer()
     user = False
     while user is False:
          if query == "Hi":
               print("Hello my name is Alexa 2.0 Nice to meet you")
               continue
          elif query == "Open YouTube":
               print("Openning YouTube")
               speak("Openning YouTube")
               webbrowser.open("http://www.youtube.com")
               break
          elif query == "Open Google":
               print("Openning Google")
               speak("Openning Google")
               webbrowser.open("http://www.google.com")
               break
          elif query == "date":
               date = datetime.datetime.today().weekday() + 1
               day_dict = {1: "Monday", 2: "Tuesday", 
                           3: "Wednesday", 4: "Thursday", 5: "Friday", 
                           6: "Saturday", 7: "Sunday"}
               if day in day_dict.keys():
                    day = day_dict[day]
                    print("Today is " + day)
                    speak("Today is " + day)
               continue
          elif query == "time":
               time = str(datetime.datetime.now())
               print("It is " + time)
               hour = time[11:13]
               minute = time[14:16]
               speak(self, "Time is " + hour + ":" + minute)
          elif query == "exit":
               print("Okay quiting")
               speak("Okay quiting")
               break
          elif query == "wikipedia":
               speak("Searching Wikipedia")
               query = query.replace("wikipedia", "")
               result = wikipedia.summary(query, sentences=6)
               print(result)
               speak("According to the wikipedia: ")
               speak(result)
               continue
          