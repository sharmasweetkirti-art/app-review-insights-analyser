import pandas as pd

# Load dataset
df = pd.read_csv("reviews.csv")

print("===== BASIC DATA OVERVIEW =====")
print(f"Total Reviews: {len(df)}")
print("\nAverage Rating:", round(df["rating"].mean(), 2))

print("\nRating Distribution:")
print(df["rating"].value_counts().sort_index())

print("\nReviews by Platform:")
print(df["platform"].value_counts())

print("\nReviews by Region:")
print(df["region"].value_counts())

# -----------------------------
# Simple Theme Detection
# -----------------------------

accuracy_keywords = ["misunderstands", "accent", "noise", "inaccurate", "laggy"]
robotic_keywords = ["robotic", "unnatural", "human-like"]
delight_keywords = ["helpful", "love", "futuristic", "amazing", "best"]

def detect_theme(text, keywords):
    text = text.lower()
    return any(keyword in text for keyword in keywords)

df["accuracy_issue"] = df["review_text"].apply(lambda x: detect_theme(x, accuracy_keywords))
df["robotic_issue"] = df["review_text"].apply(lambda x: detect_theme(x, robotic_keywords))
df["delight_signal"] = df["review_text"].apply(lambda x: detect_theme(x, delight_keywords))

print("\n===== THEME SUMMARY =====")
print("Accuracy Issues:", df["accuracy_issue"].sum())
print("Robotic Feel Issues:", df["robotic_issue"].sum())
print("Delight Signals:", df["delight_signal"].sum())

# -----------------------------
# Sample Real Quotes
# -----------------------------

print("\n===== SAMPLE USER QUOTES =====")

print("\nAccuracy Related:")
print(df[df["accuracy_issue"]]["review_text"].head(2).to_string(index=False))

print("\nRobotic Related:")
print(df[df["robotic_issue"]]["review_text"].head(2).to_string(index=False))

print("\nDelight Related:")
print(df[df["delight_signal"]]["review_text"].head(2).to_string(index=False))
