# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


test ="Hello Potato"
print("------------------STRINGS------------------------")

print(test.upper().isupper())
print(len(test))
print(test[0])

print(test.index("Potato"))
print(test.replace("Potato","World" ))
print("////////////////////////////////////Lists And Tuples////////////////////////////////////")
Tuple = (4, 9)
list = [55, 54]
print("lists "+ str(list))
print("and Tuples " + str(Tuple))


print("The differance between a Tuple and a list is Tuples can't be changed")
print("for instance a Tuple like " + str(Tuple[0:]) + " can only ever be " + str(Tuple[0:]))
print("whereas a list like " + str(list) +" can become ")
list = [24,48]
print(list)
print("get it?")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
