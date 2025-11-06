def find_large(num):
    large_num = 0
    for number in num:
        if large_num < number:
            large_num = number
    return large_num
