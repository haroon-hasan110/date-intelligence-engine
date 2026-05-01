def get_zodiac(month, day):
    zodiac_data = [
        ((3, 21), (4, 19), "Aries", "♈", "Fire", ["Bold", "Energetic", "Confident"]),
        ((4, 20), (5, 20), "Taurus", "♉", "Earth", ["Stable", "Loyal", "Patient"]),
        ((5, 21), (6, 20), "Gemini", "♊", "Air", ["Curious", "Social", "Quick-witted"]),
        ((6, 21), (7, 22), "Cancer", "♋", "Water", ["Emotional", "Loyal", "Intuitive"]),
        ((7, 23), (8, 22), "Leo", "♌", "Fire", ["Confident", "Leader", "Creative"]),
        ((8, 23), (9, 22), "Virgo", "♍", "Earth", ["Practical", "Detail-oriented", "Smart"]),
        ((9, 23), (10, 22), "Libra", "♎", "Air", ["Balanced", "Charming", "Fair"]),
        ((10, 23), (11, 21), "Scorpio", "♏", "Water", ["Intense", "Passionate", "Mysterious"]),
        ((11, 22), (12, 21), "Sagittarius", "♐", "Fire", ["Adventurous", "Optimistic", "Honest"]),
        ((12, 22), (1, 19), "Capricorn", "♑", "Earth", ["Disciplined", "Ambitious", "Focused"]),
        ((1, 20), (2, 18), "Aquarius", "♒", "Air", ["Innovative", "Independent", "Unique"]),
        ((2, 19), (3, 20), "Pisces", "♓", "Water", ["Dreamy", "Kind", "Creative"]),
    ]

    for start, end, name, symbol, element, traits in zodiac_data:
        sm, sd = start
        em, ed = end

        if sm <= em:
            if (month == sm and day >= sd) or (month == em and day <= ed) or (sm < month < em):
                return {
                    "name": name,
                    "symbol": symbol,
                    "element": element,
                    "traits": traits,
                }
        else:
            if (month == sm and day >= sd) or (month == em and day <= ed) or (month > sm or month < em):
                return {
                    "name": name,
                    "symbol": symbol,
                    "element": element,
                    "traits": traits,
                }

    return None