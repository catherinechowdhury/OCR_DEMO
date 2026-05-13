import pandas as pd

# TRAIN
train_df = pd.read_csv("images\\label\\train_label.csv")

with open("train_labels.txt", "w", encoding="utf-8") as f:
    for _, row in train_df.iterrows():
        filename = row["FILENAME"]
        label = row["IDENTITY"]

        f.write(f"{filename}\t{label}\n")

# TEST
test_df = pd.read_csv("images\\label\\test_label.csv")

with open("test_labels.txt", "w", encoding="utf-8") as f:
    for _, row in test_df.iterrows():
        filename = row["FILENAME"]
        label = row["IDENTITY"]

        f.write(f"{filename}\t{label}\n")

print("Conversion complete!")