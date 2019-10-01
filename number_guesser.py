#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: September 2019
# This program gets the user to guess a number

import constants


def main():

    while True:
        # imput
        number_guessed = int(input("pick a number between 0-9:"))

        # process
        if number_guessed == constants.right_number:
            # output
            print("You win, you guessed the number")
            break
        else:
            print("wrong, try again")


if __name__ == "__main__":
    main()
