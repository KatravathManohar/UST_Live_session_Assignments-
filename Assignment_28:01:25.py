"""

1.use the os and os.path modules to list the contents of your downloads folder
and indicate for each item whether it's a file or a folder (hint : use os.path.join)


2.import  string module and print out all  ASCII letters defined in this module

3.Import the sample() function from the random module and the ascii_letters attribute
of the string module. use these to randomly sample five letters and assign these to a
variable called five_letters

4.Take a input from the user a date for eg: 25/02/2020
    a.print output Date in format  Tuesday 25 February 2020
    b.print the day of the week of a given input  date
    c. Add 15 days and 23 hours to a given input date
    d. calculate the date 6 months from the current date


5.Create a game of rock paper and scissors where user will input one option
while second option is chosen by the computer(i.e your python program). Based
on the options select declare the result
1. user wins
2. computer wins
3. draw
 if it is draw continue the game till one of them gets won

"""

"""import os

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

for item in os.listdir(downloads_path):
    full_path = os.path.join(downloads_path, item)
    if os.path.isfile(full_path):
        print(f"{item} - File")
    else:
        print(f"{item} - Folder")







import string

print("All ASCII letters:", string.ascii_letters)
print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)


from random import sample
from string import ascii_letters

five_letters = sample(ascii_letters, 5)
print("Five random letters:", five_letters)

five_letters_string = ''.join(five_letters)
print("As a string:", five_letters_string)



from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


date_str = input("Enter date (DD/MM/YYYY): ")

date_obj = datetime.strptime(date_str, "%d/%m/%Y")

# a.formatted date
formatted_date = date_obj.strftime("%A %d %B %Y")
print("Formatted date:", formatted_date)

# b.day
day_of_week = date_obj.strftime("%A")
print("Day of week:", day_of_week)

# c.Adding 15 days and 23 hours
new_date = date_obj + timedelta(days=15, hours=23)
print("Date after adding 15 days and 23 hours:", new_date)

# d.Adding 6 months to current date
current_date = datetime.now()
six_months_later = current_date + relativedelta(months=6)
print("Date 6 months from now:", six_months_later.strftime("%d %B %Y"))"""

import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    
    while True:
        
        user_choice = input("Enter User choice (rock/paper/scissors): ").lower()
        while user_choice not in options:
            print("Invalid choice! Please try again.")
            user_choice = input("Enter user choice (rock/paper/scissors): ").lower()
        
        
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a draw!.")
            continue
            
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("User wins!")
            break
            
        else:
            print("Computer wins!")
            break
play_game()
















