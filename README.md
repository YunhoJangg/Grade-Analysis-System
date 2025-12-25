# 📊 성적 분석 & 자동 PDF 리포트 생성 시스템
**2025-2 경북대학교 "컴퓨팅사고와 SW코딩" 과목 프로젝트 과제**

CSV 파일 형태의 학생 성적 데이터를 불러와 통계 분석을 수행하고, 시각화 그래프를 포함한 전문적인 PDF 리포트를 자동으로 생성하는 프로그램

## 1. 주요 기능 (Key Features)
- **데이터 로드 및 검증**: CSV 파일을 Pandas DataFrame으로 읽어오며, 점수 범위 및 데이터 타입을 검증합니다.
- **통계 분석**: 각 학생의 총점/평균 계산 및 학급 전체의 중앙값, 분위수 등 상세 통계치를 산출합니다.
- **데이터 시각화**: Matplotlib을 활용하여 학생별 총점 막대 그래프, 성적 분포 히스토그램, 시험별 평균 선 그래프를 생성합니다.
- **PDF 리포트 생성**: 분석 결과와 그래프 이미지를 결합한 PDF 문서를 자동으로 생성 및 저장합니다.
- **예외 처리**: 파일 누락, 데이터 형식 오류 등에 대한 사용자 친화적인 안내 메시지를 제공합니다.

## 2. 기술 스택 (Technology Stack)
- **언어**: Python
- **데이터 처리**: NumPy, Pandas  
- **시각화**: Matplotlib  
- **리포트 생성**: fpdf2

## 3. 프로젝트 구조 (Module Structure)
유지보수와 확장이 용이하도록 기능을 모듈화했습니다.
- `main.py`: 프로그램 실행 및 메뉴 인터페이스 제어  
- `data_manager.py`: CSV 입출력 및 데이터 유효성 검사  
- `analyzer.py`: 통계 연산 및 수치 데이터 분석  
- `visualizer.py`: 데이터 기반 그래프 생성 및 저장  
- `report_generator.py`: 분석 결과와 이미지를 PDF로 변환  

## 4. 시작하기 (Getting Started)

### 설치 방법
```bash
git clone https://github.com/YunhoJangg/Grade-Analysis-System.git
cd Grade-Analysis-System
pip install -r requirements.txt
