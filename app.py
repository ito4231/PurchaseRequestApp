import streamlit as st
import sqlite3
import pandas as pd

# SQLite3データベースに接続します
conn = sqlite3.connect('sample.db')

# データベースからデータを取得します
query = "SELECT * FROM persons"
df = pd.read_sql(query, conn)

# 接続を閉じます
conn.close()

# Streamlitアプリを作成します
st.title('SQLite3データベースのデータを表示するアプリ')
st.caption("これはテストあぷりです。")
# データを表示します
st.write(df)
