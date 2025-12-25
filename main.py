import tkinter as tk
from tkinter import filedialog, messagebox
import data_manager
import analyzer
import visualizer
import report_generator
import os

class GradeAnalysisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("성적 분석 및 PDF 리포트 시스템")
        self.root.geometry("380x540")
        
        self.df = None
        self.stats = None

        tk.Label(root, text="성적 분석 시스템", font=("Arial", 18, "bold")).pack(pady=30)

        btn_style = {"width": 35, "height": 2, "font": ("Arial", 10)}
        
        tk.Button(root, text="1. CSV 데이터 불러오기", command=self.load_file, **btn_style).pack(pady=10)
        tk.Button(root, text="2. 통계 분석 실행", command=self.run_analysis, **btn_style).pack(pady=10)
        tk.Button(root, text="3. 시각화 그래프 생성", command=self.run_visualize, **btn_style).pack(pady=10)
        tk.Button(root, text="4. PDF 리포트 자동 생성", command=self.run_report, **btn_style).pack(pady=10)
        tk.Button(root, text="5. 분석 결과 CSV로 저장", command=self.save_csv, **btn_style).pack(pady=10)

        self.status_var = tk.StringVar(value="파일을 불러와주세요.")
        self.status_label = tk.Label(root, textvariable=self.status_var, fg="blue", font=("Arial", 9))
        self.status_label.pack(pady=20)

        copyright_text = "Made by Yunho Jang"
        tk.Label(root, text=copyright_text, fg="gray", font=("Arial", 8)).pack(side="bottom", pady=15)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.df = data_manager.load_data(file_path)
            if self.df is not None:
                self.status_var.set(f"로드 완료: {os.path.basename(file_path)}")
                self.status_label.config(fg="green")
            else:
                messagebox.showerror("오류", "데이터 형식이 잘못되었거나 파일을 읽을 수 없습니다.")

    def run_analysis(self):
        if self.df is not None:
            self.df = analyzer.calculate_student_performance(self.df)
            self.stats = analyzer.get_class_statistics(self.df)
            messagebox.showinfo("분석 완료", f"학급 평균: {self.stats['Mean']:.2f}\n최고점: {self.stats['Max']:.2f}")
            self.status_var.set("통계 분석이 완료되었습니다.")
        else:
            messagebox.showwarning("주의", "먼저 CSV 파일을 불러와주세요.")

    def run_visualize(self):
        if self.df is not None and "Total" in self.df.columns:
            visualizer.create_visualizations(self.df)
            messagebox.showinfo("시각화 완료", "그래프가 'plots' 폴더에 저장되었습니다.")
            self.status_var.set("시각화 그래프 생성이 완료되었습니다.")
        else:
            messagebox.showwarning("주의", "먼저 통계 분석(2번)을 수행해주세요.")

    def run_report(self):
        if self.df is not None and self.stats is not None:
            try:
                report_generator.generate_pdf_report(self.df, self.stats)
                messagebox.showinfo("성공", "PDF 리포트가 성공적으로 생성되었습니다.")
                self.status_var.set("PDF 리포트 생성이 완료되었습니다.")
            except Exception as e:
                messagebox.showerror("오류", f"리포트 생성 중 오류 발생: {e}")
        else:
            messagebox.showwarning("주의", "분석 데이터가 부족합니다 (1~3번 과정 확인).")

    def save_csv(self):
        if self.df is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if save_path:
                self.df.to_csv(save_path, index=False)
                messagebox.showinfo("저장 완료", f"결과가 {os.path.basename(save_path)}에 저장되었습니다.")
        else:
            messagebox.showwarning("주의", "저장할 데이터가 없습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeAnalysisGUI(root)
    root.mainloop()