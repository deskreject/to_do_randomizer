import csv
import random
import os

def read_csv():
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return list(reader)

def select_task(tasks):
    return random.choice(tasks)

def ask_proceed(task):
    answer = input(f"Do you want to proceed with this task: {task}? (y/n) ")
    return answer.lower() == 'y'

def ask_completion():
    while True:
        completion = float(input("How much of the task did you complete? (0-1) "))
        if 0 <= completion <= 1:
            return completion
        print("Invalid input. Please enter a number between 0 and 1.")

def ask_new_task():
    answer = input("Do you want to add a new task? (y/n) ")
    return answer.lower() == 'y'

def get_new_task():
    name = input("Enter the name of the new task: ")
    category = input("Enter the category of the new task: ")
    return [name, '', category]

def write_csv(task):
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(task)

def main():
    tasks = read_csv()
    while True:
        task = select_task(tasks)
        if ask_proceed(task):
            ask_completion()
        if ask_new_task():
            new_task = get_new_task()
            write_csv(new_task)
        else:
            break

if __name__ == "__main__":
    main()