# This file use langchain to host codellama 7B
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

model = Ollama(
    model="codellama",
    temperature=0.9
)

RESPONSE_TEMPLATE = {
    "status": "success/error",
    "data": "your answer/i don't know"
}

prompt = PromptTemplate.from_template("""
    code for me a Python program that {purpose},
    always format your answer as json like this: {template},
    say nothing but json, even when you not know the answer
""")

chain = LLMChain(
    llm=model,
    prompt=prompt,
    verbose=False
)

user_input = input("What you want the program to code for you? ")

_input = {
    "purpose": user_input,
    "template": RESPONSE_TEMPLATE
}

print(chain.run(_input))
