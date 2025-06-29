def show_dashboard():
    import streamlit as st
    import pandas as pd
    import datetime
    import os

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

    # トップ画面
    st.title("就活支援アプリへようこそ！")

    # 成功メッセージの表示
    if "success_message" in st.session_state:
        st.success(st.session_state.success_message)
        del st.session_state.success_message  # ← 1回表示したら削除

    if "success_message" in st.session_state:
            st.success(st.session_state.success_message)
            del st.session_state.success_message

    if st.button("企業作成画面へ"):
        st.session_state.page = "org_create"

    for i, row in df.iterrows():
        with st.expander(f"{row['企業名']}"):

            if st.button(f"詳細を見る", key=f"view_{i}"):
                st.session_state.selected_company = row.to_dict()
                st.session_state.selected_index = i #インデックスの保存
                st.session_state.page = "org_detail"
         



     
 




