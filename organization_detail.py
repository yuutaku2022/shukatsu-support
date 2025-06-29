import streamlit as st
import pandas as pd
import os
def show_org_detail():
	#csv読み込み
	DATA_DIR = "data"
	CSV_FILE = os.path.join(DATA_DIR, f"{ company['企業名'] }.csv")

	def load_data():
		if os.path.exists(CSV_FILE):
			return pd.read_csv(CSV_FILE)
		else:
			return pd.DataFrame(columns=["name", "date", "S_time", "E_time", "bikou"])

	df = load_data()
	

	#編集画面を表示
	if st.button('企業情報の編集'):
		st.session_state.page = "edit"
	
	company = st.session_state.get("selected_company")
	if not company:
		st.warning("企業データが見つかりません")
		if st.button('企業一覧に戻る'):
			st.session_state.page = "dashboard"
	
	st.title(f"{company['企業名']}")
	st.markdown(f'<a href="{company["マイページURL"]}" target="_blank">マイページへ</a>', unsafe_allow_html=True)
	st.write(f"ID：{company['ID']}")
	st.write(f"パスワード：{company['パスワード']}")

	st.subheader('予定されたイベント')
	if st.button('イベントを追加'):
		st.session_state.page = "event_make"
	

	



	if st.button('戻る'):
		st.session_state.page = "dashboard"



	