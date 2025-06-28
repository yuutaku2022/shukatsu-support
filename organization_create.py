import streamlit as st
import pandas as pd
import os

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "companies.csv")
COLUMNS = ["企業名", "マイページURL", "ID", "パスワード"]

# dataフォルダがなければ作成
os.makedirs(DATA_DIR, exist_ok=True)

def safe_read_csv(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            return pd.read_csv(file_path)
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=COLUMNS)
    else:
        return pd.DataFrame(columns=COLUMNS)

st.title('新規企業作成')

# keyをつけて入力欄を管理
name = st.text_input('企業名入力欄（必須）')
mypage_url = st.text_input('マイページURL（任意）', key='mypage_url')
id = st.text_input('ID（任意）', key='id')
password = st.text_input('Password（任意）', key='password')

if st.button('作成'):
    if not name:
        st.error('企業名は必須項目です')
    else:
        new_entry = {
            '企業名': name,
            'マイページURL': mypage_url,
            'ID': id,
            'パスワード': password,
        }

        df = safe_read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')
        
        st.success('企業情報を保存しました！')
