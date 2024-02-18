import streamlit as st
import sqlite3
import pandas as pd

# SQLite3データベースに接続
db_file_name = '単価データベース.db'
conn = sqlite3.connect(db_file_name)

# データベースからデータを取得
query = "SELECT 種類, メーカー, 商品名 FROM 単価テーブル"
df = pd.read_sql_query(query, conn)

# 種類のプルダウンメニュー
selected_category = st.sidebar.selectbox('種類を選択してください', df['種類'].unique())

# 選択した種類に基づいてデータをフィルタリング
filtered_df = df[df['種類'] == selected_category]

# 商品名のプルダウンメニュー
selected_product = st.sidebar.selectbox('商品名を選択してください', filtered_df['商品名'].unique())

# 選択した商品名に基づいて結果を表示
result_df = filtered_df[filtered_df['商品名'] == selected_product]
st.write(result_df)

# 接続を閉じる
conn.close()
