# the list
tasks = []
# the intro/ welcome txt and getting usr input
print("Welcome to your to-do planner")
choice = input("type add or show ")

# functions


def show():
    print("Here are your tasks:")
    for e in tasks:
        print(": " + e)


def ext():
    print("Here are your tasks for today Good Luck! :D")
    for e in tasks:
        print(": " + e)

# loops


while choice.casefold() == "show":
    show()
    nw_tsk = input("Would you like to add a task? (y / n ) :")
    if nw_tsk.casefold() == 'y':
        choice = "add"
    if nw_tsk.casefold() == 'exit':
        ext()
        break
while choice.casefold() == "add":
    task = input("add a task ")
    tasks.append(task)
    show()
    nw_tsk = input("another? (y / n ) type 'exit' to leave: ")
    if nw_tsk.casefold() == 'n':
        show()
        nw_tsk = input("would you like to add a task? (y / n ) type 'exit' to leave: ")
    if nw_tsk.casefold() == 'exit':
        ext()
        break

        # casefold converts to lower case
