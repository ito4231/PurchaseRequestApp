# app.py
#%%
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# SQLite3データベースに接続
db_file_name = 'データベース.db'
conn = sqlite3.connect(db_file_name)

# データベースからデータを取得
query = "SELECT * FROM 商品テーブル"
df = pd.read_sql_query(query, conn) 
query = "SELECT * FROM 所属テーブル"
df2 = pd.read_sql_query(query, conn)


tab1, tab2 = st.tabs(["⏏️ 購入申請", "🗃 申請履歴"])
with tab1:

    # １所属のプルダウンメニュー
    busyo = st.selectbox('1.部署名を選択してください', [""] + list(df2['部署名'].unique()))

    # ２氏名の入力
    name = st.text_input('2.氏名を入力してください')

    # ３種類のプルダウンメニュー
    selected_category = st.selectbox('3.種類を選択してください', [""] + list(df['種類'].unique()))

    # 選択した種類に基づいてデータをフィルタリング
    filtered_df = df[df['種類'] == selected_category]

    # ４商品名のプルダウンメニュー
    selected_product = st.selectbox('4.商品名を選択してください', [""] + list(filtered_df['商品名'].unique()))

    # 選択した商品名に基づいて結果を表示
    if selected_product:
        result_df = filtered_df[filtered_df['商品名'] == selected_product]

        # 必要なカラムのみを取得
        display_columns = ['メーカー', '品番', '出荷単位', '備考']
        result_table = result_df[display_columns]
        
        # メーカー名
        makername = result_df.iloc[0,1]
        # 商品番号
        itemnum = result_df.iloc[0,3]

        # 5.商品詳細の表示
        st.caption("5.商品詳細")
        st.table(result_table)
        
        # 6.商品詳細の表示
        selected_quantity = st.selectbox('6.数量を選択してください', [""] + list(range(1, 11)))
        
        # ★投稿
        st.markdown("""
        <style>
            div.stButton > button {
                width: 100%;
                background-color: blue;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
            
        if selected_category == "" or name == "" or selected_product == "" or selected_quantity == "":
            st.warning("空欄を埋めてください。")
        else:
            # ボタンのために空のスロットを作成
            submit_button_slot = st.empty()
            # 空のスロットにボタンを作成
            submit_button = submit_button_slot.button("購入申請")
            if submit_button:
                # ボタンを成功メッセージに置き換える
                submit_button_slot.success("購入を承りました.")

                # タイムスタンプを取得
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # データベースに情報を追加
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO 履歴テーブル (タイムスタンプ, 部署名, 氏名, 種類, メーカー, 商品名, 商品番号, 数量)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (timestamp, busyo, name, selected_category, makername, selected_product, itemnum, selected_quantity))

                # コミットして変更を保存
                conn.commit()

with tab2:
    query = "SELECT * FROM 履歴テーブル"
    df3 = pd.read_sql_query(query, conn)
    df3['タイムスタンプ'] = pd.to_datetime(df3['タイムスタンプ'])  # タイムスタンプ列を日時型に変換
    df3 = df3.sort_values(by='タイムスタンプ', ascending=False)
    st.dataframe(df3, use_container_width=True)

# 接続を閉じる
conn.close()

# %%
