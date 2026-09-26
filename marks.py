def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, subject_count):
    return total / subject_count

def calculate_result(marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    return total, percentage
