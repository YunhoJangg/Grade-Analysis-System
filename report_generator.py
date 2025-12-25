from fpdf import FPDF
import datetime
import os

class GradeReport(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 15)
        self.cell(0, 10, "Student Performance Analysis Report", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')} | Page {self.page_no()}", align='C')

def generate_pdf_report(df, stats, output_path="grade_report.pdf"):
    pdf = GradeReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Class Statistics Summary", ln=True)
    pdf.set_font("Arial", size=11)
    
    pdf.cell(0, 10, f"- Class Mean: {stats['Mean']:.2f}", ln=True)
    pdf.cell(0, 10, f"- Maximum Score: {stats['Max']:.2f}", ln=True)
    pdf.cell(0, 10, f"- Minimum Score: {stats['Min']:.2f}", ln=True)
    pdf.cell(0, 10, f"- Median: {stats['Median']:.2f}", ln=True)
    pdf.cell(0, 10, f"- Top 25% Cut: {stats['Top25']:.2f}", ln=True)
    pdf.ln(5)

    interpretation = f"The overall class average is {stats['Mean']:.2f}, and the highest score is {stats['Max']:.2f}."
    pdf.multi_cell(0, 10, f"Analysis: {interpretation}")
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Performance Visualizations", ln=True)

    if {"total_scores.png", "score_distribution.png", "exam_comparison.png"}.issubset(set(os.listdir("plots"))):
        pdf.image("plots/total_scores.png", x=10, y=None, w=180)
        pdf.ln(5)
        pdf.image("plots/score_distribution.png", x=10, y=None, w=90)
        pdf.image("plots/exam_comparison.png", x=105, y=None, w=90)

    pdf.output(output_path)
    print(f"성공: PDF 리포트가 '{output_path}'로 생성되었습니다.")

if __name__ == "__main__":
    import os
    from data_manager import load_data
    from analyzer import calculate_student_performance, get_class_statistics
    
    df = load_data("scores.csv")
    if df is not None:
        df = calculate_student_performance(df)
        stats = get_class_statistics(df)
        generate_pdf_report(df, stats)