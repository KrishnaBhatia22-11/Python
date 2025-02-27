def grade_student(scores):
    avg = sum(scores) / len(scores)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

print(grade_student([85, 90, 78, 92, 88]))
print("Krishna Bhatia 1/23/SET/BCS/358")
