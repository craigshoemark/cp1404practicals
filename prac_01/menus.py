# Menus
"""
MENU = (H)ello (G)oodbye (Q)uit

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = """(H)ello\n(G)oodbye\n(Q)uit"""
name = input("Enter name: ")
print(MENU)
choice = input(">>> ")
while choice.upper() != "Q":
    if choice.upper() == "H":
        print(f"Hello {name}")
    elif choice.upper() == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Finished.")
