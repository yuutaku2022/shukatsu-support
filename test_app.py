# app.py
import streamlit as st

# 初期状態の設定
if "page" not in st.session_state:
    st.session_state.page = "home"

# メニュー
with st.sidebar:
    st.title("📚 メニュー")
    if st.button("🏠 ホーム"):
        st.session_state.page = "home"
    if st.button("📝 新規登録"):
        st.session_state.page = "register"
    if st.button("🔍 詳細表示"):
        st.session_state.page = "details"

# ページ表示の分岐
if st.session_state.page == "home":
    st.title("🏠 ホーム画面")
    st.write("ここがトップ画面")

elif st.session_state.page == "register":
    st.title("📝 新規登録")
    name = st.text_input("企業名を入力")
    if st.button("登録する"):
        st.success(f"{name} を登録しました！")

elif st.session_state.page == "details":
    st.title("🔍 詳細画面")
    st.write("ここに詳細情報を表示")