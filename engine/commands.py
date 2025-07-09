import pyttsx3
import speech_recognition as sr
import streamlit as st
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.9)
recognizer = sr.Recognizer()

def listen_commands():
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, 10, 6)
    
    try:
        text = recognizer.recognize_google(audio, language='en_US')
        st.toast("Waiting for next input...", icon="⏳")
    except Exception as ex:
        return None
    return text.lower()

def introduce_jarvis():
    with st.chat_message('ai'):
        st.markdown("Hello, I am Task Agent, your Artificial Intelligence assistant. I am here to assist you with various tasks. How can I help you today?")

def handle_commands(message=1):
    if message == 1:
        command = listen_commands()
        if not command or command.strip() == "":
            st.toast("Waiting for next input...", icon="⏳")
            return
       
    else:
        command = message.lower()
        if not command or command.strip() == "":
            st.toast("Waiting for next input...", icon="⏳")
            return

    with st.chat_message('user'):
        st.markdown(f"📥 **Command Detected:** `{command}`")
    
    try:
        if 'stop' in command:
            st.info("Turning off the Agent", icon="⏳")
            return

        elif 'open' in command:
            from engine.features import open_software
            open_software(command)
              
        elif 'play' in command:
            from engine.features import play_song_on_youtube
            text = command.replace('play', '').strip()
            play_song_on_youtube(text)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            with st.chat_message('ai'):
                st.markdown(f"The current time is {current_time}")

        elif 'how are you' in command:
            with st.chat_message('ai'):    
                st.markdown("I'm fine, what about you, Sir?")
        
        elif 'hi' in command or 'hello' in command:
            with st.chat_message('ai'):
                st.markdown("Hi. I am Task Agent! How can I help you today.")
            
        elif 'fine' in command or 'good' in command:
            with st.chat_message('ai'):    
                st.markdown("That's wonderful! How can I assist you today?")

        elif 'who is god' in command:
            with st.chat_message('ai'):
                st.markdown("Tony Stark built the legacy of Iron Man. True power comes from within, not just the tech.")

        elif 'what is your name' in command or 'who are you' in command:
            introduce_jarvis()

        elif "send message" in command or "phone call" in command or "video call" in command:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(command)
            if contact_no != 0:
                with st.chat_message('ai'):
                    st.markdown("Which mode you want to use Whatsapp or mobile")
                    preference = listen_commands()
                with st.chat_message('user'):
                    st.markdown(preference)
                
                if 'mobile' in preference:
                    if "send message" in command or "send sms" in command:
                        with st.chat_message('ai'):
                            st.info("What Message to send")
                        message = listen_commands()
                        with st.chat_message('user'):    
                            st.markdown(message)
                        sendMessage(message, contact_no, name)
                    
                    elif "phone call" in command:
                        makeCall(name, contact_no)
                    
                    else:
                        st.info("Please Try Again...")

                elif 'whatsapp' in preference:
                    message=""
                    if "send message" in command:
                        message = 'message'
                        with st.chat_message('ai'):
                            st.info("What Message to Send")
                        command = listen_commands()
                        
                    elif "phone call" in command:
                        message = 'call'
                    else:
                        message = 'video call'
                        
                    whatsApp(contact_no, command, message, name)

        else:
            from engine.features import chatBot
            with st.chat_message('ai'):
                st.markdown("Processing your commands to ChatBot...")
                chat = chatBot(command)
                st.markdown(f"💡 **AI Response:** {chat}")
                                 
    except:
        st.markdown("Sorry, I didn't understand that command.")
        
    st.toast("Waiting for next input...", icon="⏳")
   