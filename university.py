
from dataclasses import dataclass
from typing import List


# Scholarship eligibility criteria
MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARK = 60.0
MIN_ATTENDANCE = 75.0
MAX_FAMILY_INCOME = 250000


@dataclass
class Applicant:
    applicant_id: str
    name: str
    subject_marks: List[float]
    attendance: float
    family_income: float

    @property
    def aggregate(self):
        return sum(self.subject_marks) / len(self.subject_marks)

    @property
    def minimum_subject_mark(self):
        return min(self.subject_marks)


def evaluate_eligibility(applicant):
    """Check all scholarship eligibility conditions."""

    if not applicant.subject_marks:
        return False, "No subject marks provided"

    if any(mark < 0 or mark > 100
           for mark in applicant.subject_marks):
        return False, "Invalid subject marks"

    if not 0 <= applicant.attendance <= 100:
        return False, "Invalid attendance"

    if applicant.family_income < 0:
        return False, "Invalid family income"

    if applicant.aggregate < MIN_AGGREGATE:
        return False, "Aggregate marks below minimum"

    if applicant.minimum_subject_mark < MIN_SUBJECT_MARK:
        return False, "Subject-wise minimum not satisfied"

    if applicant.attendance < MIN_ATTENDANCE:
        return False, "Attendance below minimum"

    if applicant.family_income > MAX_FAMILY_INCOME:
        return False, "Family income exceeds limit"

    return True, "Eligible"


def rank_applicants(applicants):
    """Separate eligible applicants and rank them by merit."""

    eligible = []
    rejected = []

    for applicant in applicants:
        status, reason = evaluate_eligibility(applicant)

        if status:
            eligible.append(applicant)
        else:
            rejected.append((applicant, reason))

    # Ranking and tie-breaking rules:
    # 1. Higher aggregate marks
    # 2. Higher attendance
    # 3. Lower family income
    # 4. Higher minimum subject mark
    # 5. Applicant ID in ascending order
    eligible.sort(
        key=lambda a: (
            -a.aggregate,
            -a.attendance,
            a.family_income,
            -a.minimum_subject_mark,
            a.applicant_id
        )
    )

    return eligible, rejected


def display_results(eligible, rejected):
    print("\n===== SCHOLARSHIP MERIT LIST =====")

    if not eligible:
        print("No eligible applicants found.")

    for rank, applicant in enumerate(eligible, start=1):
        print(
            f"Rank: {rank} | "
            f"ID: {applicant.applicant_id} | "
            f"Name: {applicant.name} | "
            f"Aggregate: {applicant.aggregate:.2f}% | "
            f"Attendance: {applicant.attendance:.1f}% | "
            f"Income: Rs. {applicant.family_income:.0f}"
        )

    print("\n===== INELIGIBLE APPLICANTS =====")

    for applicant, reason in rejected:
        print(
            f"ID: {applicant.applicant_id} | "
            f"Name: {applicant.name} | "
            f"Reason: {reason}"
        )


def main():
    applicants = [
        Applicant("S104", "Ananya",
                  [85, 90, 88, 92], 90, 180000),

        Applicant("S102", "Rahul",
                  [85, 90, 88, 92], 90, 150000),

        Applicant("S103", "Priya",
                  [80, 82, 78, 85], 95, 200000),

        Applicant("S105", "Kiran",
                  [90, 92, 55, 88], 95, 120000),

        Applicant("S106", "Meena",
                  [78, 80, 82, 79], 70, 100000),

        Applicant("S107", "Arjun",
                  [88, 90, 91, 89], 92, 300000),
    ]

    eligible, rejected = rank_applicants(applicants)
    display_results(eligible, rejected)


if __name__ == "__main__":
    main()
