#!/usr/bin/python3
import hidden_4
names_list = dir(hidden_4)
for name in names_list:
    if (name[0] == "_"):
        continue
    else:
        print("{}".format(name))
