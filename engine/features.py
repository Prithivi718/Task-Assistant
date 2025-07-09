import struct
import webbrowser
import playsound as ps
import sqlite3
#import pyaudio

import pyautogui as gui
#from pvporcupine import create

import pywhatkit
from engine.commands import *
from engine.helper import *
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.reasoning import ReasoningTools
from engine.config import OPENROUTER_API_KEY
from textwrap import dedent
import urllib.parse

import os



def playJarvisSound():
    music_dir = "www\\assests\\audio\\start_sound.mp3"
    try:
        ps.playsound(music_dir)
    except Exception as e:
        print(f"Error playing sound: {e}")


def open_software(text):
    text = text.replace("jarvis", "")
    text = text.replace("open", "")
    text = text.lower().strip()

    if text != "":
        try:
            # ✅ Create a fresh DB connection in this thread
            conn = sqlite3.connect("jarvis.db")
            cursor = conn.cursor()

            # Search for software path
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (text,))
            results = cursor.fetchall()

            if results:
                st.markdown(f"🧠 Opening: **{text}**")
                os.startfile(results[0][0])

            else:
                # Search in web_command table
                cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (text,))
                results = cursor.fetchall()

                if results:
                    st.markdown(f"🌐 Opening website: **{text}**")
                    webbrowser.open(results[0][0])
                else:
                    # Try system fallback
                    try:
                        os.system('start ' + text)
                        st.markdown(f"⚙️ Trying to open with system command: **{text}**")
                    except:
                        st.warning("❌ Application not found.")

            # Close connection
            conn.close()

        except Exception as e:
            st.error(f"❌ Failed to open software/web: {e}")


def play_song_on_youtube(song_name):
    st.info(f"🎵 Now Playing: **{song_name}**")
    pywhatkit.playonyt(song_name)


def findContact(query):
    import sqlite3
    words_to_remove = ['jarvis', 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']

    def remove_words(text, words):
        return ' '.join([word for word in text.split() if word.lower() not in words])

    query = remove_words(query.lower(), words_to_remove)

    try:
        # Always create a new connection in the current thread
        conn = sqlite3.connect('jarvis.db')
        cursor = conn.cursor()

        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
                       ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        conn.close()

        if results:
            mobile_number_str = str(results[0][0])
            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str
            return mobile_number_str, query
        else:
            return 0, 0

    except Exception as e:
        print("❌ DB Error:", e)
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to " + name
    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to " + name
    else:
        target_tab = 6
        message = ''
        jarvis_message = "starting video call with " + name

    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://web.whatsapp.com/send?phone={mobile_no}&text={encoded_message}"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(whatsapp_url)
    gui.hotkey('ctrl', 'f')
    for i in range(1, target_tab):
        gui.hotkey('tab')
    gui.hotkey('enter')
    st.info(jarvis_message)

def chatBot(user_chat):
    reasoning_agent = Agent(
        name="Reasoning Agent",
        role="Logical problem solver that breaks tasks into clear reasoning steps.",
        model=OpenRouter(id="openai/gpt-4o-mini", api_key=OPENROUTER_API_KEY),
        description="This agent analyzes the problem, thinks step-by-step, and produces structured solutions.",
        instructions=dedent("""\
            Understand the user's request deeply.,
            Think through the task step-by-step using your own reasoning.,
            Focus on clarity, correctness, and structure.,
            Do not consider tone or emotion — focus only on logical clarity.,
            Your output will be passed to a tone-aware agent next.,
        """),
        tools=[ReasoningTools(think=True, analyze=True, add_instructions=True, add_few_shot=True)],
        debug_mode=False,
        show_tool_calls=False
    )

    response_agent = Agent(
        name="Response Agent",
        role="Friendly, emotionally-aware responder that adapts the reasoning output to the user's tone.",
        model=OpenRouter(id="openai/gpt-4o-mini", api_key=OPENROUTER_API_KEY),
        description="This agent reformats the raw reasoning output into a response that matches the user's emotional tone.",
        instructions=dedent("""\
            You will receive a structured reasoning output.
            Rephrase it to match the emotional tone of the user’s original question.
            Use emojis, casual phrasing, or professional tone depending on the user's vibe.
            Do not change the logic or steps — only adapt tone, formatting, and clarity.
            Be friendly and human-like, unless the user is being formal.
        """),
        tools=[],
        show_tool_calls=False
    )

    st.markdown("🧠 Thinking...")
    reasoning_output = reasoning_agent.run(user_chat)
    response = response_agent.run(f"User Query: {user_chat} \n\n Raw Output: {reasoning_output}")
    return response.content

def makeCall(name, mobileno):
    mobileno = mobileno.replace(" ", "")
    st.info("Calling " + name)
    command = "adb shell am start -a android.intent.action.CALL -d tel:" + mobileno
    os.system(command)

def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    st.info("sending message")
    goback(4)
    keyEvent(3)
    tapEvents(90, 1425)
    tapEvents(626, 1408)
    adbInput(mobileNo)
    tapEvents(656, 1444)
    tapEvents(317, 1440)
    adbInput(message)
    tapEvents(647, 878)
    st.info("message send successfully to " + name)
