import streamlit as st
import pandas as pd
import datetime
import os
from organization_create import show_org_create


##CSVについて

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR,'companies.csv')


# CSVの読み込み
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["企業名", "マイページURL", "ID", "パスワード"])

# CSVへの保存
def save_data(df):
    df.to_csv(CSV_FILE, index=False)

    
df = load_data()

##CSVについてここまで


#初期ページ設定
if "page" not in st.session_state:
	st.session_state.page = "dashboard"

#表示画面の切り替え
if st.session_state.page == "org_create":
	show_org_create()
else:
    # トップ画面
    st.title("就活支援アプリへようこそ！")
    
    if "success_message" in st.session_state:
         st.success(st.session_state.success_message)
         del st.session_state.success_message

    if st.button("企業作成画面へ"):
        st.session_state.page = "org_create"

    for i in range(len(df)):
     if st.button(df.iloc[i]['企業名']):
          st.write("企業名:", df.iloc[i]['企業名'],"のページに行きたい")
         



     
 




