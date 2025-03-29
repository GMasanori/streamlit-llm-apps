from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

st.title("LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: 健康の専門家")
st.write("入力フォームに健康に関する質問を入力し、「実行」ボタンを押すことでアドバイスがもらえます。")
st.write("##### 動作モード2: 歴史の専門家")
st.write("入力フォームに歴史に関する質問を入力し、「実行」ボタンを押すことで情報がもらえます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関する質問", "歴史に関する質問"]
)

st.divider()

if selected_item == "健康に関する質問":
    input_message = st.text_input(label="健康に関する質問をを入力してください。")

else:
    input_message = st.text_input(label="歴史に関する質問をを入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "健康に関する質問":
        if input_message:

            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
                SystemMessage(content="あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"),
                HumanMessage(content=input_message),
            ]

            result = llm(messages)
            st.write(result.content)

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")
            
    elif selected_item == "歴史に関する質問":
        if input_message:
            
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
                SystemMessage(content="あなたは歴史に関する専門家です。情報を提供してください。"),
                HumanMessage(content=input_message),
            ]

            result = llm(messages)
            st.write(result.content)
            
    else:
        st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")