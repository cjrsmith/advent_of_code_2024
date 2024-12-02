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

def remove_item(report, index):
    new_list = report.copy()
    new_list.pop(index)
    return new_list

safe_reports = 0
report = []
new_report = []
input_file = open("./input")
for r in input_file.readlines():
    report = [int(x) for x in r.split(" ")]
    if not contains_duplicates(report) and (is_safely_ascending(report) or is_safely_descending(report)):
        safe_reports += 1
    else: 
        for i, level in enumerate(report):
            new_report = remove_item(report, i)
            if not contains_duplicates(new_report) and (is_safely_ascending(new_report) or is_safely_descending(new_report)):
                safe_reports += 1
                break

print(safe_reports)
