# excercise tracker
import time
import csv
import os


def main():
    welcome_header()
    home()


def welcome_header():
    print(
        """
/$$$$$$$$                                         /$$                           /$$$$$$$$                           /$$                          
| $$_____/                                        |__/                          |__  $$__/                          | $$                          
| $$       /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$$  /$$$$$$          | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$$$$   |  $$ /$$/ /$$__  $$ /$$__  $$ /$$_____/| $$ /$$_____/ /$$__  $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$__/    \\  $$$$/ | $$$$$$$$| $$  \\__/| $$      | $$|  $$$$$$ | $$$$$$$$         | $$| $$  \\__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \\__/
| $$        >$$  $$ | $$_____/| $$      | $$      | $$ \\____  $$| $$_____/         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
| $$$$$$$$ /$$/\\  $$|  $$$$$$$| $$      |  $$$$$$$| $$ /$$$$$$$/|  $$$$$$$         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \\  $$|  $$$$$$$| $$      
|________/|__/  \\__/ \\_______/|__/       \\_______/|__/|_______/  \\_______/         |__/|__/      \\_______/ \\_______/|__/  \\__/ \\_______/|__/      
=======================================================================================================================================================                                                        
        """
    )


def home():
    print(
        "Welcome to the exercise tracker! \nThis program will help you keep track of your exercises.\nPlease select an option below: \n(1) Add an exercise\n(2) View exercises\n(3) Remove exercise\n(4) Exit program"
    )
    option = int(input("Enter option number: "))
    match option:
        case 1:
            add_exercise()
        case 2:
            view_exercises()
        case 3:
            remove_excercise()
        case 4:
            exit_program()
        case _:
            print("Invalid option. Please try again.")
            home()


def add_exercise():
    print("\nAdd an exercise")
    exercise_name = input("Enter a unique exercise name: ")
    exercise_duration = input("Enter exercise duration (in minutes): ")
    exercise_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("exercises.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([exercise_name, exercise_duration, exercise_date])
    print("Exercise removed successfully!\n\n")
    key = input("Press enter to return to the home screen.")
    while True:
        if key == "":
            home()


def view_exercises():
    print("\nView exercises")
    with open("exercises.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Exercise: {row[0]}, Duration: {row[1]} min, Date: {row[2]}")
    print("\n")
    print("Exercise removed successfully!\n\n")
    key = input("Press enter to return to the home screen.")
    while True:
        if key == "":
            home()


def remove_excercise():
    print("\nRemove exercise")
    exercise_name = input("Enter exercise name to remove: ")
    with open("exercises.csv", mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open("exercises.csv", mode="w") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != exercise_name:
                writer.writerow(row)
    print("Exercise removed successfully!\n\n")
    key = input("Press enter to return to the home screen.")
    while True:
        if key == "":
            home()


def exit_program():
    print("\nExiting program. Goodbye!")
    time.sleep(1)
    exit()


main()
