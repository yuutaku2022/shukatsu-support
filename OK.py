def show_OK():
    import streamlit as st

    st.write("パスワード設定完了！")
    st.write("就活支援アプリにようこそ！")
    
    st.balloons()

    if st.button("ダッシュボードへ"):
        st.session_state.page = "dashboard"
        st.rerun()  # ページを更新してダッシュボードを表示