
def contains_duplicates(report):
    return len(report) != len(set(report))
    
def is_safely_ascending(report):
    for i, level in enumerate(report):
        if i == 0:
            continue
        if level < report[i-1]:
            return False
        if is_valid_difference(level, report[i-1]):
            continue
        else:
            return False
    return True

def is_safely_descending(report):
    for i, level in enumerate(report):
        if i == 0:
            continue
        if level > report[i-1]:
            return False
        if is_valid_difference(level, report[i-1]):
            continue
        else:
            return False
    return True

def is_valid_difference(x, y):
    return 1 <= abs(x - y) <= 3

safe_reports = 0

input_file = open("./input")
for report in input_file.readlines():
    report = [int(x) for x in report.split(" ")]
    if not contains_duplicates(report):
        if is_safely_ascending(report) or is_safely_descending(report):
            safe_reports += 1

print(safe_reports)
