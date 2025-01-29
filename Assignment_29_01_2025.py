"""
Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

Exercise 3: Generate 6 digit random secure OTP

Exercise 4: Pick a random character from a given String

Exercise 5: Generate random String of length 5

Exercise 6: Generate a random Password which meets the following conditions Password length must be 10 characters long. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

Exercise 7: Calculate multiplication of two random float numbers

Exercise 8: Generate random secure token of 64 bytes and random URL

Exercise 9: Roll dice in such a way that every time you get the same number

Exercise 10: Generate a random date between given start and end dates   """

1.
import random

def generate_divisible_by_5():
    divisible_numbers = []
    
    for _ in range(3):
        number = random.randrange(100, 999, 5)
        divisible_numbers.append(number)
    
    return divisible_numbers

result = generate_divisible_by_5()
print("3 Random numbers divisible by 5:", result)


2.
import random

def lottery_tickets():
 
    tickets = random.sample(range(1000000, 9999999), 100)
    winners = random.sample(tickets, 2)
    return tickets, winners

tickets, winners = lottery_tickets()
print("Lottery winners:", winners)


3.
import random

otp = random.randint(100000, 999999)
print("OTP:", otp)    


4.
import random

input_string = "HelloParagSir"
random_char = random.choice(input_string)
print("Random Character:", random_char)  


5.
import random
import string

characters = string.ascii_letters
random_characters = random.choices(characters, k=5)
random_string = ''.join(random_characters)

print("Random String:", random_string)   



6.
import random
import string

def generate_password():
    password_length = 10
    
    password = [
        random.choice(string.ascii_uppercase), 
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    

    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length-4)
    
    random.shuffle(password)
    
    return ''.join(password)

password = generate_password()
print("Generated Password:", password)    



7.
import random

num1 = random.uniform(1.0, 10.0)  
num2 = random.uniform(1.0, 10.0)
result = num1 * num2
print("Multiplication Result:", result)     



8.
import random
import string
import urllib.parse

secure_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

base_url = "https://www.example.com/"
random_url = urllib.parse.urljoin(base_url, ''.join(random.choices(string.ascii_letters + string.digits, k=10)))

print("Secure Token:", secure_token)
print("Random URL:", random_url)      


9.
import random

random.seed(42)

dice_roll = random.choice([1, 2, 3, 4, 5, 6])

print("Dice Roll (Same number):", dice_roll)  


10.
import random
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 1, 1)

time_delta = end_date - start_date
random_days = random.randint(0, time_delta.days)
random_date = start_date + timedelta(days=random_days)

print("Random Date:", random_date.strftime("%Y-%m-%d"))




























 
