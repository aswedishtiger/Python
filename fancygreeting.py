import random
from datetime import datetime

def get_time_based_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def greet(name):
    greetings = get_time_based_greeting()
    positive_messages = [
        "You're doing amazing things!",
        "Keep pushing forward!",
        "Stay positive and productive!",
        "Believe in yourself!",
        "Great things are coming your way!"
    ]
    
    print(f"{greetings}, {name}!")
    print(f"{random.choice(positive_messages)}")
    print("Hope you have a fantastic day!")

def main():
    print("Welcome to the Greeting Program!")
    name = input("What's your name? ")
    greet(name)
    
    repeat = input("Would you like another greeting? (yes/no): ").lower()
    while repeat == 'yes':
        greet(name)
        repeat = input("Would you like another greeting? (yes/no): ").lower()

if __name__ == "__main__":
    main()