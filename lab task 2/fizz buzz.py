limit = 101
print("Let's play Fizz Buzz up to", limit)

previous = 0 
for number in range(1, limit + 1):
    
    total = number + previous  

    if number % 2 != 0: 
        user_input = input("Your turn: ")

        if number % 3 == 0 and number % 5 == 0:
            correct = "Fizz Buzz"
        elif number % 3 == 0:
            correct = "Fizz"
        elif number % 5 == 0:
            correct = "Buzz"
        else:
            correct = str(number)

        if user_input != correct:
            print("Wrong! You are eliminated. The correct answer was:", correct)
            break
        else:
            print(f"Correct! (Previous + Current = {previous} + {number} = {total})")

    else:  
        if number % 3 == 0 and number % 5 == 0:
            print("Computer says: Fizz Buzz")
        elif number % 3 == 0:
            print("Computer says: Fizz")
        elif number % 5 == 0:
            print("Computer says: Buzz")
        else:
            print("Computer says:", number)

        print(f"(Previous + Current = {previous} + {number} = {total})")

    
    previous = number
