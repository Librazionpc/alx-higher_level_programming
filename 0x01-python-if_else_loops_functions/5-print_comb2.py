#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print(f"0{i}", end=", ")
        continue
    elif (i == 99):
        print(i)
        break
    print(i, end=", ")
