import json
from datetime import datetime
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


def add_task(name , title , desc):
        data = read_data()
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")

        start_time = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")

        if name in data["tasks"]:
                print("task name already exist")
                return
        
        data["tasks"][name] = {
            "title" : title,
            "description" : desc,
            "duration" : None,
            "status": "pending",
            "start time": f"{start_time}"
        }
        write_data(data)
        return print("TASK ADDED SUCCESSFULLY")


def view_task(name : str):
        data = read_data()
        task = data["tasks"][name]
        strt_time = task["start time"]
        strt_time_str = datetime.strptime(strt_time, "%Y-%m-%d %H:%M:%S")
        friendly_time = strt_time_str.strftime("%B %d, %Y at %I:%M %p").lstrip("0")

        output = print(f'TITLE : {task["title"]} \nDescription : {task["description"]} \nDuration : {task["duration"]}\nStatus : {task["status"]}\nStarted at : {friendly_time}')
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
        end_time = datetime.now()


        if name in data["tasks"]:
            # Convert start time from string to datetime
            start_time_str = data["tasks"][name]["start time"]
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")

            # Calculate time difference
            time_diff = end_time - start_time
            total_seconds = int(time_diff.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

            # Optional: friendly duration string
            parts = []
            if hours:
                parts.append(f"{hours} hour(s)")
            if minutes:
                parts.append(f"{minutes} minute(s)")
            if seconds or not parts:
                parts.append(f"{seconds} second(s)")
            friendly_duration = " ".join(parts)
            
            data["tasks"][name]["status"] = "completed"
            data["tasks"][name]["duration"] = f"{friendly_duration}"
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

def filter_task(filter_key, filter_value):
    data = read_data()
    tasks = data["tasks"]
    result = ""
    for k, v in tasks.items():
        if v.get(filter_key) == filter_value:
            result += f"🆔 {k}\n"
            result += f"📌 Title : {v.get('title')}\n"
            result += f"📝 Desc  : {v.get('description')}\n"
            result += f"📂 Status: {v.get('status')}\n"
            result += "-------------------------\n"
    
    return result if result else "❌ No tasks found."

def list_tasks():
    data = read_data()
    if data:
        tasks = data["tasks"]
        message = ""
        if not tasks:
            return f"No Tasks Available to display"
        else:
            message += f"🧾 The tasks are :\n"
            message += f"------------------"
            for k, v in tasks.items():
                message += f"\n📌{k}"
            message += f"\n------------------"
    else:
         return f"no data found"
    return message