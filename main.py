import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_chat_response


def clear_all():
    st.session_state.clear()


def set_temperature(tp):
    if tp == "更精准":
        return 0.0
    elif tp == "通用对话":
        return 1.3
    elif tp == "更多样":
        return 1.5


st.title("✨Clone-Deepseek")
with st.sidebar:
    open_api_key = st.text_input("请输入API密钥", type='password')
    st.markdown("[获取deepseek-API密钥](https://platform.deepseek.com/)")
    st.markdown("---")
    model_kind = st.selectbox("V3 | R1(深度思考)",
                              ["deepseek-chat", "deepseek-reasoner"],
                              index=0,
                              help="deepseek-chat是普通版本；deepseek-reasoner为推理R1")

    tp = st.radio(label="设置对话多样性：",
                  options=("更精准", "通用对话", "更多样"),
                  index=1,
                  format_func=str,
                  help='更精准会更加严谨，比如在做计算题；更多样对话更具有创意')
    temperature = set_temperature(tp)
    st.write("---")
    st.button("清空上下文开启新对话", on_click=clear_all)

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "我是deepseek，有疑问尽管找我😁"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("")

if prompt:
    if not open_api_key:
        st.info("🔑请输入密钥！！")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考，请稍后....."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     model_kind,
                                     open_api_key, temperature)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("human").write(response)
