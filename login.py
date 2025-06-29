def login():
    import streamlit as st
    import pandas as pd
    import os

    DATA_DIR = "data"
    LOGIN_FILE = os.path.join(DATA_DIR, "login.txt")
    
    if not os.path.exists(LOGIN_FILE):
        st.write("初回ログインです")
        Password = st.text_input('パスワードを入力してください', type="password")
        
        if st.button("ログイン"):
            with open(LOGIN_FILE, "w") as f:
                f.write(Password)
            st.rerun()


    else:
        st.write("ログイン画面")
        Password = st.text_input('パスワードを入力してください', type="password")
        with open(LOGIN_FILE, "r") as f:
            save_pass = f.read()

            if st.button("ログイン"):
                if Password == save_pass:
                    st.session_state.page = "dashboard"
                else:
                    st.error("パスワードが間違っとるけぇ、確認しんさい。")




    