# install librarites
import streamlit as st
from openai import OpenAI

# title
st.title("OpenAI Bot")

# set OpenAI key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# default model

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# start chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
if prompt := st.chat_input("What's up?"):

    # add message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})