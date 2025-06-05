from app.crews.utils.analyze_data import analyze_data
import pandas as pd

def output_data(df):
    if df is None or isinstance(df, str):
        print("No data to output.")
        return "No data to output."

    output_file = "reddit_user_analysis.xlsx"
    df.to_excel(output_file, index=False)
    print(f"File created: {output_file}")
    return f"File created: {output_file}"
    