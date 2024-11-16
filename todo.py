import os
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST", "10.160.11.32"),
            user=os.getenv("DATABASE_USER", "todo_user"),
            password=os.getenv("DATABASE_PASSWORD", "todo_password"),
            database=os.getenv("DATABASE_NAME", "tasks_db")
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def load_tasks():
    connection = create_connection()
    tasks = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
        except Error as e:
            print(f"Error loading tasks: {e}")
        finally:
            connection.close()
    return tasks

def save_task(title):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
            connection.commit()
            print(f"Task '{title}' added successfully!")
        except Error as e:
            print(f"Error saving task: {e}")
        finally:
            connection.close()

def mark_task_as_done(task_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (>
            connection.commit()
            print(f"Task {task_id} marked as completed!")
        except Error as e:
            print(f"Error updating task: {e}")
        finally:
            connection.close()

def delete_task(task_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            connection.commit()
            print(f"Task {task_id} deleted successfully!")

            cursor.execute("SET @row_number = 0;")
            connection.commit()
            cursor.execute("UPDATE tasks SET id = (@row_number := @row_number +>
            connection.commit()

            cursor.execute("SELECT MAX(id) FROM tasks;")
            max_id = cursor.fetchone()[0] or 0
            cursor.execute(f"ALTER TABLE tasks AUTO_INCREMENT = {max_id + 1};")

            connection.commit()

        except Error as e:
            print(f"Error deleting task: {e}")
        finally:
            cursor.close()
            connection.close()

def main():
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("\nEnter the task: ")
            save_task(task)

        elif choice == '2':
            print("\nTasks:")
            tasks = load_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "Done" if task["completed"] else "Not Done"
                    print(f"{task['id']}. {task['title']} - {status}")

        elif choice == '3':
            try:
                task_id = int(input("Enter the task ID to mark as done: "))
                mark_task_as_done(task_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid task ID.")



        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid task ID.")

        elif choice == '5':
            print("\nExiting the To-Do List.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()


