def get_task_details():
    name = input("👤 Enter your task name        : ").strip()
    title = input("📌 Enter task title       : ").strip()
    desc = input("🧾 Enter task description : ").strip()
    
    duration_input = input("⏳ Enter duration (mins)  : ").strip()
    
    if duration_input.isdigit() and int(duration_input) > 0:
        duration = int(duration_input)
    else:
        duration = None


    return name, title, desc, duration

def isCompleted():
    name = input("👤 Enter your task name : ").strip()
    value = input("DO YOU WANT TO MARK THIS TASK AS COMPLETED ? THEN ENTER 1 OR TYPE 0 TO CANCEL : ")

    if value == "1":
        return name, True, False
    elif value == "0":
        print(f"YOU CANCELED THE TASK , Exiting program......")
        return None, False, True
    else:
        print(f"Invalid Input , Exiting program......")
        return None, None, True