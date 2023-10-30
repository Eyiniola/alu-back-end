#!/usr/bin/python3
import requests

# Define the base URL of the REST API
base_url = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    '''
    Get and display an employee's TODO list progress based on their employee ID.

    Args:
        employee_id (int): The employee's ID for whom to retrieve the progress.

    Returns:
        None
    '''
    try:
        ''' Fetch user information'''
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()

        ''' Check if "name" exists in the user data '''
        if "name" in user_data:
            employee_name = user_data["name"]
        else:
            employee_name = "Unknown"

        ''' Fetch TODO list for the employee '''
        todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todo_data = todo_response.json()

        ''' Calculate progress'''
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        ''' Display the progress'''
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

