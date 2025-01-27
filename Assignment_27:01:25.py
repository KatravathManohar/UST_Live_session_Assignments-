import random
lucky_number = int(input("Enter your lucky number between 1 and 10: "))

if lucky_number < 1 or lucky_number > 10:
    print("Please enter a number between 1 and 10.")
else:
    for attempt in range(1, 101):  # 100 attempts
        random_number = random.randint(1, 10)  # Generate random number between 1 and 10
        print(f"For Attempt {attempt}: Generated random number: {random_number}")
        
        if random_number == lucky_number:
            print(f"Congratulations! The random number matched your lucky number {lucky_number} on attempt {attempt}.")
            break  # Exit the loop when numbers match
    
    else:
        print("Sorry, the lucky number was not matched in 100 attempts.")
            
