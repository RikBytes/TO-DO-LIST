import json
import datetime


def add_task(name , title , desc, duration):
    with open("D:/Users/panda/Documents/2K25/TO-DO LIST/todos.json", "r+") as f:
        data = json.load(f)

        if name in data["tasks"]:
                print("task name already exist")
                return
        
        data["tasks"][name] = {
            "title" : title,
            "description" : desc,
            "duration" : duration
        }
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        return print("TASK ADDED SUCCESSFULLY")

def view_task(name : str):
    with open("D:/Users/panda/Documents/2K25/TO-DO LIST/todos.json","r") as f:
        data = json.load(f)
        task = data["tasks"][name]
        output = print(f'TITLE : {task["title"]} \nDescription : {task["description"]} \nDuration : {task["duration"]}')
        return output

def remove_task(name):
        with open("D:/Users/panda/Documents/2K25/TO-DO LIST/todos.json","r+") as f:
            data = json.load(f)

            if name in data["tasks"]:
                del data["tasks"][name]
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                return f"Removed task: {name} successfully"
            else:
                return f"Task '{name}' not found."

def completed():
    pass

def load_tasks():
    with open("D:/Users/panda/Documents/2K25/TO-DO LIST/todos.json","r") as f:
        data = json.load(f)
        task_count = len(data["tasks"])
        
        print(f"\n📋 Total Tasks: {task_count}\n")

        for task_name in data["tasks"]:
            print(f"AVAILABLE TASKS ARE : \n {task_name}")