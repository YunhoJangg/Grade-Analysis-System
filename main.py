import data_manager
import analyzer
import visualizer
import report_generator
import pandas as pd

def display_menu():
    print("\n" + "="*40)
    print("   성적 분석 및 PDF 리포트 생성 시스템")
    print("="*40)
    print("1. 성적 데이터 불러오기 (CSV)")
    print("2. 통계 분석 수행")
    print("3. 시각화 그래프 생성")
    print("4. PDF 리포트 자동 생성")
    print("5. 분석 결과 CSV 저장")
    print("0. 프로그램 종료")
    print("="*40)

def main():
    df = None
    stats = None

    while True:
        display_menu()
        choice = input("원하는 작업 번호를 선택하세요: ")

        if choice == '1':
            file_name = input("불러올 CSV 파일명을 입력하세요 (예: scores.csv): ")
            df = data_manager.load_data(file_name)

        elif choice == '2':
            if df is not None:
                df = analyzer.calculate_student_performance(df)
                stats = analyzer.get_class_statistics(df)
                print("\n[통계 분석 완료]")
                for key, val in stats.items():
                    print(f"- {key}: {val:.2f}")
            else:
                print("오류: 먼저 데이터를 불러와주세요. (1번 메뉴)")

        elif choice == '3':
            if df is not None and "Total" in df.columns:
                visualizer.create_visualizations(df)
            else:
                print("오류: 먼저 통계 분석을 수행해주세요. (2번 메뉴)")

        elif choice == '4':
            if df is not None and stats is not None:
                report_generator.generate_pdf_report(df, stats)
            else:
                print("오류: 분석 데이터 또는 통계치가 부족합니다. (2, 3번 메뉴 확인)")

        elif choice == '5':
            if df is not None:
                save_path = input("저장할 파일명을 입력하세요 (예: result.csv): ")
                df.to_csv(save_path, index=False)
                print(f"성공: 분석 결과가 '{save_path}'로 저장되었습니다.")
            else:
                print("오류: 저장할 데이터가 없습니다.")

        elif choice == '0':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()