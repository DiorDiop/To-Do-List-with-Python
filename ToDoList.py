#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import library
import csv


# In[2]:


# Create an empty list to store tasks
tasks = []


# In[ ]:



# Create the to do list table
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Mark Task as Done")
    print("5. Save Tasks to CSV")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")
    elif choice == "2":
        try:
            task_index = int(input("Enter the task number to delete: "))
            if 1 <= task_index <= len(tasks):
                deleted_task = tasks.pop(task_index - 1)
                print(f"Task '{deleted_task['task']}' deleted successfully!")
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == "3":
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")
    elif choice == "4":
        try:
            task_index = int(input("Enter the task number to mark as done: "))
            if 1 <= task_index <= len(tasks):
                tasks[task_index - 1]["done"] = True
                print(f"Task '{tasks[task_index - 1]['task']}' marked as done!")
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == "5":
        try:
            # Prompt the user for the file path where they want to save the CSV file
            file_path = input("Enter the file path to save the CSV file (e.g., 'todolist.csv'): ")
            with open(file_path, "w", newline="") as file:
                csv_writer = csv.DictWriter(file, fieldnames=["task", "action"])
                csv_writer.writeheader()
                for task in tasks:
                    action = "Done" if task["done"] else "Not Done"
                    csv_writer.writerow({"task": task["task"], "action": action})
            print(f"Tasks saved to '{file_path}' successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


# In[ ]:




