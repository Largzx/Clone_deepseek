from langchain import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os


def get_chat_response(prompt, memory, model, openai_api_key, temperature):
    model = ChatOpenAI(base_url="https://api.deepseek.com",
                       model=model,
                       openai_api_key=openai_api_key,
                       temperature=temperature)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

