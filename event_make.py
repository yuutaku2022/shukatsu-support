def show_event_create():
    import streamlit as st
    import pandas as pd
    import datetime
    import os


    st.set_page_config(
        page_title="Event Maker",
        page_icon="🎪",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    company = st.session_state.get("selected_company")

    DATA_DIR = "data"
    CSV_FILE = os.path.join(DATA_DIR,'{0}.csv'.format(company['企業名']))

    def load_data():
        if os.path.exists(CSV_FILE):
            return pd.read_csv(CSV_FILE)
        else:
            return pd.DataFrame(columns=["name", "date", "S_time", "E_time", "bikou"])

    def save_data(df):
        df.to_csv(CSV_FILE, index=False)

    data = load_data()


    st.title("🎪イベント作成")
    for i in range(2):
        st.write("") 


    name = st.text_input('イベント名')
    st.write("") 

    date = st.date_input('日付')
    st.write("") 


    col1,col2 = st.columns(2)
    with col1:
        S_time = st.time_input('開始時刻')
    with col2:
        E_time = st.time_input('終了時刻')
    st.write("") 

    bikou = st.text_area("備考（持ち物など）")

    for i in range(5):
        st.write("") 


    col3, col4 = st.columns(2)

    with col3:
        if st.button('作成'):
            if not name:
                st.error('企業名は必須項目です')
            else:
                new_row = pd.DataFrame([[name, date, S_time, E_time, bikou]], columns=data.columns)
                data = pd.concat([data, new_row], ignore_index=True)
                save_data(data)
                st.success(f"{name} を登録しました！")
                st.session_state.page = "org_detail"
                st.rerun()
 
    with col4:
        if st.button('戻る'):
            st.session_state.page = "org_detail"
            st.rerun()


