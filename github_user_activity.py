import sys
import urllib.request
import json



def show_help():
    print("""
Simple Todo CLI
Commands:
  github-activity <username>      Show github username activity
  helpme                          Show this help message
  exit                            Exit the app
""")
    
def get_activity(username):
    print("please wait....")
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            
            data = json.load(response)
            print(data)
            
            for item in data:
                event_type = item["type"]
                repo_name = item["repo"]["name"]

                if event_type == "CreateEvent":
                    ref_type = item["payload"].get("ref_type", "")
                    ref = item["payload"].get("ref", "")
                    if ref:
                        print(f"- Created {ref_type} {ref} in {repo_name}")
                    else:
                        print(f"- Created new {ref_type} in {repo_name}")

                elif event_type == "PushEvent":
                    print(f"- Pushed commits to {repo_name}")

                elif event_type == "IssuesEvent":
                    action = item["payload"].get("action", "")
                    print(f"- {action.capitalize()} issue in {repo_name}")

                elif event_type == "WatchEvent":
                    print(f"- Starred {repo_name}")

                else:
                    print(f"- {event_type} in {repo_name}")
    except Exception as e:
        print(f"Error fetching data: {e}")
def main():
    show_help()
    while True:
        command = input(">> ").strip().split(" ", 1)
        cmd = command[0]
        if cmd == "github-activity" and len(command) >1:
            get_activity(command[1])
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            print("Goodbye 👋")
            sys.exit()
        else:
            print("Unknown command. Type 'help' for options.")
    

if __name__ == "__main__":
    main()