#%%
import sqlite3
from datetime import datetime

# データベースへの接続
conn = sqlite3.connect('データベース.db')
cursor = conn.cursor()

# 履歴テーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 履歴テーブル (
        タイムスタンプ TEXT,
        部署名 TEXT,
        氏名 TEXT,
        種類 TEXT,
        メーカー TEXT,
        商品名 TEXT,
        商品番号 TEXT,
        数量 INTEGER
    )
''')

# データベースへの変更のコミットと接続のクローズ
conn.commit()
conn.close()

# %%
