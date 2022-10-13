#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 13, 2022
# This program creates different statements depending on user's integer


def main():
    # get integer from user

    integer = float(input("Enter an integer: "))

    if integer < 0:
        print("that is a negative number")

    elif integer >= 1:
        print("that is a positive number")

    elif integer == 0:
        print("that is a null number")

    else:
        print("Error, I don't think thats a integer")


if __name__ == "__main__":
    main()
