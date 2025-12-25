import pandas as pd
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return None

    try:
        df = pd.read_csv(file_path)

        required_columns = ["Name", "Midterm", "Final", "Homework"]
        for col in required_columns:
            if col not in df.columns:
                print(f"오류: 필수 컬럼 '{col}'이 누락되었습니다.")
                return None
            
        if df.empty:
            print("오류: 불러온 데이터가 비어 있습니다.")
            return None
        
        score_cols = ["Midterm", "Final", "Homework"]
        for col in score_cols:
            if not pd.api.types.is_numeric_dtype(df[col]):
                print(f"오류: '{col}' 컬럼에 숫자가 아닌 값이 포함되어 있습니다.")
                return None
            
            if (df[col] < 0).any() or (df[col] > 100).any():
                print(f"경고: '{col}' 컬럼에 0점 미만이나 100점 초과의 비정상 점수가 있습니다.")

        print(f"성공: '{file_path}' 데이터를 성공적으로 불러왔습니다.")
        return df

    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")
        return None
    
if __name__ == "__main__":
    data = load_data("scores.csv")
    if data is not None:
        print(data.head())