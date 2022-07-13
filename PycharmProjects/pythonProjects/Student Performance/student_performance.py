import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


def load_report_cards(directory, num_students):
    report_cards_ = []

    for student_number in range(num_students):
        report_card = load_report_card(directory, student_number)
        report_cards_.append(report_card)

    return report_cards_


def add_student_averages(report_cards_, subjects):
    for report_card in report_cards_:
        sum_of_marks = 0

        for key, value in report_card.items():
            if key not in subjects:
                continue

            sum_of_marks += value

        average = sum_of_marks / len(subjects)
        # add a new key to the report card with the average
        report_card["average"] = average


def get_average_student_grade(report_cards_):
    sum_of_averages = 0

    for report_card in report_cards_:
        sum_of_averages += report_card["average"]

    return sum_of_averages / len(report_cards_)


def get_subject_averages(report_cards_, subjects):
    subject_averages_ = {subject: 0 for subject in subjects}

    for report_card in report_cards_:
        for subject in subjects:
            mark = report_card[subject]
            subject_averages_[subject] += mark

    for subject in subjects:
        subject_averages_[subject] /= len(report_cards_)

    return subject_averages_


def get_grade_level_averages(report_cards_):
    grade_level_averages_ = {grade: [] for grade in range(1, 9)}

    for report_card in report_cards_:
        grade = report_card["grade"]
        average = report_card["average"]

        grade_level_averages_[grade].append(average)

    for grade in grade_level_averages_:
        grade_level_averages_[grade] = sum(
            grade_level_averages_[grade]) / len(grade_level_averages_[grade])

    return grade_level_averages_


report_cards = load_report_cards("students", NUM_STUDENTS)
add_student_averages(report_cards, SUBJECTS)

average_student_grade = round(get_average_student_grade(report_cards), 2)

subject_averages = get_subject_averages(report_cards, SUBJECTS)
sorted_subject_averages = sorted(subject_averages.items(), key=lambda x: x[1])
hardest_subject = sorted_subject_averages[0][0]
easiest_subject = sorted_subject_averages[-1][0]

grade_level_averages = get_grade_level_averages(report_cards)
sorted_grade_level_averages = sorted(
    grade_level_averages.items(), key=lambda x: x[1])
best_grade_level = sorted_grade_level_averages[-1][0]
worst_grade_level = sorted_grade_level_averages[0][0]

students_sorted_by_grade = sorted(report_cards, key=lambda x: x['average'])
best_student = students_sorted_by_grade[-1]["id"]
worst_student = students_sorted_by_grade[0]["id"]

print("Average Student Grade:", average_student_grade)
print("Hardest Subject:", hardest_subject)
print("Easiest Subject:", easiest_subject)
print("Best Performing Grade:", best_grade_level)
print("Worst Performing Grade:", worst_grade_level)
print("Best Student ID:", best_student)
print("Worst Student ID:", worst_student)
