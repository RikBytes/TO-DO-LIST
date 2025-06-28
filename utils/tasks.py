import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv("FILE_PATH") # PUT THE JSON FILE PATH HERE

def read_data():
    if not os.path.exists(FILE_PATH):
        sample_data = {"tasks": {}}
        try:
            with open(FILE_PATH, "w") as f:
                json.dump(sample_data, f, indent=4)
            return sample_data
        except Exception as e:
            print(f"❌ Failed to create new file: {e}")
            return None

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        print("❌ Failed to decode JSON. The file might be corrupted.")
        decision = input("🔧 Do you want to reset the file? Type 'yes' to reset, anything else to abort: ").strip().lower()
        if decision == "yes":
            sample_data = {"tasks": {}}
            try:
                with open(FILE_PATH, "w") as f:
                    json.dump(sample_data, f, indent=4)
                print("✅ File reset successfully.")
                return sample_data
            except Exception as e:
                print(f"❌ Failed to reset the file: {e}")
                return None
        else:
            print("🚫 Operation aborted.")
            return None

    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None



def write_data(data):
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Failed to write to file: {e}")

def add_task(name , title , desc, duration):

        data = read_data()

        if name in data["tasks"]:
                print("task name already exist")
                return
        
        data["tasks"][name] = {
            "title" : title,
            "description" : desc,
            "duration" : duration,
            "completed": False
        }
        write_data(data)
        return print("TASK ADDED SUCCESSFULLY")

def view_task(name : str):
        data = read_data()
        task = data["tasks"][name]
        output = print(f'TITLE : {task["title"]} \nDescription : {task["description"]} \nDuration : {task["duration"]}\nCompleted : {task["completed"]}')
        return output

def remove_task(name):
            data = read_data()

            if name in data["tasks"]:
                del data["tasks"][name]
                write_data(data)
                return f"✅ Removed task: '{name}' successfully."
            else:
                return f"❌ Task '{name}' not found."


def completed(name : str):
         data = read_data()

         if name in data["tasks"]:
            data["tasks"][name]["completed"] = True
            write_data(data)
            return f"TASK MARKED COMPLETED"
         else:
            print(f"Task '{name}' not found.")

def load_tasks():
        data = read_data()

        task_count = len(data["tasks"])
        
        print(f"\n📋 Total Tasks: {task_count}\n")
        print("📝 AVAILABLE TASKS ARE:")

        for task_name in data["tasks"]:
            print(f" - {task_name}")