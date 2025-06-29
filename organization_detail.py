import streamlit as st
import pandas as pd
import os
import datetime

def show_org_detail():

	company = st.session_state.get("selected_company")
	if not company:
		st.warning("企業データが見つかりません")
		if st.button('企業一覧に戻る'):
			st.session_state.page = "dashboard"
	
	#csv読み込み
	DATA_DIR = "data"
	CSV_FILE = os.path.join(DATA_DIR, f"{company['企業名']}.csv")

	def load_data():
		if os.path.exists(CSV_FILE):
			return pd.read_csv(CSV_FILE)
		else:
			return pd.DataFrame(columns=["name", "date", "S_time", "E_time", "bikou"])

	df = load_data()


	#編集画面を表示
	if st.button('企業情報の編集'):
		st.session_state.page = "org_edit"
	
	st.title(f"{company['企業名']}")

	# 成功メッセージの表示
	if "success_message" in st.session_state:
			st.success(st.session_state.success_message)
			del st.session_state.success_message  # ← 1回表示したら削除！

	if company['マイページURL'].strip() != '':

		st.markdown(f"""
		<div style="
				border: 2px solid #4CAF50;
				border-radius: 10px;
				padding: 16px;
				background-color: #f9f9f9;
				margin-bottom: 20px;
		">
			<p>
				<a href="{company['マイページURL']}" target="_blank" style="
					display: inline-block;
					padding: 8px 16px;
					background-color: #4CAF50;
					color: white;
					text-decoration: none;
					border-radius: 5px;
					font-weight: bold;
					">
					マイページへ
				</a>
				</p>
			<p>ID：{company['ID']}</p>
			<p>パスワード：{company['パスワード']}</p>
		</div>
		""", unsafe_allow_html=True)

	today = datetime.date.today()

	st.subheader('予定されたイベント')
	if st.button('イベントを追加'):
		st.session_state.page = "event_make"
	
	for i, row in df.iterrows():
		selected_date = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()

		if selected_date >= today:
			with st.expander(f"{row['date']}：{row['name']}"):

				if st.button(f"編集する", key=f"view_{i}"):
					st.session_state.selected_event = row.to_dict()
					st.session_state.page = "event_edit"
	

	st.subheader('過去のイベント')
	for i, row in df.iterrows():
		selected_date = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()
		if selected_date < today:
			st.text(f"{row['date']}：{row['name']}")



	if st.button('戻る'):
		st.session_state.page = "dashboard"



	