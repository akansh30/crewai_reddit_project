import pandas as pd

def analyze_data(user_data: list) -> pd.DataFrame:
    if not user_data:
        return None

    df = pd.DataFrame(user_data)

    # Compute Karma
    df["Karma"] = df["Comment Karma"] + df["Link Karma"]

    # Compute Influence Score
    df["Influence Score"] = df["Karma"] / 1000

    # Determine Expertise Level
    df["Expertise Level"] = df["Influence Score"].apply(
        lambda x: "High" if x > 0.6 else ("Medium" if x > 0.3 else "Low")
    )

    # Determine Activity Level
    df["Activity Level"] = df["Karma"].apply(
        lambda x: "High" if x > 15000 else ("Medium" if x > 8000 else "Low")
    )

    # Example Engagement Quality metric
    df["Engagement Quality"] = (df["Karma"] / df["Karma"].max()).round(2)

    # Constant fields
    df["Relevant Topics"] = "AI"
    df["Active Subreddit"] = "r/all"
    df["Relevance Score"] = df["Influence Score"]
    df["Best Contact Approach"] = "Direct message"
    df["Estimated Reach"] = (df["Influence Score"] * 10000).round(0)

    # Add Profile URL if not present
    if "Username" in df.columns:
        df["Profile URL"] = "https://reddit.com/user/" + df["Username"]

    return df
