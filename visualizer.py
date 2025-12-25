import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_visualizations(df):
    if not os.path.exists("plots"):
        os.makedirs("plots")

    plt.figure(figsize=(10, 6))
    plt.bar(df["Name"], df["Total"], color='skyblue')
    plt.title("학생별 총점 현황")
    plt.xlabel("학생 이름")
    plt.ylabel("총점")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/total_scores.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.hist(df["Average"], bins=10, color='lightgreen', edgecolor='black')
    plt.title("평균 점수 분포")
    plt.xlabel("평균 점수")
    plt.ylabel("학생 수")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("plots/score_distribution.png")
    plt.close()

    exam_labels = ["중간고사", "기말고사", "과제"]
    exam_means = [df["Midterm"].mean(), df["Final"].mean(), df["Homework"].mean()]
    
    plt.figure(figsize=(8, 5))
    plt.plot(exam_labels, exam_means, marker='o', linestyle='-', color='orange', linewidth=2)
    plt.title("시험 유형별 성적 추이")
    plt.xlabel("시험 유형")
    plt.ylabel("평균 점수")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.savefig("plots/exam_comparison.png")
    plt.close()
    
    print("성공: 모든 그래프 이미지가 'plots' 폴더에 저장되었습니다.")

if __name__ == "__main__":
    from data_manager import load_data
    from analyzer import calculate_student_performance
    df = load_data("scores.csv")
    if df is not None:
        df = calculate_student_performance(df)
        create_visualizations(df)