"""
Project management program

Estimate time for completion: 10 hours.
Actual time:
"""

from project import Project
from datetime import datetime

FILENAME = 'projects.txt'
MENU = """
- (L)oad projects\n- (S)ave projects\n- (D)isplay projects \n- (F)ilter projects by date 
- (A)dd new project \n- (U)pdate project \n- (Q)uit
"""


def main():
    projects = []

    # TODO Menu
    print("Welcome to Pythonic Project Management")
    # Display loaded objects summary
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            choose_filename = input("Choose a file to load project from: ")
            projects = load_projects(choose_filename)
            display_projects(projects)
        elif choice == 'S':
            save_projects(FILENAME, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    projects = []
    # TODO error checking
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
            start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion = float(completion)
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)

    return projects


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    completed_projects = [project for project in projects if project.completion == 100]
    projects.sort()
    print('Completed projects:')
    for project in completed_projects:
        print(project)


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_to_update = int(input("Project choice: "))
    project = projects[project_to_update]
    print(project)
    new_completion = float(input("New Percentage: "))
    project.completion = new_completion
    new_priority = int(input("New Priority: "))
    project.priority = new_priority


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = float(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)
    projects.sort()


def filter_projects_by_date(projects):
    """Filter projects by user specified date."""
    start_date = input("Show projects that start after date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()

    filtered_projects = [project for project in projects if project.start_date > start_date]

    for projects in filtered_projects:
        print(projects)


def save_projects(filename, projects):
    """Save projects to file, writing over previous file contents."""
    save_to_file = input(f"Would you like to save to {filename}? yes or no: ").lower()
    project = projects
    if save_to_file == "yes":
        with open(filename, 'w') as outfile:
            outfile.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
            for project in projects:
                line = (f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                        f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion:.2f}\n")
                outfile.write(line)
        print("Thank you for using custom-built project management software.")
    else:
        print("Thank you for using custom-built project management software.")


main()
