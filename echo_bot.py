# import libraries
import streamlit as st

# title
st.title("Echo Bot")

# start chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show history of messages on return
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# respond to user input
if prompt := st.chat_input("what's up?"):
    
    # display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # echo user response
    response = f"Echo: {prompt}"

    # display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # add to chat history
    st.session_state.messages.append({"role": "assisitant", "content": response})
