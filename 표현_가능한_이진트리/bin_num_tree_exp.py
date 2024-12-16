from math import log2, floor

def convert_to_bin_str(number):
    bin_chars = []
    while number > 0:
        number, rem = divmod(number, 2)
        bin_chars.append(str(rem))
    pad_len = pow(2, floor(log2(len(bin_chars))) + 1) - 1 - len(bin_chars)
    bin_chars.extend(["0" * pad_len])
    return "".join(bin_chars[::-1])
        
    
def check_valid_tree(bin_str, start, end):
    length = end - start
    
    if length <= 0: return False

    if length == 1:
        return True
    
    mid = (start + end) // 2
    
    if bin_str[mid] == "0" and any(num != "0" for num in bin_str):
        return False
    
    left_validity = check_valid_tree(bin_str, start, mid)
    right_validity = check_valid_tree(bin_str, mid + 1, end)
    return left_validity and right_validity
    

def solution(numbers):
    bin_strs = [convert_to_bin_str(num) for num in numbers]
    ans = []
    
    for bin_str in bin_strs:
        breakpoint()
        if check_valid_tree(bin_str, start=0, end=len(bin_str)):
            ans.append(1)
        else:
            ans.append(0)
    
    return ans


if __name__ == "__main__":
    print(solution([15]))
    # print(solution([63, 111, 95]))
