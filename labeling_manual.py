import pandas as pd
import numpy as np
import os


df = pd.read_csv("messages_group_db.csv", sep="\t")


index_non_label = 0

while index_non_label < len(df):
    if str(df.iloc[index_non_label, -2]) == str(np.nan):
        print("------------------------------------")
        print(f"Choose label: 0 - pass, 1 - procede. Group - {df.iloc[index_non_label, 0]} ")
        print(" ")
        while True:
            try:
                label = int(str(input(f"--> {df.iloc[index_non_label, -4]} ")).replace(" ", ""))
            except ValueError:
                label = None
                pass
            if label in (None, 0, 1):
                break
            else:
                print("Please, choose 0 or 1 or press Enter")
                continue

        if label is None:
            label = 0
        df = pd.read_csv("messages_group_db.csv", sep="\t")        
        df.iloc[index_non_label, -2] = label
        df.to_csv("messages_group_db.csv", sep="\t", index=False)
        df = pd.read_csv("messages_group_db.csv", sep="\t")
        print(f"Procede {index_non_label+1}/{len(df)}")
    index_non_label += 1

# rerun training DS model
os.system("python .//DS_Model//ds_model_train.py")

