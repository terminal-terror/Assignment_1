def chinese_zodiac(year):
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    return zodiac_signs[year % 12]

# Get the user's birth year
birth_year = int(input("Enter your birth year: "))
zodiac_sign = chinese_zodiac(birth_year)
print(f"Your Chinese zodiac sign is: {zodiac_sign}")