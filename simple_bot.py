# import libraries
import streamlit as st
import random
import time

# response emulator
def response_generator():
    response = random.choice(
        [
            "Hi! How can I help you?",
            "Greetings, human! I am at your service.",
            "Do you require assistance?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# title
st.title("Simple Bot")

# start history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display history on re-launch
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
if prompt := st.chat_input("What's up?"):

    # user message display
    with st.chat_message("user"):
        st.markdown(prompt)

    # update chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display assistant response
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    
    # add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": prompt})