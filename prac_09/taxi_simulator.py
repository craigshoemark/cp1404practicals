"""
Taxi Simulator
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit c)hoose taxi d)rive"""


def main():
    """Get taxi, choose distance, display cost, display accumulative cost"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    total_fares = 0
    taxi_choice = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            taxi_choice = choose_taxi(taxis, total_fares)
        elif choice == "d":
            drive(taxi_choice, total_fares)
            total_fares += taxi_choice.get_fare()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} {taxi}")


def choose_taxi(taxis, total_fares):
    """Choose a taxi to drive."""
    taxi_choice = 0
    print("Taxis available:")
    print("Bill to date", f"${total_fares:.2f}")
    for index, taxi in enumerate(taxis):
        print(f"{index} {taxi}")
    is_valid_input = False
    while not is_valid_input:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0 or taxi_choice > len(taxis):
                print("Invalid choice")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input (not an integer)")
    return taxis[taxi_choice]


def drive(taxi_choice, total_fares):
    """Drive taxi of choice."""
    distance = float(input("Drive how far? "))
    taxi_choice.start_fare()
    taxi_choice.drive(distance)
    total_fares += taxi_choice.get_fare()

    print(f"Your {taxi_choice.name} trip cost you $ {taxi_choice.get_fare():.2f}")
    return total_fares


main()
