#%%
import pandas as pd

# Excelファイルの読み込み
excel_file_path = 'グループ推奨品リスト.xlsx'
excel_file = pd.ExcelFile(excel_file_path)

# タブごとにデータフレームを作成し、リストに追加
dfs = []
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    
    # タブ名を新しい列として追加
    df.insert(0, '種類', sheet_name)
    
    # "写真" カラムを作成し、すべてのレコードに "test.png" を埋め込む
    df['写真'] = 'test.png'
    
    # リストにデータフレームを追加
    dfs.append(df)

# リスト内のデータフレームを結合
final_df = pd.concat(dfs, ignore_index=True)

# 結合したデータフレームを表示
final_df
# %%
import sqlite3
# SQLite3データベースに接続
db_file_name = '単価データベース.db'
conn = sqlite3.connect(db_file_name)

# データフレームをSQLite3データベースに保存
final_df.to_sql('単価テーブル', conn, index=False, if_exists='replace')

# 接続を閉じる
conn.close()
# %%
