def show_org_edit():
	import streamlit as st
	import pandas as pd
	import os

	index = st.session_state.get("selected_index")
	DATA_DIR = "data"
	CSV_FILE = os.path.join(DATA_DIR,'companies.csv')

	def load_data():
			if os.path.exists(CSV_FILE):
					return pd.read_csv(CSV_FILE)
			else:
					return pd.DataFrame(columns=["企業名", "マイページURL", "ID", "パスワード"])

	# CSVへの保存
	def save_data(df):
			df.to_csv(CSV_FILE, index=False)
			
	index = st.session_state.get("selected_index")

	if index is None:
		st.error("編集対象の企業が見つかりません")
		return

	df = load_data()

	company = df.loc[index]
	
	st.title('企業編集')

	# keyをつけて入力欄を管理
	name = st.text_input('企業名入力欄（必須）', value=company['企業名'])
	mypage_url = st.text_input('マイページURL（任意）', key='mypage_url',value=company['マイページURL'])
	id = st.text_input('ID（任意）', key='id', value=company['ID'])
	password = st.text_input('Password（任意）', key='password', value=company['パスワード'])
	
	col1, col2 = st.columns(2)
	with col1:
		if st.button('更新'):
				if not name:
					st.error('企業名は必須項目です')
				else:
					df.loc[index, '企業名'] = name
					df.loc[index, 'マイページURL'] = mypage_url
					df.loc[index, 'ID'] = id
					df.loc[index, 'パスワード'] = password

					save_data(df)

					st.session_state.success_message = f'「{name}」の企業情報を更新しました！'
					st.session_state['selected_company'] = {
							'企業名': name,
							'マイページURL': mypage_url,
							'ID': id,
							'パスワード': password,
					}
					st.session_state.page = "org_detail"

	with col2:
		if st.button("戻る"):
			st.session_state.page = "org_detail"