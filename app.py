# app.py
#%%
import streamlit as st
import sqlite3
import pandas as pd

# SQLite3データベースに接続
db_file_name = '単価データベース.db'
conn = sqlite3.connect(db_file_name)

# データベースからデータを取得
query = "SELECT * FROM 単価テーブル"
df = pd.read_sql_query(query, conn)

# 種類のプルダウンメニュー
selected_category = st.selectbox('種類を選択してください', df['種類'].unique())

# 選択した種類に基づいてデータをフィルタリング
filtered_df = df[df['種類'] == selected_category]

# 商品名のプルダウンメニュー
selected_product = st.selectbox('商品名を選択してください', filtered_df['商品名'].unique())

# 選択した商品名に基づいて結果を表示
result_df = filtered_df[filtered_df['商品名'] == selected_product]

# 必要なカラムのみを取得
display_columns = ['メーカー', '品番', '単価', '出荷単位', '備考']
result_table = result_df[display_columns]

# 結果を表示
st.table(result_table)
# 写真パス
image_path = result_df["写真"]

# 画像表示
st.image(image_path, caption='選択された商品の写真', use_column_width=True)

# 接続を閉じる
conn.close()
