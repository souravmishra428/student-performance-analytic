"""
functions.py
Reusable functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd


# ---------- Grading Rule ----------
def assign_grade(avg):
    """Return grade based on average marks."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def pass_fail(avg):
    """Pass if average >= 50, else Fail."""
    return "Pass" if avg >= 50 else "Fail"


# ---------- Data Loading ----------
def load_data(path="students.csv"):
    """Load CSV into a Pandas DataFrame."""
    df = pd.read_csv(path)
    return df


# ---------- Core Processing ----------
def process_students(df, subjects):
    """
    Add Total, Average, Grade, Result columns.
    Uses NumPy for numerical calculations and a loop for iteration.
    """
    totals = []
    averages = []
    grades = []
    results = []

    for _, row in df.iterrows():
        marks = row[subjects].to_numpy(dtype=float)   # NumPy array
        total = np.sum(marks)
        avg = np.mean(marks)

        totals.append(total)
        averages.append(round(avg, 2))
        grades.append(assign_grade(avg))
        results.append(pass_fail(avg))

    df["Total"] = totals
    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results
    return df


# ---------- Analysis Functions ----------
def top_students(df, n=3):
    """Return top n students by average."""
    return df.sort_values(by="Average", ascending=False).head(n)


def subject_wise_avg(df, subjects):
    """Return subject-wise class average (NumPy-based)."""
    result = {}
    for sub in subjects:
        result[sub] = round(float(np.mean(df[sub].to_numpy())), 2)
    return result


def class_statistics(df, subjects):
    """Return overall class stats."""
    all_marks = df[subjects].to_numpy()
    return {
        "class_average": round(float(np.mean(all_marks)), 2),
        "highest_average": float(df["Average"].max()),
        "lowest_average": float(df["Average"].min()),
        "highest_mark": int(all_marks.max()),
        "lowest_mark": int(all_marks.min()),
    }


def pass_fail_stats(df):
    """Return pass/fail counts and percentages."""
    counts = df["Result"].value_counts().to_dict()
    total = len(df)
    passed = counts.get("Pass", 0)
    failed = counts.get("Fail", 0)
    return {
        "passed": passed,
        "failed": failed,
        "pass_percentage": round(passed / total * 100, 2),
        "fail_percentage": round(failed / total * 100, 2),
    }


def department_wise_avg(df):
    """Average marks per department."""
    return df.groupby("Department")["Average"].mean().round(2).to_dict()