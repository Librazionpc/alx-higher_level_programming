#!/usr/bin/python3.8
import hidden_4


def main():
    lists = dir(hidden_4)
    for i in lists:
        if i[0] != "_" and i[1] != "_":
            print(i)


if __name__ == "__main__":
    main()
