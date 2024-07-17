"""
Project management program

Estimate time for completion: 10 hours.
Actual time:
"""


# Imports:
# Class
# Datetime

# CONSTANTS:
# FILENAME = projects.txt
MENU = """
(L)oad projects\n(S)ave projects\n(D)isplay projects \n(F)ilter projects by date 
(A)dd new project \n(U)pdate project \n(Q)uit
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
            pass
        elif choice == 'S':
            pass
        elif choice == 'D':
            pass
        elif choice == 'F':
            pass
        elif choice == 'A':
            pass
        elif choice == 'U':
            pass
        elif choice == 'Q':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    pass


def load_projects():
    # TODO Prompt the user for a filename to load projects from and load them
    # Load from file projects.txt
    # Projects will be objects
    pass


def display_projects():
    # TODO Display two groups: incomplete projects; completed projects, both sorted by priority

    # TODO Incomplete projects: own function ?
    # Display incomplete projects, name, date, priority(sort by), estimate, completion percentage.
    # See sample output.
    # TODO Completed projects: own function ?
    # Display incomplete projects, name, date, priority, estimate, completion percentage.
    # See sample output.
    pass


def update_project():
    # Choose a project, then modify the completion % and/or priority - leave blank to retain existing values
    # TODO enumerate (start 0), name, start date, priority, estimate, completion %,
    #  add new completion %, add new priority (by number).
    # See sample output.
    pass


def add_new_project():
    # Ask the user for the inputs and add a new project to memory
    # TODO add project name, start date, priority, cost estimate, percent completed
    # See sample output.
    pass


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
