# 1) Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("hello_" + user_name + "!")



# 2) Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for i in range(1, 101, 2):
        print(i)



# 3)Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    if not a_list:
        return None  

    max_num = a_list[0]  

    for num in a_list:
        if num > max_num:
            max_num = num

    return max_num



# 4) Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    # Check if the year is divisible by 4 but not by 100, or if it's divisible by 400
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False



# 5) Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    if len(a_list) < 2:
        return True  # A list with 0 or 1 elements is considered consecutive

    # Check if the difference between each element and the next is consistently 1
    for i in range(len(a_list) - 1):
        if a_list[i + 1] - a_list[i] != 1:
            return False

    return True



