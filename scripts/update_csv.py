# scripts/update_csv.py

import pandas as pd
import os

CSV_PATH = "data/metadata.csv"

def append_to_csv(record):
    df_new = pd.DataFrame([record])

    if os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0:
        df_existing = pd.read_csv(CSV_PATH)
        df = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(CSV_PATH, index=False)