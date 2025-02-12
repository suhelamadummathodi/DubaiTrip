import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(DEEPSEEK_API_KEY,BASE_URL)
def chat_bot(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= message
    )

    return(completion.choices[0].message.content)

bot_message = [{"role": "system", "content": "You are a Dubai trip planner. You should give precise and accurate information to user regarding itinerary, food, accomodation, events and tourist attractions based on the days available. Interact with the user to get user details and respond professionally."},
                {"role": "assistant", "content": "Hello 👋. I am Dubai Genie, your ultimate travel guide. How may I help you?"}]

st.title("Dubai Trip Planning Assistant")
if 'messages' not in st.session_state:
    st.session_state.messages = bot_message

for message in st.session_state.messages:
    if(message['role']!='system'):
        with st.chat_message(message['role']):
            st.markdown(message['content'])

user_input = st.chat_input("Enter your message")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    st.session_state.messages.append({"role":"user", "content":user_input})
    
    response = chat_bot(st.session_state.messages)
    if response:
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant", "content":response})
