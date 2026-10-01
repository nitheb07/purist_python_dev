"""
Final task - sample solution: Student Grade Tracker
Reuses: input, lists, loops, conditionals, functions, type hints.

Run:  python final_task_solution.py
"""
from typing import List


class Student:
    pass_mark = 40

    def __init__(self, name: str):
        self.name = name
        self.grades: List[int] = []

    def add_grade(self, grade: int):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def average(self) -> float:
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

    def status(self) -> str:
        if self.average() >= self.pass_mark:
            return "pass"
        return "fail"

    def describe(self) -> str:
        return "%s: average %.1f -> %s" % (self.name, self.average(), self.status())


class HonorsStudent(Student):
    pass_mark = 60          # same behavior, stricter rule


def read_grades(student: Student):
    """Keep asking for grades until the user types -1."""
    grade = int(input("Grade for %s (-1 to stop): " % student.name))
    while grade != -1:
        student.add_grade(grade)
        grade = int(input("Grade for %s (-1 to stop): " % student.name))


if __name__ == "__main__":
    students = [Student("Asha"), HonorsStudent("Ravi")]
    for student in students:
        read_grades(student)
    print()
    for student in students:
        print(student.describe())
