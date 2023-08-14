import streamlit as st 
import pyperclip 

from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(
    page_title="GPT Prompt Help",
)

from functions import (
    improve_prompt,
    answer_prompt,
    combine_answers
)
with st.sidebar:
    st.write("# GPT Prompt Help")
    
    st.write("### A.k.a. Do you Need a Prompt Engineer?")
    
    st.write("This app helps you see potential improvements your GPT3/GPT4 prompts, and see the results of those potental changes.")
    
    st.write("### How to use this app")
    st.write("Enter any prompt into the box. The app will answer that prompt as is (using GPT3.5), then suggest an improved verison of that prompt, and answer that improved prompt.")
    
    st.write("After the prompts have been answered, the app will combine the answers into a single answer, presented again at the top of the page.")
    
    st.markdown("---")
    
    st.write("### Why use this app?")
    st.write("As Large Language Models become more prevalent, prompt engineering has become hot topic. **GPT Prompt Help** aims to provide everyone an easy way to experience the benefit of improved prompts, and to learn how to improve them for themselves.")
    
    
    st.write("### What happens with what I enter?")
    st.write("The app uses popular prompt engineering prompts to iterate on the initial prompt, and then proceeds to answer those improved versions in addition to the initial version.")
    
    st.write("### What are the prompts used?")
    st.write("The app is now available on Github at https://github.com/KevinRPan/gptprompthelp")
    

expander = st.expander("Tips")
expander.write("Try running any question on your mind. The app will try to answer it, and then improve the prompt to see if it can answer it better. For example, _help me understand prompt engineering_.")

if user_input := st.chat_input("Ask anything"):

    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        a1 = answer_prompt(user_input, callbacks=[st_callback], system_instructions="")

    st.markdown("---")

    st.info("**Improved prompt** \n\n The app will now try to improve your prompt.")
    with st.chat_message("user"):
        st_callback = StreamlitCallbackHandler(st.container())
        new_prompt_complex = improve_prompt(user_input, callbacks=[st_callback], simple_instruction=False, use4 = False)

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        a_complex = answer_prompt(new_prompt_complex, callbacks=[st_callback])

    st.markdown("""---""") 
    with st.chat_message("user"):
        st.write("Describe the difference between these two answers and summarize them into a single answer.")

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        combined = combine_answers([a1,a_complex],
                                    user_input, 
                                    callbacks=[st_callback])

    st.markdown("""---""") 
