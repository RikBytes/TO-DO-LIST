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