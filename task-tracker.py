
# Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track
# what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills,
# including working with the filesystem, handling user inputs, and building a simple CLI application.

# Requirements
# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file.
# The user should be able to:

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

#Here are some constraints to guide the implementation:

# Use positional arguments in command line to accept user inputs.
'''
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.
'''
# Example
'''
The list of commands and their usage is given below:

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
'''
import json
import random
import datetime
def add_task(description):
    '''
    id: A unique identifier for the task
    description: A short description of the task
    status: The status of the task (todo, in-progress, done)
    createdAt: The date and time when the task was created
    updatedAt: The date and time when the task was last updated
    Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.
    '''
    data = {'id':int(random.random()*100*4123),'description':description,'status':'todo','createdAt':str(datetime.datetime.now()),'updatedAt':str(datetime.datetime.now())}
    with open('data.json', 'r+') as f:
        file_data = json.load(f)
        file_data["tasks"].append(data)
        f.seek(0)
        json.dump(file_data, f)
        print(f"New Task added successfully!")

'''
# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
'''
def delete_task(id):
    with open('data.json','r+') as f:
        file_data = json.load(f)
        found = False
        for idx, obj in enumerate(file_data["tasks"]):
            if obj['id'] == int(id):
                file_data['tasks'].pop(idx)
                found = True
        if(found==False):
            print("Task doesn't exist!")
        else:
            f.seek(0)
            f.truncate()
            json.dump(file_data, f)
            print(f"Task #{id} deleted successfully!")


def update_task(id,description):
    with open('data.json', 'r+') as f:
        file_data = json.load(f)
        found = False
        index = 0
        for i in range(0,len(file_data["tasks"])):
            if(file_data["tasks"][i]['id']==int(id)):
                found = True
                if i==index:
                    file_data["tasks"][index]['description']=description
                    file_data["tasks"][index]['updatedAt']=str(datetime.datetime.now())
                # data = {'id':int(id),'description':description,'status':file_data["tasks"][i]['status'],'createdAt':file_data["tasks"][i]['createdAt'],'updatedAt':str(datetime.datetime.now())}
            else:
                index=+1
            if(found==False):
                print("Task doesn't exist!")
            else:
                f.seek(0)
                f.truncate()
                json.dump(file_data, f)
                print(f"Task #{id}'s description updated successfully!")

'''
# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1
'''

def mark_task(status,id):
    with open('data.json','r+') as f:
        file_data = json.load(f)
        found = False
        index = 0
        for i in range(0,len(file_data["tasks"])):
            if(file_data["tasks"][i]['id']==int(id)):
                found = True
                if i==index:
                    file_data["tasks"][index]['status']=status
                    file_data["tasks"][index]['updatedAt']=str(datetime.datetime.now())
                # data = {'id':int(id),'description':description,'status':file_data["tasks"][i]['status'],'createdAt':file_data["tasks"][i]['createdAt'],'updatedAt':str(datetime.datetime.now())}
            else:
                index=+1
        if(found==False):
            print("Task doesn't exist!")
        else:
            f.seek(0)
            f.truncate()
            json.dump(file_data, f)
            print(f"Task #{id}'s status updated successfully!")

'''
# Listing all tasks
task-cli list
'''
def display():
    with open('data.json','r+') as f:
            file_data = json.load(f)
            for i in (file_data['tasks']):
                print(i)
'''
# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
'''
def display_status(status):
    with open('data.json','r') as f:
        file_data = json.load(f)
        for i in range(0,len(file_data['tasks'])):
            if(file_data['tasks'][i]['status']==status):
                print(file_data['tasks'][i])
# Task Properties
# Each task should have the following properties:

'''
id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.
'''
'''
Start by creating a basic CLI structure to handle user inputs.
Implement each feature one by one, ensuring to test thoroughly before moving to the next e.g. implement adding task functionality first, listing next, then updating, marking as in progress, etc.
Testing and Debugging
Test each feature individually to ensure they work as expected. Look at the JSON file to verify that the tasks are being stored correctly.
Debug any issues that arise during development.
Finalizing the Project
Ensure all features are implemented and tested.
Clean up your code and add comments where necessary.
Write a good readme file on how to use your Task Tracker CLI.
'''
import sys
def main():
    print("Welcome to Task Tracker!!!")
    arg = sys.argv[1]
    if arg.startswith("mark-"):
        mark_task(arg.replace("mark-", ""),sys.argv[2])
    else:    
        match arg:
            case "add":
                add_task(sys.argv[2])
            case "update":
                update_task(sys.argv[2],sys.argv[3])
            case "list":
                if(len(sys.argv)>2):
                    display_status(sys.argv[2])
                else:
                    display()
            case "delete":
                delete_task(sys.argv[2])
            case _:
                print("The given argument(s) isn't supported.")
main()