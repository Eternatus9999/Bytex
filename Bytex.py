#Importen modulars
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipediaapi
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
import pyautogui
import requests
import instaloader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import pygetwindow as gw
import pygame
import openai
import socket
from PIL import Image, ImageDraw





#Get the current date and time
current_datetime = datetime.now()

#Format the datetime object with AM/PM
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%I:%M %p")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

#TO draw function
def draw_image(type):
    if type == "line":
        draw.line((100, 100, 400, 400), fill="black", width=5)

#Set time Fuction
def set_alarm(seconds):
    time.sleep(seconds)

    #Play a sound
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/ASUS/OneDrive/Desktop/New folder/Naruto-Lofi-Beat.mp3")
    pygame.mixer.music.play()
    speak(f"wake up sir it's {formatted_time}, you have work to do")
    command = takecommand().lower()
    if "stop the alarm" in command:
        pygame.mixer.music.stop

#Send message via WhatsApp
def wtmsg():
    speak("sir, whom do you like to send message")
    C_name = takecommand().lower()
    if "me" in C_name:
        P_No = "+94764887732"
        sendmsg(P_No)
    
    elif "akka" in C_name:
        P_No = "+94763587433"
        sendmsg(P_No)
    
    elif "amma" in C_name:
        P_No = "+94774499435"
        sendmsg(P_No)
    
    elif "thaththa" in C_name:
        P_No = "+94772623552"
        sendmsg(P_No)
    
    elif "namitha" in C_name:
        P_No = "+94703256686"
        sendmsg(P_No)
    
    elif "sadew" in C_name:
        P_No = "+94778569017"
        sendmsg(P_No)
    
    elif "janindu" in C_name:
        P_No = "+94764887732"
        sendmsg(P_No)
    
    elif "sadeepa" in C_name:
        P_No = "+94705905313"
        sendmsg(P_No)
    
    elif "anuda" in C_name:
        P_No = "+94763070772"
        sendmsg(P_No)
    
    elif "famous" in C_name:
        P_No = "+94773189968"
        sendmsg(P_No)
    
    elif "madushanka" in C_name:
        P_No = "+94763909496"
        sendmsg(P_No)
    
    elif "go back" in C_name:
         stop()

    else:
        # speak("Say that again please...") 
        wtmsg()

def stop():
    speak("ok sir going back, is there any other work")

#Send message fuction
def sendmsg(P_No):
    speak("how do you want to send the message sir voice or type")
    method = takecommand().lower()
    if "voice" in method:
        speak("what do you want to send sir")
        S_Message = takecommand().lower()
        hour = datetime.now().hour
        minute = datetime.now().minute + 2
        kit.sendwhatmsg(f"{P_No}",f"{S_Message}", hour, minute)#this is the real time not how many hours
        time.sleep(7)
        speak("please wait sir process in progress")
        pyautogui.click()
        pyautogui.press("enter")
        speak("message has been sent")
    elif "type" in method:
        speak("please type the message you want to send sir")
        S_Message = input("Type here => ")
        hour = datetime.now().hour
        minute = datetime.now().minute + 2
        kit.sendwhatmsg(f"{P_No}",f"{S_Message}", hour, minute)#this is the real time not how many hours
        time.sleep(7)
        speak("please wait sir process in progress")
        pyautogui.click()
        pyautogui.press("enter")
        speak("message has been sent")
    

#Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#TO convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r. listen(source,timeout=10,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e: 
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good AFternoon")

    else:
        speak("Good Evening")

    speak(f"it's {formatted_time}, what do you want me to do sir")

#To send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Kython9999@gmail.com', '#Kython2004')
    server.sendmail('Kython9999@gmail.com', to, content)
    server.close()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=de0388071d5f477cac8916b25712c2ad"

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head =[]
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth",]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is:{head[i]}")

if __name__ == "__main__":
    #takecommand()
    wish()

    #if 1:
    while True:

        query = takecommand().lower()

#Logic building for tasks


# VVVV add application you want to open
        
        if "who are you" in query or "tell me about you" in query:
            speak("I'm bitex. a vertual assistant. i was created by kython in 2024. my purpose is to help you. please ask me to do anything you want . what can i do for you sir")

#TO tell the date
        elif "tell me the day" in query:
            speak(f"{formatted_date}")

#To open applications
        elif "open notepad" in query:
            speak("okay sir, opening notepad")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open calculator" in query:
            speak("okay sir, opening calculator")
            npath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            speak("okay sir, opening command prompt")
            os.system("start cmd")
        
        elif "open camera" in query:
            speak("okay sir, opening camera")
            cap = cv2.VideoCapture(0)
            window_name = 'Camera Feed'
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            while True:
                ret, frame = cap.read()
                if ret:
                    cv2.imshow(window_name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        elif "open obs" in query:
            speak("okay sir opening obs")
            npath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(npath)

        elif "open anki" in query:
            speak("okay sir opening anki")

        elif "open intellij" in query:
            speak("okay sir opening intellij")
            npath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.2\\bin\\idea64.exe"
            os.startfile(npath)

        elif "open vscode" in query:
            speak("okay sir opening vscode")
            npath = "C:\\Users\\Kython\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)

        elif "open unreal engine" in query:
            speak("okay sir opening unreal engine")
            npath = "C:\\Program Files\\Epic Games\\UE_4.27\\Engine\\Binaries\\Win64\\UnrealEditor.exe"
            os.startfile(npath)

        elif "open blender" in query:
            speak("okay sir opening blender")
            npath = "C:\\Program Files\\Blender Foundation\\Blender 3.2.1\\blender.exe"
            os.startfile(npath)

        elif "open whatsapp" in query:
            speak("okay sir opening whatsapp")
            # npath = "C:\Program Files\WindowsApps\WhatsAppDesktop.exe"
            # os.startfile(npath)
            os.startfile("whatsapp://")

        elif "open instagram" in query:
            speak("okay sir opening instagram")
            os.startfile("instagram://")
        
#To play music
        elif "play music" in query or "play song" in query or "play a song" in query or "play a music" in query:
            speak("where do you want to play music sir")
            an = takecommand().lower()
            if "youtube" in an:
                speak("wich song sir")
                an_s = takecommand().lower()
                kit.playonyt(an_s)
            else:
                speak("where is the song sir")
                an = takecommand().lower()
                music_dir = an
                songs = os.listdir(music_dir)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            #Get the hostname of the computer
            hostname = socket.gethostname()

            #Get the IP address of the computer
            ip_address = socket.gethostbyname(hostname)

            speak(f"sir your hostname is {hostname} and your IP address is {ip_address}")
        
        

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()  # Clean up the query
            wiki_wiki = wikipediaapi.Wikipedia('en')  # Initialize Wikipedia API
            page = wiki_wiki.page(query)  # Fetch the page
            if page.exists():
                summary = page.summary[:500]  # Limit the summary to 500 characters
                speak("According to Wikipedia")
                speak(summary)
                # print(summary)  # Uncomment if you want to see the results in the console
            else:
                speak(f"Sorry, I couldn't find any information on {query}.")


        elif "open youtube" in query:
            if "search" in query:
                speak("what do you want to search sir")
                an_s = takecommand().lower()
                kit.playonyt(an_s)
            else:
                speak("okay sir, opening youtube")
                webbrowser.open("youtube.com")

        elif "open instagram" in query:
            speak("okay sir, opening instagram")
            webbrowser.open("instagram.com")

#To open icet lms
        elif "open icet lms" in query:
            speak("okay sir, opening icet lms")
            webbrowser.open("https://icetlms.lk/my/")

        elif "open google" in query:
            speak("okay sir, opening google")
            speak("Sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

#Add phone numbers to send messages
        elif "send a message" in query:
            P_No = wtmsg()

#To send email with/without attachment
        elif "send an email" in query:
            # Set your email credentials
            sender_email = 'kython9999@gmail.com'
            # Use the generated app password instead of the account password
            sender_password = 'uqlk yqvj ywkx rpbe '
              
            # Set the recipient email address
            speak("okay sir please type the resevers email you want to send ")
            recipient_email = input("Type here => ")

            #Select attachment or not
            speak("do you want to send the email with an attachment sir")
            an = takecommand().lower()
            if "no" in an:
                # Create the email message
                speak("sir what is the subject of this email")
                subject = takecommand().lower()
                speak("and sir, what is the message for this email")
                body = takecommand().lower()
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))
              
                # Connect to the SMTP server (in this example, using Gmail's SMTP server)
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(message)
                speak('Email sent successfully!')

            elif "yes" in an:
                # Create the email message
                speak("sir what is the subject of this email")
                subject = takecommand().lower()
                speak("and sir, what is the message for this email")
                body = takecommand().lower()
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))

                speak("sir please type the file location wich you want to attach")
                file_path = input("Type here => ")
                attachment = open(file_path, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file_path}')
                
                message.attach(part)
                attachment.close()
                
                # Connect to the SMTP server (in this example, using Gmail's SMTP server)
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(message)
                speak('sir email with attachment sent successfully!')         

        elif "you can sleep now" in query or "sleep now" in query or "can sleep" in query:
            speak("thank you for using me sir, have a nice day")
            sys.exit()

