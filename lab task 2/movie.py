films = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

additional_films = int(input("How many extra films do you want to add? "))

for i in range(additional_films):
    name = input("Enter film name: ")
    cost = int(input("Enter film cost: "))
    films.append((name, cost))

sum_of_costs = 0
for film in films:
    sum_of_costs += film[1]

mean_cost = sum_of_costs / len(films)
print("The mean cost of all films is:", mean_cost)

print("Films with cost exceeding the mean:")
counter = 0
for film in films:
    if film[1] > mean_cost:
        gap = film[1] - mean_cost
        print(f"{film[0]} exceeds by {gap} over the mean.")
        counter += 1
print("Count of films above mean:", counter)