#%%
import sqlite3
import pandas as pd

# データを定義します
data = {
    '名前': ['太郎', '花子', '次郎', '三郎', '四郎'],
    '年齢': [25, 30, 35, 40, 45],
    '性別': ['男性', '女性', '男性', '男性', '男性'],
    '都道府県': ['東京', '大阪', '名古屋', '福岡', '札幌']
}

# DataFrameを作成します
df = pd.DataFrame(data)

# SQLite3データベースに接続します
conn = sqlite3.connect('sample.db')

# DataFrameをデータベースに保存します
df.to_sql('persons', conn, index=False, if_exists='replace')

# 接続を閉じます
conn.close()

# %%