#To tell password
        elif "tell me my passwords" in query or "tell me my password" in query:
            speak("okay sir please tell me the emergency protocol code")
            code = input("Enter the emergency protocol code here => ")
            if "" in code:
                speak("please wait sir emergency protocol activating")
                time.sleep(10)
                speak("sir your password are generating")
                                
#To close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close calculator" in query:
            speak("okay sir, closing calculator")
            os.system("taskkill /f /im calculator.exe")

        elif "close camera" in query:
            speak("okay sir, closing camera")
            cv2.destroyAllWindows()
        
        elif "close whatsapp" in query:
            speak("okay sir, closing whatsapp")
            #webbrowser.("web.whatsapp.com")
        
#To set alarm
        elif "set alarm" in query:
            speak("sir how do you want to set the alarm")
            command = takecommand().lower()
            if "hours" in command or "hour" in command:
                speak("sir can you please type the number")
                I_Time = int(input("Type here => "))
                alarm_time = I_Time/360
                set_alarm(alarm_time)

            elif "minutes" in command or "minute" in command:
                speak("sir can you please type the number")
                I_Time = int(input("Type here => "))
                alarm_time = I_Time/60
                set_alarm(alarm_time)

#To find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
#To shutdown
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
#To restart
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

#To sleep
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

#To switch windows
        elif "switch the window" in query:
            speak("is there a specific window you want to switch sir")
            answer = takecommand().lower()
            if "no" in answer:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif "yes" in answer:
                speak("wich window you want to switch sir")
                W_Window = takecommand().lower()
                window_title = W_Window
                target_window = gw.getWindowsWithTitle(window_title)
                if target_window:
                    # The window is found; bring it to the foreground
                    target_window[0].activate()
                else:
                    speak(f"No window found with the title: {window_title}")

#To change the position of the selected window
        elif "change the position" in query:
            speak("where do you want to move the window sir")
            command = takecommand().lower()
            if "left" in command:
                pyautogui.keyDown("win")
                pyautogui.press("left")
                pyautogui.keyUp("win")
                
            elif "right" in command:
                pyautogui.keyDown("win")
                pyautogui.press("right")
                pyautogui.keyUp("win")

            elif "up" in command:
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")

            elif "down" in command:
                pyautogui.keyDown("win")
                pyautogui.press("down")
                pyautogui.keyUp("win")

            elif "minimize" in command or "minimise" in command:
                pyautogui.keyDown("win")
                pyautogui.press("down")
                pyautogui.press("down")
                pyautogui.keyUp("win")

            elif "maximize" in command or "maximise" in command:
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")

            elif "don't" in command:
                break
            else:
                speak("")

#To listen the news                  
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

#To check a instagram profile
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please tell me the user name correctly.")
            name = input("Enter name here => ")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                break

#To take screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("sir, please tell me the location to save the screenshot")
            location = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for my next command")

#To hide files & folder
        elif "hide all files" in query or "hide this folder" in query:
            speak("do you want to hide this folder sir")
            confirm = takecommand().lower()
            if "yes hide it" in confirm:
                speak("sir, please wait a moment for process")
                os.system("attrib +h /s /d")
                speak("sir all the files inthis folder is hidden.")
            elif "leave it" in confirm:
                speak("ok sir")
                pass

#To visible file & folder
        elif "visible all files" in query or "visible this folder" in query:
            speak("do you want to visible this folder sir")
            confirm =takecommand().lower()
            if "yes visible it" in confirm:
                speak("sir, please wait a moment for process")
                os.system("attrib -h /s /d")
                speak("sir all the files inthis folder is visible.")
            elif "leave it" in confirm:
                speak("ok sir")
                pass
        
        elif "draw image" in query:
            speak("sir please type the width and height")
            width = int(input("Input the width"))
            height = int(input("Input the height"))
            image = Image.new("RGB", (width,height), "white")
            draw = ImageDraw.Draw(image)
            speak("sir what kind of image do you want me to draw sir")
            command = takecommand().lower()
            draw_image(command)

        #speak("sir do you have any other work")
            
