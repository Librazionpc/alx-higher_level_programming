#!/usr/bin/python3.8
import hidden_4


def main():
    lists = dir(hidden_4)
    for i in range(len(lists)):
        if lists[i][0] == '_' and lists[i][1] == '_':
            continue
        else:
            print("{}".format(l[i]))


if __name__ == "__main__":
    main()
