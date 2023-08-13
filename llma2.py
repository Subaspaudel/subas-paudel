#import replicate
import os
import streamlit as st
st.header(' SIMPLE CHATBOT')
os.environ["REPLICATE_API_TOKEN"]='r8_6tFxLQjMutOzaA69q8Wxqmbzd8ZMUVQ1XDQh2'
pre_prompt="Helpful Assistant"
prompt_input=st.text_input('User:')
#output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                       # input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                       # "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters
fs=' Nepal is a beautiful Country '

st.text_area("Bot :",value=fs)
