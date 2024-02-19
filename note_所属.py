#%%
import pandas as pd
import sqlite3

# データフレームの作成
部署データ = [
    "経営戦略部",
    "病棟医事課",
    "クリニック医事課",
    "病棟看護部",
    "クリニック看護部",
    "病棟リハビリ",
    "クリニックリハビリ",
    "j-studio",
    "医療安全管理部",
    "介護部j-HEARTY",
    "介護部短リハ",
    "介護部訪リハ",
    "介護部居宅",
    "介護部j-step",
    "栄養課",
    "洗濯室",
    "放射線・検査科",
    "薬剤室"
]

df = pd.DataFrame({"部署名": 部署データ})
df
#%%
# SQLiteデータベースに接続
conn = sqlite3.connect("データベース.db")

# データフレームをSQLiteテーブルに書き込む
df.to_sql("所属テーブル", conn, if_exists="replace", index=False)

# 接続を閉じる
conn.close()

# %%
