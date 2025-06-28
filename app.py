import streamlit as st
from organization_create import show_org_create

#初期ページ設定
if "page" not in st.session_state:
	st.session_state.page = "dashboard"

#表示画面の切り替え
if st.session_state.page == "org_create":
	show_org_create()
else:
    # トップ画面
    st.title("就活支援アプリへようこそ！")
    st.write("以下から始めましょう")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("企業作成画面へ"):
            st.session_state.page = "org_create"
    with col2:
        if st.button("イベント作成画面へ"):
            st.session_state.page = "event_create"	

