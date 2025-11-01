import argparse, json, os, sys, shlex, time, calendar
from datetime import datetime


DATA_FILE = "store.json"
data_map = {} #chache memory

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(desc, amount,category):
    data = load_data()
    if amount < 0:
        print("Positive amount required")
        return
    temp = {
            "description": desc, 
            "amount": amount,
            "category": category,
            "created_at":  time.strftime("%Y-%m-%d", time.gmtime(time.time()))
            }
    temp["id"] = max([d["id"] for d in data],default=0)+1
    data.append(temp)
    save_data(data)
    print(f"Expense added successfully (ID: {temp['id']})")

def update(id, newData):
    data = load_data()
    updated = False
    for (d) in data:
         if isinstance(d, dict) and d.get("id") == id: 
            d.update(newData)
            updated = True
            break
    if not updated:
        print(f"Expense not found")
        return
    save_data(data)
    print(f"Expense updated successfully (ID: {id})")

def summary(month= None):
    data = load_data()
    if month is not None:
        total_amount = sum(d.get("amount", 0)
                            for d in data 
                            if d.get("created_at") and datetime.strptime(d.get("created_at"), "%Y-%m-%d").month  == month)
        print(f"Total expenses for {calendar.month_name[month]}: ${total_amount}")
        return
    else:
        total_amount = sum(d["amount"] for d in data)
        print(f"Total expenses: ${total_amount}")

def show_list():
    data = load_data()
    if len(data) == 0:
        print("no data")
        return
    print(f"{'ID':<3} {'Date':<12} {'Description':<12} {'Amount':<6} {'Category':<6}")
    for d in data:
        category = d.get("category") or "null"
        print(f"{d['id']:<3} {d['created_at']:<12} {d['description']:<12} ${d['amount']:<6}{category:<6}")

def remove(target_id: int):
    data = load_data()
    deleted = False
    for i, d in enumerate(data):
        if d["id"] == target_id:
            del data[i]
            deleted = True
            break
    if not deleted:
        print(f"Expense not found")
        return
    save_data(data)
    print(f"Expense deleted successfully (ID: {target_id})")
    

def build_parser():
    parser = argparse.ArgumentParser(description="Simple To-Do CLI App")
    subparsers = parser.add_subparsers(dest="action")

    add_expenses = subparsers.add_parser("add", help="Add a new expense")
    add_expenses.add_argument("--desc", required=True)
    add_expenses.add_argument("--amount", type=int, default=1)
    add_expenses.add_argument("--category", type=str)
    
    update_expenses = subparsers.add_parser("update", help="Update a expense")
    update_expenses.add_argument("--desc")
    update_expenses.add_argument("--amount", type=int)
    update_expenses.add_argument("--category", type=str)
    update_expenses.add_argument("--id", required=True, type=int)

    summary_expenses =subparsers.add_parser("summary", help="Total expense")
    summary_expenses.add_argument("--month", required=False, type=int)
    
    subparsers.add_parser("list", help="Show list")
    
    delete_expenses =subparsers.add_parser("delete", help="Delete a expense")
    delete_expenses.add_argument("--id", required=True, type=int)

    return parser

def main():
    parser = build_parser()

    print("Welcome to To-Do CLI!")
    while True:
        user_input = input(">> expenses-tracker ").strip()
    
        if user_input == "exit":
            print("Goodbye 👋")
            sys.exit()
            break
        elif user_input.lower() == "help":
            parser.print_help()
            continue
        
        try:
            args = parser.parse_args(shlex.split(user_input))
        except:
            print("Invalid input. Type 'help' for options.")
            continue
    
        if args.action == "add":
            add(args.desc, args.amount, args.category)
        elif args.action == "update":
            update_data = {}
            for k, v in vars(args).items():
                if v is not None and k != "id" and k != "action":
                    if k == "desc":
                        update_data["description"] = v
                    else:
                        update_data[k] = v
            update(args.id, update_data)
        elif args.action == "list":
            show_list()
        elif args.action == "summary":
            summary(args.month)
        elif args.action == "delete":
            remove(args.id)
        else:
            print("Unknown command. Type 'help' for options.")

        
       
        

if __name__ == "__main__":
      main()