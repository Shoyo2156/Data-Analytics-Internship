
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*.csv")

print("Total CSV files:", len(files))

for file in files:
    df = pd.read_csv(file)

    print("\n" + "=" * 60)
    print("FILE:", os.path.basename(file))
    print("SHAPE:", df.shape)

    print("\nCOLUMNS:")
    print(df.columns.tolist())

    print("\nDATA TYPES:")
    print(df.dtypes)

    print("\nMISSING VALUES:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    print("\nDUPLICATE ROWS:", df.duplicated().sum())
