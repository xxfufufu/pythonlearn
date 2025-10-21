import sys

tasks = []

def show_help():
    print("""
Simple Todo CLI
Commands:
  add <task>      Add a new task
  list            Show all tasks
  done <index>    Mark a task as done
  helpme          Show this help message
  exit            Exit the app
""")
    
def add(task):
    tasks.append({"task": task, "is_done": False})
    
def list():
    if not tasks:
        print("no task")
        return
    for i, task in enumerate(tasks,1):
        status = "✅" if task["is_done"] else  "❌"
        print(f"{i}. {task['task']} {status}")

def mark_done(index):
    try:
        tasks[index -1]["is_done"] = True
        print("great!!!")
    except:
        print("invalid number task")
    
def main():
    show_help()
    while True:
        command = input(">> ").strip().split(" ", 1)
        cmd = command[0]
        
        if cmd == "add" and len(command) > 1:
            add(command[1])
        elif cmd == "list":
            list()
        elif cmd == "done" and len(command) > 1:
            mark_done(int(command[1]))
        elif cmd == "exit":
            print("Goodbye 👋")
            sys.exit()
        elif cmd == "help":
            show_help()
        else:
            print("Unknown command. Type 'help' for options.")
        


if __name__ == "__main__":
    main()
    