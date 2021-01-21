import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("processed.cleveland.data", header=None,
                 names=["age", "sex", "chest pain", "rest bp", "cholestrol", "fasting blood sugar",
                                  "rest ECG", "max HR", "exer. ind. angina", "ST depression", "ST slope",
                                  "major vessels", "thal", "prediction"])

# remove any rows that contain a '?'
question_mark_mask = (df != "?").all(1)

df = df[question_mark_mask]

df_labels = df["prediction"]
df_features = df.drop(columns=["prediction"])

print(df_labels.head())
print(df_features.head())

train_features, test_features, train_labels, test_labels = train_test_split(df_features, df_labels, test_size=0.2)

print(len(train_features), len(train_labels), len(test_features), len(test_labels))

train_features.to_csv("data/training_data.csv", index=False)
train_labels.to_csv("data/training_labels.csv", index=False)
test_features.to_csv("data/test_data.csv", index=False)
test_labels.to_csv("data/test_labels.csv", index=False)
