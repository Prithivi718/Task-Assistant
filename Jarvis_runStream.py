import streamlit as st
from engine.features import playJarvisSound
from engine.commands import handle_commands

# ---------- Main Streamlit App ----------
def main():
    st.set_page_config(page_title="Task Assistant", layout="centered")
    st.title("🤖 Task Voice Assistant")
    st.caption("Click the mic or enter your command to start...")

    st.markdown("###")
    
    # Layout: input box (left) + mic button (right)
    col1, col2 = st.columns([6, 1])  # Wider input, smaller button

    with col1:
        user_input = st.text_input("Type your command...", placeholder="e.g., Open Chrome, Send message to Alex")

    with col2:
        if st.button("🎤", help="Click to speak"):
            playJarvisSound()
            st.toast("🎙 Listening...")
            handle_commands()

    # Optional: Handle text input
    if user_input:
        handle_commands(user_input)

# ✅ VERY IMPORTANT
if __name__ == "__main__":
    main()
