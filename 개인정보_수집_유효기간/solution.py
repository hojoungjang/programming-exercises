from math import ceil

def calc_expiry(start_date, month_offset):
    year, month, day = [int(val) for val in start_date.split(".")]
    
    year_offset = (month + month_offset - 1) // 12
    new_month = (month + month_offset- 1) % 12 + 1
    new_year = year + year_offset
    new_day = day - 1
    
    if new_day == 0:
        new_day = 28
        new_month -= 1
        
    if new_month == 0:
        new_month = 12
        new_year -= 1
    
    return ".".join([
        str(new_year),
        str(new_month).zfill(2),
        str(new_day).zfill(2),
    ])

def solution(today, terms, privacies):
    cat_terms = {}
    for t in terms:
        cat, month_offset = t.split(" ")
        cat_terms[cat] = int(month_offset)
    
    answer = []
    for i, privacy_data in enumerate(privacies):
        date_str, cat = privacy_data.split(" ")
        expiry_date = calc_expiry(date_str, cat_terms[cat])
        if expiry_date < today:
            answer.append(i+1)
    
    return answer


if __name__ == "__main__":
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
