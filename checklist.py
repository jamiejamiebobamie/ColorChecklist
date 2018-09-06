"""In our case our user stories will look something like this:

As a user, I want to be able to create, read, update, and destroy items in a checklist.

As a user, I want to be able to mark off colors so I can know that it's already represented.

As a user, I want to be able to see everything in my list at once so I know what is in my list.

So from our user stories we can generate a list of important features and functionalities that our users will expect from our application."""



#create, read, update, and destroy

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

"""def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
# Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run"""

#test()

running = True
while running:
    selection = input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
