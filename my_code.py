# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# none

def avg(user_list):
    average = sum(user_list) / len(user_list)
    return average


if __name__ == '__main__':
    # test your fucntion with this print statement before writing the input loop
    # print(avg([1, 4, 8]))    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    user_list = [] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
    number_of_numbers = int(input("Enter how many numbers you want to take the average of: "))
    times = 1

    while number_of_numbers >= times:
        x = int(input("Enter a number: "))
        user_list.append(x)
        times = times + 1

    print(avg(user_list))
