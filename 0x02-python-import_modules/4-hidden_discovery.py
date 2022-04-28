#!/usr/bin/python3
import hidden_4
import string


def main():
    names = dir(hidden_4)
    for name in names:
        if name.startswith("__") is False:
            print(f"{name}")


if __name__ == "__main__":
    main()
