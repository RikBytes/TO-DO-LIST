from utils import add_task, view_task, remove_task, load_tasks, get_task_details, completed, isCompleted, filter_task

def main():
    while True:
        option = input(f"PLEASE SELECT AN PROPER OPTION : \n 1) LOAD TASKS \n 2) ADD TASK \n 3) VIEW TASK \n 4) REMOVE TASK \n 5) COMPLETE TASK \n 6) FILTER TASK \nTYPE 0 TO EXIT \nENTER YOUR CHOICE : ")

        match option:
            case "1":
                print("LAOD Task selected.")
                
                data = load_tasks()

                break
            case "2":
                print("ADD Task selected.")

                name, title, desc = get_task_details()
                add_task(name, title,  desc)

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

            case "5":
                print("COMPLETE TASK SELECTED")

                name, value, isQuit = isCompleted()

                if isQuit:
                    break
                else:
                    message = completed(name)
                    if message == None:
                        print("no data found")
                    else:
                        print(message)
                    break
            case "6":
                print("FILTER TASK SELECTED")
                print(f"-------------------")
                filter_key = input("ENTER THE NAME OF THE KEY : ")
                filter_value = input("ENTER THE NAME OF THE VALUE : ")
                print(f"-------------------\n")
                message = filter_task(filter_key, filter_value)
                print(message)
                break
            case "0":
                print("Exiting program ............")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()