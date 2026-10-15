"""
main.py
Student Performance Analytics System - Main Program
"""

from functions import (
    load_data,
    process_students,
    top_students,
    subject_wise_avg,
    class_statistics,
    pass_fail_stats,
    department_wise_avg,
)

SUBJECTS = ["Math", "Science", "English", "Computer"]


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def main():
    # Step 1: Load data
    df = load_data("students.csv")

    print_header("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Total records loaded: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    print("\n--- First 5 Records ---")
    print(df.head().to_string(index=False))

    # Step 2: Process data
    df = process_students(df, SUBJECTS)

    print("\n--- Processed Data (with Total / Average / Grade / Result) ---")
    print(df.to_string(index=False))

    # Step 3: Analysis
    print_header("CLASS STATISTICS")
    stats = class_statistics(df, SUBJECTS)
    for k, v in stats.items():
        print(f"{k.replace('_', ' ').title():<20}: {v}")

    print_header("SUBJECT-WISE AVERAGE")
    for sub, avg in subject_wise_avg(df, SUBJECTS).items():
        print(f"{sub:<12}: {avg}")

    print_header("PASS / FAIL STATISTICS")
    pf = pass_fail_stats(df)
    for k, v in pf.items():
        print(f"{k.replace('_', ' ').title():<20}: {v}")

    print_header("DEPARTMENT-WISE AVERAGE")
    for dept, avg in department_wise_avg(df).items():
        print(f"{dept:<12}: {avg}")

    print_header("TOP 3 PERFORMERS")
    top = top_students(df, 3)
    for _, row in top.iterrows():
        print(f"{row['Name']:<20} Avg: {row['Average']:<6} Grade: {row['Grade']}")

    # Best subject
    subj_avgs = subject_wise_avg(df, SUBJECTS)
    best_subject = max(subj_avgs, key=subj_avgs.get)
    print_header("KEY INSIGHTS")
    print(f"Best performing subject : {best_subject} ({subj_avgs[best_subject]})")
    print(f"Top student             : {top.iloc[0]['Name']} "
          f"(Avg: {top.iloc[0]['Average']}, Grade: {top.iloc[0]['Grade']})")
    print(f"Overall class average   : {stats['class_average']}")
    print(f"Students passed         : {pf['passed']} / {len(df)} "
          f"({pf['pass_percentage']}%)")


if __name__ == "__main__":
    main()