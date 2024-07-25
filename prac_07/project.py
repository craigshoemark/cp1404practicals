"""Project Class."""


# def sort_by_priority(projects):
#     projects.sort()


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """classProject instance variables."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Display string values."""
        # TODO - will be int and float values here..
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def __repr__(self):
        """Display representation."""
        # TODO - will be int and float values here..
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate{self.cost_estimate:.2f}, completion: {self.completion}")

    def __lt__(self, other):
        """Determine project priority."""
        return self.priority < other.priority
