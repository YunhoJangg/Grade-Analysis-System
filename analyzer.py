import numpy as np
import pandas as pd

def calculate_student_performance(df):
    df["Total"] = df[["Midterm", "Final", "Homework"]].sum(axis=1)
    df["Average"] = df["Total"] / 3
    return df

def get_class_statistics(df):
    scores = df["Average"].values
    
    stats = {
        "Mean": np.mean(scores),
        "Max": np.max(scores),
        "Min": np.min(scores),
        "Median": np.median(scores),
        "Top25": np.percentile(scores, 75)
    }
    
    return stats

if __name__ == "__main__":
    from data_manager import load_data
    test_df = load_data("scores.csv")
    if test_df is not None:
        test_df = calculate_student_performance(test_df)
        print("==== 개별 학생 성적 ====")
        print(test_df)
        
        print("\n==== 학급 전체 통계 ====")
        statistics = get_class_statistics(test_df)
        for key, value in statistics.items():
            print(f"{key}: {value:.2f}")