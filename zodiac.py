from datetime import datetime

def get_zodiac_sign(month, day):
    """Return zodiac sign based on month and day"""
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]
    
    for sign, start, end in zodiac_signs:
        start_month, start_day = start
        end_month, end_day = end
        
        if start_month == end_month:
            if month == start_month and start_day <= day <= end_day:
                return sign
        else:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return sign
    return None

def get_monthly_reading(sign):
    """Return astrology reading for the month"""
    readings = {
        "Capricorn": "Focus on your goals and consolidate your plans for the future.",
        "Aquarius": "Innovation and creativity are highlighted. Embrace new ideas.",
        "Pisces": "Trust your intuition and let compassion guide your decisions.",
        "Aries": "Take bold action and pursue opportunities with confidence.",
        "Taurus": "Stability and security are your focus. Invest wisely.",
        "Gemini": "Communication flourishes. Share your ideas and connect with others.",
        "Cancer": "Home and family matters take priority. Nurture relationships.",
        "Leo": "Creativity and self-expression shine. Be bold and authentic.",
        "Virgo": "Attention to detail brings success. Organize and refine.",
        "Libra": "Balance and harmony are key. Seek peace in your interactions.",
        "Scorpio": "Deep transformation occurs. Embrace change and renewal.",
        "Sagittarius": "Adventure calls. Expand your horizons and explore new paths.",
    }
    return readings.get(sign, "No reading available")

# Main script
date_input = input("Enter your birth date (MM-DD): ")
try:
    month, day = map(int, date_input.split("-"))
    sign = get_zodiac_sign(month, day)
    if sign:
        print(f"Your zodiac sign: {sign}")
        print(f"Monthly reading: {get_monthly_reading(sign)}")
    else:
        print("Invalid date entered")
except ValueError:
    print("Please enter date in MM-DD format")