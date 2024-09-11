def zodiac_sign(day, month):
    if month == 'december':
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 'january':
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'february':
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'march':
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'april':
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'may':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'june':
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'july':
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'august':
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'september':
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'october':
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'november':
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    return astro_sign

if __name__ == "__main__":

    month = input("Please enter your birth month (january, february, etc.): ").lower()


    day = int(input("Please enter the day you were born (1-31)): "))


    
    sign = zodiac_sign(day, month)
    print(f"Your astrological sign is: {sign}")
