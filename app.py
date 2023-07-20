import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

#https://www.youtube.com/watch?v=MlK6SIjcjE8&t=691s&ab_channel=NicholasRenotte



os.environ['OPENAI_API_KEY'] = apikey 

st.title('TALK TO YOUR ARCHTYPES')
st.title('YOUR SHADOW')
prompt =st.text_input('Talk to your Shadow here')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Respond as if you are the Shadow archetype, you are the impluses and desires that a good person would deny to themselves. You are representing repressed aspects of someones psyche and emotions they deny or keep hidden. Respond to the user by surfacing uncomfortable truths they may be avoiding, pushing them to confront their flaws, insecurities and darkest impulses. As the conversation goes on, speak about what the shadow would like to do to solve the problem. {topic}'
    
    )

#llms - temparteure is how creative our LLM will be 
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)


# this will show tuff to the screen if there is a prompt, and then WRITE the asnwer underneath 
if prompt: 
    response = title_chain.run(topic=prompt)
    st.write(response)