# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:10:29 2023

@author: Mst Abida Sultana
"""

#Import section
from datetime import date
#from employee import Employee
import random
import json

#Flower Box Section
###################################
#   Name : Mst Abida Sultana 
#   Email: msultana1@lamar.edu
#   ID   : L20572135
#   Date : 24-Sep-2023
#
#
###################################

#Variables section

#Empty variable declaration for use later in program
first_name = "" 
last_name = "" 
year_born = "" 
password_length = ""   
is_this_correct = "" 
all_employee_data_in_tuples_list = []  
username_list = [] 
username_sorted_list = [] 
employee_data_dictionary = {} 
#employee_greeting_and_age_list = []  
#employee_greeting_age_list = [] 
#greeting = ""   
#age = 0  
#Yes_list to make verification easier
yes_list = ["Yes", "YES", "Y", "yes", "y"] 
#New variable
error_message = ""

#Functions section

def build_username(first, last, year, dup):      
    """function to construct username dependent on dup check""" 
    if (not dup):                                
        username = first[0].lower() + last.lower() + year[-2:]
    else: 
        username = first.lower() + last[0:1].lower() + year[-2:]
    
    return username

def build_password(password_length_int, use_special_characters, use_numbers):
    ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    SPECIAL_CHARACTERS = "!@#$%^&*"
    NUMBERS = "0123456789"
    count = 0
    password = ""
    
    while count < password_length_int:
        randomNumber = random.randrange(0,51,1)
        pwChar = ALPHABET[randomNumber]
        password = password + pwChar
        pwChar = ""
        count = count + 1
        
        if use_special_characters and count < password_length_int:
            randomNumber = random.randrange(0,7,1)
            pwChar = SPECIAL_CHARACTERS[randomNumber]
            password = password + pwChar
            pwChar = ""
            count = count + 1
            
        if use_numbers and count < password_length_int:
            randomNumber = random.randrange(0,9,1)
            pwChar = NUMBERS[randomNumber]
            password = password + pwChar
            pwChar = ""
            count = count + 1
            
    return password


#Input section

#Read in dictionary stored in text file
try:
    with open("employee_data.txt", "r", encoding="utf-8") as file:
        for line in file:
            temp_dict = str(line)
            temp_dict = temp_dict.strip()
            temp_dict = temp_dict.replace("\'", "\"")
            employee_data_dictionary = json.loads(temp_dict)
except FileNotFoundError:
    print("Sorry, file not found")
else:
    file.close()
    
#Displays a message and ask for user input for x number of employees
print("Enter the information below to create a username for the network.")
while len(all_employee_data_in_tuples_list) < 3:                   # Using while loops until x number of employee data records are entered      
    while len(first_name) < 2:
        first_name = input("Enter your first name: ")

    while len(last_name) < 2:
        last_name = input("Enter your last name: ")

    while len(year_born) < 4:
        year_born =input("Enter the full year you were born: ") #This sets the year born variable to what the user enters as an employee year of birth 
        
    while True:  # using while
        password_length = input("Enter a number between 6 and 10 or 16 ") 
        try:
            password_length_int = int(password_length)  
            if(6 <= password_length_int <= 10 or password_length_int == 16):  # using if to get the password length between 10 and 17
                break 
            else:
                continue 
        except:
            continue 
    
    special_number_answer = input("Would you like special characters in your password? ")  # taking the input from user
    
    if special_number_answer in yes_list:   # checking if the input is in yes list
        use_special_characters = True 
        
    else:
        use_special_characters = False
    
    special_number_answer = input("Would you like numbers in your password? ") # taking the input from user

    if special_number_answer in yes_list:       # checking if the input is in yes list
        use_numbers = True 
    else:
        use_numbers = False
    
    print("You entered " + first_name + " " + last_name + " " + year_born + "Password length " + str(password_length) + " with Special Characters " + str(use_special_characters) + " with Numbers " + str(use_numbers) + "is this correct? ") 
    
    is_this_correct = input("Yes or No: ") # asking if previous printed statement is true or false

    if(is_this_correct in yes_list): # using if to check if the user input in yes list
        employee_data = (first_name, last_name, year_born, password_length_int, password_length, use_special_characters, use_numbers) #creating tuples 
        all_employee_data_in_tuples_list.append(employee_data) # clear followings for next iteration
        first_name = "" 
        last_name = "" 
        year_born = "" 
        password_length = "" 
        use_special_characters = False 
        use_numbers = False 
    else:
        #clear variable and start data enter over
        first_name = "" 
        last_name = "" 
        year_born = "" 
        password_length = "" 
        use_special_characters = False 
        use_numbers = False 
        continue 


#Processing section

for employee in all_employee_data_in_tuples_list:
    employee_first_name = employee[0]            #declare and assign first name
    employee_last_name = employee[1]            #declare and assign first name
    employee_year_born = employee[2] 
    password_len_int = employee[3]
    special_characters_in_password = employee[4]
    numbers_in_password = employee[5]        #declare and assign first name
    dup_found = False
   
    #pass first name, last name, birth year and dup flag to build username function
    #set usernsme to retrun value fo function call
    username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) 
    
    #test username against current list
    #find dup call build suername function again dup flag true
    if username in username_list: 
        dup_found = True 
        username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) 
       
    
    username_list.append(username) # update username list with new user 
    
    #call build password function in class for password
    #my_employee = Employee(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]) 
    password = build_password(password_len_int,special_characters_in_password,numbers_in_password) 
    
    #temp_tuple = (my_employee.greet_person(), my_employee.age())
    #employee_greeting_age_list.append(temp_tuple) 
    
    #build an employee record via list then add record to the employee dictionary
    employee_record = [employee_first_name, employee_last_name, employee_year_born, password]
    employee_data_dictionary[username] = employee_record 
 
username_sorted_list = list(username_list)   # create a copy of the username list 
username_sorted_list.sort() #  sorting the copy

#write employee data dictionary to the employee_data.txt file
try:
    with open("employee_data.txt", "w") as file:
        file.write(str(employee_data_dictionary))
except FileNotFoundError:
    print("Sorry, file not found")
else:
    file.close()

#Output section

print(username)      # this display your os username
today = date.today()
print("Today's Date is: ", today)              # Displays the current system date


#for employee_greeting_age in employee_greeting_and_age_list:
    #greet = employee_greeting_age[0]    #display massage from class function call
    #age = employee_greeting_age[1] 
    #print(greeting + "You are " + str(age))

print(all_employee_data_in_tuples_list)    #display the list of employee tuples
print(username_list)              #display the list of usernames 
print(employee_data_dictionary)      #display the employee data dictionary 
print(username_sorted_list)     #display sorted list

