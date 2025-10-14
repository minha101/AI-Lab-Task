# LUHN Algorithm implementation
card_number = input("Enter a card number: ")

cleaned_number = ""
i = 0
while i < len(card_number):
    if card_number[i] != " ":
        cleaned_number += card_number[i]
    i += 1

total = 0
is_second = False
k = len(cleaned_number) - 1
while k >= 0:
    digit = int(cleaned_number[k])
    
    if is_second:
        digit = digit * 2
        if digit > 9:
            digit = digit - 9
        total += digit
        is_second = False
    else:
        total += digit
        is_second = True
    
    k -= 1

if total % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")