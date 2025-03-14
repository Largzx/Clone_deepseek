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


if __name__ == '__main__':
    memory = ConversationBufferMemory(return_messages=True)
    print(get_chat_response("今天是几号", memory, "deepseek-chat", os.environ["OPENAI_API_KEY"]))
    # print(get_chat_response("", memory, "deepseek-chat", os.environ["OPENAI_API_KEY"]))
