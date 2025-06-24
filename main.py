from utils import add_task, view_task, remove_task, load_tasks, get_task_details, completed

def main():
    while True:
        option = input(f"PLEASE SELECT AN PROPER OPTION : \n 1) LOAD TASKS \n 2) ADD TASK \n 3) VIEW TASK \n 4 ) REMOVE TASK \n TYPE 0 TO EXIT \nENTER YOUR CHOICE : ")

        match option:
            case "1":
                print("LAOD Task selected.")
                
                data = load_tasks()

                break
            case "2":
                print("ADD Task selected.")

                name, title, desc, duration = get_task_details()
                add_task(name, title,  desc, duration)

                break
            case "3":
                print("VIEW Task selected.")

                key = input("ENTER THE TASK TITLE TO KNOW THE DETAILS : ")
                data = view_task(key)

                break
            case "4":
                print("REMOVE TASK SELECTED")

                key = input("ENTER THE TASK TITLE TO REMOVE IT : ")
                data = remove_task(key)
                print(data)

                break

            case "0":
                print("Exiting program ............")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()