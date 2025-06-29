import streamlit as st
import pandas as pd
import datetime 
import os

st.set_page_config(
    page_title="イベント編集",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="expanded",
)

## CSVファイルの読み書きに関する設定と関数
# イベントデータが保存されるCSVファイルのパスを定義
DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, 'event_data.csv')

# CSVファイルを読み込む関数
def load_data():
    # dataフォルダがなければ作成 
    os.makedirs(DATA_DIR, exist_ok=True) 
    
    if os.path.exists(CSV_FILE):
        # CSVファイルが存在すれば読み込む
        df = pd.read_csv(CSV_FILE)
        return df 
    else:
        # 存在しなければ空のデータフレームを返す
        return pd.DataFrame(columns=["name", "date", "S_time", "E_time", "bikou"])

# データフレームをCSVファイルに保存する関数
def save_data(df):
    df.to_csv(CSV_FILE, index=False)


## イベント編集画面の主要ロジックとUI

# イベント編集画面の表示を担当する関数
def show_event_edit():
    st.title("✍️イベント編集")

    # st.session_stateから編集対象のイベントデータと現在の企業名を取得
    selected_event_data = st.session_state['selected_event_for_edit']
    selected_company_name = st.session_state['selected_company_name']

    st.subheader(f"企業「{selected_company_name}」のイベント「{selected_event_data['name']}」を編集")

    # 既存のイベントデータで入力フォームを初期化
    name = st.text_input('イベント名', value=selected_event_data['name'], key="edit_name_input")
    date = st.date_input('日付', value=selected_event_data['date'], key="edit_date_input")

    col1, col2 = st.columns(2)
    with col1:
        S_time = st.time_input('開始時刻', value=selected_event_data['S_time'], key="edit_s_time_input")
    with col2:
        E_time = st.time_input('終了時刻', value=selected_event_data['E_time'], key="edit_e_time_input")

    bikou = st.text_area("備考（持ち物など）", value=selected_event_data['bikou'], key="edit_bikou_input")

    col3, col4, col5 = st.columns(3)

    # 現在のCSVファイルから全てのイベントデータを最新の状態でロード
    data = load_data()

    with col3:
        if st.button('更新'):
            # 編集前の元のイベント名を使って、CSVファイルから該当するイベントの行を特定
            original_name = selected_event_data['name'] 

            # CSVデータの中から、original_nameと一致する行のインデックスを探す
            match_index = data[data['name'] == original_name].index

            if not match_index.empty: # 該当するイベントが見つかった場合のみ更新
                data.loc[match_index[0], 'name'] = name
                data.loc[match_index[0], 'date'] = date
                data.loc[match_index[0], 'S_time'] = S_time
                data.loc[match_index[0], 'E_time'] = E_time
                data.loc[match_index[0], 'bikou'] = bikou
                
                save_data(data) # 更新されたデータフレームをCSVファイルに保存
                st.success(f"「{name}」の情報を更新しました！") 
                
                # 更新後に企業詳細画面に戻るように追加
                st.session_state.page = "company_detail"
                st.rerun() # 画面を再読み込みしてページを遷移
            else: # 該当するイベントが見つからなかった場合
                st.error("編集対象のイベントが見つかりませんでした。")


    with col4:
        if st.button('削除'):
            original_name = selected_event_data['name'] 

            # original_nameと一致しない行だけを残すことで、該当イベントを削除した新しいデータフレームを作成
            data_before_delete = data.copy()
            data = data[data['name'] != original_name].reset_index(drop=True) 

            if len(data_before_delete) > len(data): # 行が減ったか確認
                save_data(data) # 新しいデータフレームをCSVファイルに保存
                st.success(f"「{original_name}」を削除しました。")
                
                # 削除後は企業詳細画面に戻る
                st.session_state.page = "company_detail"
                st.rerun() # 画面を再読み込みしてページを遷移
            else: # 削除対象が見つからなかった場合
                st.error("削除対象のイベントが見つかりませんでした。")


    with col5:
        if st.button('企業詳細に戻る'):
            st.session_state.page = "company_detail" # 企業詳細画面に戻る
            st.rerun() # 画面を再読み込みしてページを遷移

