"""
This script is a to-do randomizer. It reads tasks from a CSV file, 
randomly selects a task, and asks the user if they want to proceed with the task.
If the user wants to add a new task, it asks for the task details and writes them to the CSV file.
"""

import csv
import random
import os

def read_csv():
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return list(reader)

def select_task(tasks):
    category = random.choice([task[2] for task in tasks])  # Randomly choose a category
    filtered_tasks = [task for task in tasks if task[2] == category]  # Filter tasks by category
    return random.choice(filtered_tasks)[0]  # Randomly select a name from the filtered tasks
# Use a weighted random choice where the weights are the completion rates
    task = random.choices(filtered_tasks, weights=[float(filtered_tasks[1]) for task in tasks], k=1)[0]
    return task

def ask_proceed(task):
    answer = input(f"Do you want to proceed with this task: {task}? (y/n) ")
    if answer.lower() == 'n':
        delete_task = input("Do you want to delete this task from the CSV? (y/n) ")
        if delete_task.lower() == 'y':
            delete_row(task)
            tasks = read_csv()
            task = select_task(tasks)
    return task

def delete_row(task):
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != task:
                writer.writerow(row)

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
    return [name, 0, category]

def write_csv(task, new_task=None):
    tasks = read_csv()
    # Update the completion rate of the selected task
    for t in tasks:
        if t[0] == task[0]:
            t[1] = str(task[1])
    # Add the new task if any
    if new_task:
        tasks.append(new_task)
    with open('C:\\Users\\astaub1\\Python_work\\to_do_randomizer\\Data\\database_todos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'completion_rate', 'category'])  # Write the header
        writer.writerows(tasks)  # Write the tasks

def main():
    tasks = read_csv()
    while True:
        task = select_task(tasks)
        while True:
            task = ask_proceed(task)
            if task:
                break
        completion = ask_completion()
        task[1] = completion  # Update the completion rate in the task
        write_csv(task)  # Write the updated task to the CSV
        if ask_new_task():
            new_task = get_new_task()
            write_csv(task, new_task)
        else:
            break

if __name__ == "__main__":
    main()