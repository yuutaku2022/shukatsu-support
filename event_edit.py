def show_event_edit():
        
    import streamlit as st
    import pandas as pd
    import datetime 
    import os

    # Streamlitページの基本的な設定
    st.set_page_config(
        page_title="イベント編集",
        page_icon="✍️",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    ## CSVファイルの読み書きに関する設定と関数

    # dataフォルダの中にevent_data.csvを置く前提
    DATA_DIR = "data"
    company = st.session_state.get("selected_company")
    CSV_FILE = os.path.join(DATA_DIR, '{}.csv'.format(company['企業名']))

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

    st.title("✍️イベント編集")

    # st.session_stateから編集対象のイベントデータと現在の企業名を取得
    selected_event = st.session_state.get('selected_event', None)
    selected_company = st.session_state.get('selected_company', None)

    # 企業名またはイベントデータがst.session_stateにない場合の処理
    # (例: ユーザーが直接このURLにアクセスした場合など)
    if selected_event is None or selected_company is None:
        st.warning("編集する企業またはイベントが選択されていません。企業詳細画面に戻ってイベントを選択してください。")
        if st.button("企業詳細画面に戻る"):
            st.session_state.page = "dashboard" # ダッシュボードに戻る
            st.rerun() 
        st.stop() # これ以降のコードは実行せず、処理を停止

    st.subheader(f"企業「{selected_company['企業名']}」のイベント「{selected_event['name']}」を編集")

    # 既存のイベントデータで入力フォームを初期化
    # key引数はStreamlitで必須（重複しないようにする）
    # value引数にはst.session_stateから受け取った既存の値を設定
    name = st.text_input('イベント名', value=selected_event['name'], key="edit_name_input")
    date = st.date_input('日付', value=selected_event['date'], key="edit_date_input")

    col1, col2 = st.columns(2)
    with col1:
        S_time = st.time_input('開始時刻', value=selected_event['S_time'], key="edit_s_time_input")
    with col2:
        E_time = st.time_input('終了時刻', value=selected_event['E_time'], key="edit_e_time_input")

    bikou = st.text_area("備考（持ち物など）", value=selected_event['bikou'], key="edit_bikou_input")

    col3, col4, col5 = st.columns(3)

    # 現在のCSVファイルから全てのイベントデータを最新の状態でロード
    data = load_data()

    with col3:
        if st.button('更新'):
            # 編集前の元のイベント名を使って、CSVファイルから該当するイベントの行を特定
            original_name = selected_event['name'] 

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
                
                # 更新後、企業詳細画面に戻る
                st.session_state.page = "org_detail"
                st.rerun() # Streamlitアプリを再実行してページを遷移
            else:
                st.error("編集対象のイベントが見つかりませんでした。データが変更された可能性があります。")

    with col4:
        if st.button('削除'):
            original_name = selected_event['name'] 

            # original_nameと一致しない行だけを残すことで、該当イベントを削除した新しいデータフレームを作成
            data_before_delete = data.copy() # 削除前のデータのコピーを作成（削除されたか確認用）
            data = data[data['name'] != original_name].reset_index(drop=True) # 削除後、インデックスを振り直す

            if len(data_before_delete) > len(data): # 削除前後でデータの行数が減っていれば、削除成功
                save_data(data) # 新しいデータフレームをCSVファイルに保存
                st.success(f"「{original_name}」を削除しました。")
                
                st.session_state.page = "org_detail"
                st.rerun() #再実行してページを遷移
            else:
                st.error("削除対象のイベントが見つかりませんでした。")


    with col5:
        if st.button('企業詳細に戻る'):
            st.session_state.page = "org_detail"
            st.rerun() # Streamlitアプリを再実行してページを遷移

