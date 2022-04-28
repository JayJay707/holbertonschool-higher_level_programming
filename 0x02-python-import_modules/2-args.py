#!/usr/bin/python3
import sys


def main():
    nb = len(sys.argv) - 1
    if nb == 0:
        print("0 arguments.")
    else:
        print(f'{nb} argument{"s" if nb != 1 else ""}:')
        for i in range(nb):
            print(f"{i + 1}: {sys.argv[i + 1]}")


if __name__ == "__main__":
    main()
