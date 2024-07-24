"""
Project management program

Estimate time for completion: 10 hours.
Actual time:
"""

# Imports:
from project import Project

# from datetime import datetime

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
            pass
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            pass
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            pass
        elif choice == 'Q':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    pass


def load_projects(filename):
    projects = []
    # TODO error checking
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
            start_date = "22,33,24"  # TODO update using datetime module later
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion = float(completion)
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)

    return projects


def display_projects(projects):  # not yet sorting by priority

    incomplete_projects = [project for project in projects if project.completion < 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    completed_projects = [project for project in projects if project.completion == 100]

    print('Completed projects:')
    for project in completed_projects:
        print(project)


def update_project():
    # Choose a project, then modify the completion % and/or priority - leave blank to retain existing values
    # TODO enumerate (start 0), name, start date, priority, estimate, completion %,
    #  add new completion %, add new priority (by number).
    # See sample output.
    pass


def add_new_project(projects):
    # TODO sort by priority
    name = input("Name: ")
    start_date = int(input("Start date (dd/mm/yy): "))
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = float(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)


def filter_projects_by_date():
    # TODO show projects after (x date),
    # TODO display name, start date, priority, estimate cost, completion percentage %
    # See sample output.
    pass


def save_projects():
    # TODO Prompt the user for a filename to save projects to and save them
    #
    pass


main()
