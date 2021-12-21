#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    result = ""
    for i in str:
        count += 1
        if (n == count-1):
            continue
        result += i
    return result
