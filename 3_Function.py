# concept -> 1
def hello(to):
    print("Hello , ",to)


# concept -> 2
# Step 1: The script starts executing from the top.
# Step 2: hello() is called initially without any argument. It uses the default parameter 'world' and prints "Hello, world".
# Step 3: The script pauses at input("What is your name?"), waiting for the user to provide input.
# Step 4: The user enters their name which is captured by input() and stored in the variable name.
# Step 5: hello(name) is called next, passing the user's input (name) as the argument. It then prints "Hello, " followed by the user's name.
# Step 6: The script completes its execution after printing the final output.

def hello(to = 'world'):
    print("Hello , ",to)

hello()
name = input("What is your name ?")
hello(name)

# # Concpet -> 3 : 
# # Execution Flow:
# # When you run main(), it prompts you to enter your name.
# # It then calls hello(name) with the entered name as an argument.
# # The hello() function prints a greeting message, using the provided name or defaulting to "World" if no name was entered.
def main():
    name = input("What's your name ? ")
    hello(name)

def hello(to = "World"):
    print("hello , ",to)

main()


# concept -> 4
# Control Flow Summary:
# Program Start: Execution begins from the start of the script.
# Function Definitions: The square and main functions are defined to encapsulate specific tasks.
# Main Function Execution:
# main() is called, initiating the primary flow of the program.
# User Input:
# The program prompts the user to enter a value for x.
# Input Processing:
# The user input, initially a string, is converted into an integer using int().
# Function Call (square(x)):
# The main() function calls square(x) with the integer value of x.
# Square Calculation:
# Inside square(n), the square of n (i.e., n ** 2) is computed using the pow() function.
# Return Result:
# The squared value is returned from square(x) back to main().
# Output:
# Finally, main() prints the result, displaying "Squared of x is : " followed by the computed squared value.
# Program End:
# Execution concludes after printing the result, completing the program's operation.

def main():
    x = int(input("What is value of x ?"))
    print("Squared of x is : ", square(x))

def square(n):
    return pow(n,2);

main()

