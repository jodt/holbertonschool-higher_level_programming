#!/usr/bin/python3
"""
This is the add_item module
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file').load_from_json_file

arg_list = sys.argv
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

for i in range(1, len(arg_list)):
    my_list.append(arg_list[i])

save_to_json_file(my_list, filename)
