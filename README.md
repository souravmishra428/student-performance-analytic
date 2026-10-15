# Student Performance Analytics System

**Student:** Your Name
**Course:** Python with AI – EWB Courses
**Submission Date:** 15 October 2026

## Objective
Analyze student marks and attendance data using NumPy and Pandas to
generate grades, pass/fail results, subject-wise performance, and
top performers.

## Technologies Used
- Python 3.x
- NumPy
- Pandas

## Dataset
`students.csv` — 20 student records with columns:
StudentID, Name, Department, Math, Science, English, Computer, Attendance.

## Implementation
1. Load CSV with Pandas.
2. Process each student's marks with NumPy (`sum`, `mean`).
3. Assign grades and pass/fail using defined rules.
4. Compute subject-wise, department-wise and class statistics.
5. Display top performers and key insights.

## Grading Rule
| Average | Grade |
|---------|-------|
| ≥ 90 | A+ |
| ≥ 80 | A |
| ≥ 70 | B |
| ≥ 60 | C |
| ≥ 50 | D |
| < 50 | F |

Pass condition: Average ≥ 50.

## How to Run
```bash
pip install pandas numpy
python main.py