#!/usr/bin/python3
import sys


def main():
    nb = 0
    for i in range(len(sys.argv) - 1):
        nb += int(sys.argv[i+1])
    print(f"{nb}")


if __name__ == "__main__":
    main()
