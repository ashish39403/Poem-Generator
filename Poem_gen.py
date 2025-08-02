from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st


load_dotenv()


#LLM DESIGN:-
llm = ChatGroq(
    model = "llama-3.1-8b-instant", 
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature= 0.5,
)



#Streamlit For designing...
st.header("Generate Your Idea's with Poetic AI..🌿 ")

user_input = st.text_input('Enter the Theme of your Poem . . .')


Type=st.selectbox('Choose the Type of the Poem' ,["None", " 1. Narrative Poem" ," 2. Lyric Poem" ," 3. Free Verse", "3. Haiku"])
Tone = st.selectbox('Choose the Type of the Poem', ["None", "1. Romantic Tone", " 2. Melancholic Tone", " 3. Inspirational Tone" ,"4. Playful / Humorous Tone","5. Mysterious Tone"])


if st.button('Generate  '):
    if user_input:
        with st.spinner('Generating'):
            prompt =f"Write a beautiful poem about {user_input}."      
            res = llm.invoke(prompt)     
            st.write(res.content)
    else:
        st.warning('Enter the theme for  your Poem first😊')
        
    
        
        
