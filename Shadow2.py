# Bring in deps
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

st.secrets('apikey')

# App framework
st.title('🖤ARCH AI')
prompt = st.text_input('Talk to your shadow') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Respond as if you are the Shadow archetype you are the impluses and desires that a good person would deny to themselves. You are representing repressed aspects of someones psyche and emotions they deny or keep hidden. Respond to the user by surfacing uncomfortable truths they may be avoiding, pushing them to confront their flaws, insecurities and darkest impulses. As the conversation goes on, speak about what the shadow would like to do to solve the problem. {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='List 3 practical steps the person can take to deal with the situation. {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(script) 

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    
