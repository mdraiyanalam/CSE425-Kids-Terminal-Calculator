import math
import json
import pyttsx3
import speech_recognition as sr

# Global Variables
memory = None
history = []
progress_file = "progress.json"
engine = pyttsx3.init()

# Helper Functions
def speak_feedback(message):
    print(message)
    engine.say(message)
    engine.runAndWait()

def log_history(operation, result):
    history.append(f"{operation} = {result}")
    save_progress(operation, result)

def save_progress(operation, result):
    data = {"operation": operation, "result": result}
    with open(progress_file, "a") as file:
        file.write(json.dumps(data) + "\n")

def show_progress():
    try:
        with open(progress_file, "r") as file:
            for line in file:
                entry = json.loads(line.strip())
                print(f"{entry['operation']} = {entry['result']}")
    except FileNotFoundError:
        print("No progress recorded yet.")

# Voice Interaction
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak_feedback("Listening for your voice command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            speak_feedback(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak_feedback("Sorry, I did not understand that.")
        except sr.RequestError:
            speak_feedback("Speech recognition service is unavailable.")

def voice_operations():
    command = voice_input()
    if "add" in command or "plus" in command:
        numbers = [float(num) for num in command.split() if num.isdigit()]
        result = sum(numbers)
        speak_feedback(f"The result is: {result}")
    # Additional operations like subtraction, multiplication, etc., can be added here.

# Basic Arithmetic Operations
def basic_operations():
    print("\nBasic Arithmetic Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Choose an operation (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        speak_feedback(f"The result is: {result}")
        log_history(f"{num1} + {num2}", result)
    elif choice == '2':
        result = num1 - num2
        speak_feedback(f"The result is: {result}")
        log_history(f"{num1} - {num2}", result)
    elif choice == '3':
        result = num1 * num2
        speak_feedback(f"The result is: {result}")
        log_history(f"{num1} * {num2}", result)
    elif choice == '4':
        if num2 == 0:
            speak_feedback("Division by zero is not allowed!")
        else:
            result = num1 / num2
            speak_feedback(f"The result is: {result}")
            log_history(f"{num1} / {num2}", result)
    else:
        speak_feedback("Invalid choice!")

# Advanced Mathematical Operations
def advanced_operations():
    print("\nAdvanced Mathematical Operations:")
    print("1. Power (x^y)")
    print("2. Square Root")
    print("3. Modulus")
    choice = input("Choose an operation (1-3): ")

    if choice == '1':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = math.pow(base, exponent)
        speak_feedback(f"The result is: {result}")
        log_history(f"{base} ^ {exponent}", result)
    elif choice == '2':
        num = float(input("Enter the number: "))
        if num < 0:
            speak_feedback("Square root of a negative number is not supported!")
        else:
            result = math.sqrt(num)
            speak_feedback(f"The result is: {result}")
            log_history(f"√{num}", result)
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 % num2
        speak_feedback(f"The result is: {result}")
        log_history(f"{num1} % {num2}", result)
    else:
        speak_feedback("Invalid choice!")

# Memory Storage and Recall
def memory_operations():
    global memory
    print("\nMemory Operations:")
    print("1. Store (m+)")
    print("2. Recall (mr)")
    print("3. Clear (mc)")
    choice = input("Choose an operation (1-3): ")

    if choice == '1':
        memory = float(input("Enter a value to store in memory: "))
        speak_feedback("Value stored in memory!")
    elif choice == '2':
        if memory is None:
            speak_feedback("Memory is empty!")
        else:
            speak_feedback(f"Recalled value from memory: {memory}")
    elif choice == '3':
        memory = None
        speak_feedback("Memory cleared!")
    else:
        speak_feedback("Invalid choice!")

# History Management
def view_history():
    if not history:
        speak_feedback("\nNo history available!")
    else:
        print("\nHistory:")
        for entry in history:
            print(entry)

def clear_history():
    global history
    history = []
    speak_feedback("History cleared!")

# Learning Mode
def learning_mode():
    print("\nLearning Mode:")
    print("Step-by-step solutions for math problems.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        speak_feedback(f"Step 1: Add {num1} and {num2}.")
        result = num1 + num2
    elif operation == '-':
        speak_feedback(f"Step 1: Subtract {num2} from {num1}.")
        result = num1 - num2
    elif operation == '*':
        speak_feedback(f"Step 1: Multiply {num1} and {num2}.")
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            speak_feedback("Division by zero is not allowed!")
            return
        speak_feedback(f"Step 1: Divide {num1} by {num2}.")
        result = num1 / num2
    else:
        speak_feedback("Invalid operation!")
        return

    speak_feedback(f"The result is: {result}")

# Unit Conversion
def unit_conversion():
    print("\nUnit Conversion:")
    print("1. Meters ↔ Kilometers")
    print("2. Grams ↔ Kilograms")
    choice = input("Choose a conversion (1-2): ")

    if choice == '1':
        meters = float(input("Enter value in meters: "))
        speak_feedback(f"{meters} meters is {meters / 1000} kilometers.")
    elif choice == '2':
        grams = float(input("Enter value in grams: "))
        speak_feedback(f"{grams} grams is {grams / 1000} kilograms.")
    else:
        speak_feedback("Invalid choice!")

# Math in Everyday Life Mode
def everyday_math_mode():
    print("\nMath in Everyday Life Mode:")
    print("1. Budgeting Problem")
    print("2. Time-based Puzzle")
    choice = input("Choose a challenge (1-2): ")

    if choice == '1':
        budget = 10
        toy_price = 2
        speak_feedback(f"You have ${budget}. Each toy costs ${toy_price}.")
        answer = int(input("How many toys can you buy? "))
        if answer == budget // toy_price:
            speak_feedback("Correct!")
        else:
            speak_feedback("Try again.")
    elif choice == '2':
        start_time = 3
        duration = 2
        speak_feedback(f"A train leaves at {start_time} PM and takes {duration} hours.")
        answer = int(input("What time will it arrive? "))
        if answer == (start_time + duration) % 12:
            speak_feedback("Correct!")
        else:
            speak_feedback("Try again.")
    else:
        speak_feedback("Invalid choice!")

# Personalized Greetings
def personalized_greetings():
    name = input("Enter your name: ")
    speak_feedback(f"Hello, {name}! Welcome to the Advanced Calculator.")

# Main Menu
def main():
    personalized_greetings()

    while True:
        print("\nMain Menu:")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Memory Operations")
        print("4. View History")
        print("5. Clear History")
        print("6. Learning Mode")
        print("7. Unit Conversion")
        print("8. Voice Interaction")
        print("9. Progress Tracking")
        print("10. Math in Everyday Life Mode")
        print("11. Exit")

        choice = input("Choose an option (1-11): ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            advanced_operations()
        elif choice == '3':
            memory_operations()
        elif choice == '4':
            view_history()
        elif choice == '5':
            clear_history()
        elif choice == '6':
            learning_mode()
        elif choice == '7':
            unit_conversion()
        elif choice == '8':
            voice_operations()
        elif choice == '9':
            show_progress()
        elif choice == '10':
            everyday_math_mode()
        elif choice == '11':
            speak_feedback("Goodbye!")
            break
        else:
            speak_feedback("Invalid choice!")

# Run the Calculator
if __name__ == "__main__":
    main()
