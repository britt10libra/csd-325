# Brittany Smith
# 8/15/26
# Module 1.3 Assignment
# Purpose: program asks the user for a number of bottles and
# counts down until there are no bottles left.
# Source: concepts from The Pragmatic Programmer
# Python Software Foundation. Python Documentation.
# https://docs.python.org/3/tutorial/controlflow.html

def countdown(bottles):

    # Continue looping while there is more than one bottle remaining
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        # Subtract one bottle from the current total
        bottles = bottles - 1

        # Use singular wording when only one bottle remains
        if bottles == 1:
            print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.")
        else:
            # Use plural wording when more than one bottle remains
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.")

        # Print a blank line to make the outpout easier to read
        print()

    # Display the final verse when only one bottle is left
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottles of beer on the wall.")
    print()

# Ask the user how many bottles should be used for the countdown
bottles = int(input("Enter number of bottles: "))

# Pass the user's number into the countdown function
countdown(bottles)

# Display the final message after the function finishes
print("Time to buy more bottles of beer.")