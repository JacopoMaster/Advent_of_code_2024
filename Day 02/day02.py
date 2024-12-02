def is_safe_report(report):
    """
    🎄 Check if a report is 'nice' according to Santa's safety rules: 🎅
    1. All levels must either be steadily increasing or steadily decreasing. 
    2. Adjacent levels must differ by at least 1 and no more than 3. 
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if not all(-3 <= diff <= -1 or 1 <= diff <= 3 for diff in differences):
        return False
    
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    
    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    """
    🎅 Check if a report becomes 'nice' with the Problem Dampener (Santa's magical forgiveness tool 🎁✨):
    It allows removing one naughty level to save an otherwise nice report! 🛠️
    """
    #
    if is_safe_report(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    
    return False


def count_safe_reports(file_path):
    """
    🎄 Count the number of 'nice' reports according to Santa's original safety rules. 🎅
    """
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report):
                safe_count += 1  
                
    return safe_count


def count_safe_reports_with_dampener(file_path):
    """
    🎁 Count the number of 'nice' reports with the magical help of the Problem Dampener. ✨
    """
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1  
                
    return safe_count



file_path = 'input.txt'  


safe_reports = count_safe_reports(file_path)
safe_reports_with_dampener = count_safe_reports_with_dampener(file_path)


print(f"🎄 Reports that are nice without Santa's Problem Dampener: {safe_reports} 🎁")
print(f"🎅 Reports that are nice with Santa's magical Problem Dampener: {safe_reports_with_dampener} ✨")
