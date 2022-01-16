#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Grading chart


def grading(mark: str):
    # grading function to return middle grade

    # defining conversion chart
    chart = {
        "4+": "97.5",
        "4": "90.5",
        "4-": "83",
        "3+": "78",
        "3": "74.5",
        "3-": "71",
        "2+": "68",
        "2": "64.5",
        "2-": "61",
        "1+": "58",
        "1": "54.5",
        "1-": "51",
        "R": "24.5",
    }

    # process
    return chart[mark] if mark in chart else chart["1-"]


def main():
    # main function for multiplication table

    # input
    mark_inp = input("Enter the level you want converted to a precentage: ")

    # output/calling function
    print(f"Level {mark_inp} has a middle precentage of {grading(mark_inp)}%")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
