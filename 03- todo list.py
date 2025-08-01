# Simple To-Do List App

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({'task': task, 'done': False})
    print("✅ Task added.")

def view_tasks():
    if not tasks:
        print("📝 No tasks found.")
        return
    for idx, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "❌"
        print(f"{idx}. {t['task']} [{status}]")

def mark_complete():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("🎉 Task marked as complete.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ Deleted task: {deleted['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option. Please choose 1-5.")
