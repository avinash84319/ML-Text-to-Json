import csv
import random

indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara",
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Ranchi", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar",
    "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Howrah", "Ranchi", "Gwalior",
    "Jabalpur", "Coimbatore", "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati", "Chandrapur", "Solapur",
    "Hubli-Dharwad", "Bareilly", "Moradabad", "Mysuru", "Gurgaon", "Aligarh", "Jalandhar", "Tiruchirappalli", "Bhubaneswar",
    "Salem", "Warangal", "Thiruvananthapuram", "Bhiwandi", "Saharanpur", "Gorakhpur", "Bikaner", "Amravati", "Noida",
    "Jamshedpur", "Bhilai", "Cuttack", "Firozabad", "Kochi", "Nellore", "Bhavnagar", "Dehradun", "Durgapur", "Asansol",
    "Rourkela", "Nanded", "Kolhapur", "Ajmer", "Akola", "Gulbarga", "Jamnagar", "Ujjain", "Loni", "Siliguri", "Jhansi",
    "Ulhasnagar", "Jammu", "Sangli-Miraj & Kupwad", "Mangalore", "Erode", "Belgaum", "Ambattur", "Tirunelveli", "Malegaon",
    "Gaya", "Jalgaon", "Udaipur", "Maheshtala", "Tirupur", "Davanagere", "Kozhikode", "Akbarpur", "Bhagalpur", "Agra",
    "Bhiwani", "Berhampur", "Bhopal", "Bikaner", "Bilaspur", "Burhanpur", "Chandrapur", "Chittoor", "Cuttack", "Dhule",
    "Dindigul", "Durg", "Erode", "Gandhinagar", "Guntur", "Guwahati", "Haldia", "Haridwar", "Hospet", "Hosur", "Hugli-Chinsurah",
    "Imphal", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Junagadh", "Karimnagar", "Khammam", "Kollam", "Kurnool",
    "Latur", "Mathura", "Muzaffarpur", "Nagercoil", "Nangloi Jat", "North Dumdum", "Patiala", "Proddatur", "Raichur", "Raiganj",
    "Rampur", "Ratlam", "Raurkela", "Rohtak", "Sagar", "Shivamogga", "Shimla", "Siliguri", "Solapur", "Sonipat", "South Dumdum",
    "Sri Ganganagar", "Srinagar", "Thane", "Thanjavur", "Thrissur", "Tiruchirappalli", "Tirunelveli", "Tirupati", "Tirupur",
    "Ulhasnagar", "Vadodara", "Vasai-Virar", "Vijayawada", "Visakhapatnam", "Warangal", "Yamunanagar",
    # Add more cities here (at least 900 more)
    "City1001", "City1002", "City1003", "City1004", "City1005", "City1006", "City1007", "City1008", "City1009", "City1010",
    "City1011", "City1012", "City1013", "City1014", "City1015", "City1016", "City1017", "City1018", "City1019", "City1020",
    # ... (repeat the pattern until you reach 1000 cities)
    "City1991", "City1992", "City1993", "City1994", "City1995", "City1996", "City1997", "City1998", "City1999", "City2000"
]

location_types = {
    "near": ["close", "nearby", "around", "proximity"],
    "in": ["within", "inside", "within the vicinity of"],
    "around": ["surrounding", "around", "nearby", "in the area of"],
    "close_to": ["near", "close to", "adjacent to", "in proximity to"],
    "within": ["inside", "within", "in the confines of"]
}

verbs = ["need", "want", "seek", "require", "searching", "look for", "have a question about", "trying to find", "wish to locate"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific procedure", "preventive care", "regular checkup", "consultation"]

def generate_query_structure(location_type):
    return random.choice([
        "Find a {article} {keyword} {preposition} in {city}.",
        "Where is {keyword} {preposition} in {city}?",
        "Looking for {article} {keyword} {preposition} in {city}.",
        "Can you help me {verb} {article} {keyword} {preposition} in {city}?",
        "I'm {verb} {article} {keyword} {preposition} near {city}.",
        "Tell me about {keyword} {preposition} in {city}.",
        "{verb} {article} {keyword} {preposition} near {city}.",
        "Looking to {verb} {article} {keyword} {preposition} in {city}."
    ])

def generate_query(location_type, city=None):
    query_structure = generate_query_structure(location_type)

    keyword, preposition = random.choice(list(location_types[location_type])), location_type
    
    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword,
        preposition=preposition,
        city=city
    )

    if location_type == "near":
        query += f" Need {random.choice(['doctor', 'physician', 'healthcare provider'])} for {random.choice(scenarios)}."
    elif location_type == "in":
        query += f" It's {random.choice(scenarios)}, and I require {random.choice(['hospital', 'medical center', 'healthcare facility'])}."
    elif location_type == "around":
        query += f" I want to {random.choice(scenarios)}."
    elif location_type == "close_to":
        query += f" Tell me about {random.choice(['my appointments', 'upcoming appointments', 'scheduled visits'])}."
    elif location_type == "within":
        query += f" Check {random.choice(['my medical records', 'health records', 'medical history'])} for my review."

    return query.capitalize(),city

def generate_query_structure_without(location_type):
    return random.choice([
        "Find a {article} {keyword} {preposition} nearby.",
        "Where is {keyword} {preposition} around me?",
        "Looking for {article} {keyword} {preposition}.",
        "Can you help me {verb} {article} {keyword} {preposition}",
        "I'm {verb} {article} {keyword} {preposition}.",
        "Tell me about {keyword} {preposition} nearby.",
        "{verb} {article} {keyword} {preposition}.",
        "Looking to {verb} {article} {keyword} {preposition}."
    ])

def generate_query_without(location_type, city=None):
    query_structure = generate_query_structure_without(location_type)

    keyword, preposition = random.choice(list(location_types[location_type])), location_type
    
    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword,
        preposition=preposition,
        city=city
    )

    if location_type == "near":
        query += f" Need {random.choice(['doctor', 'physician', 'healthcare provider'])} for {random.choice(scenarios)}."
    elif location_type == "in":
        query += f" It's {random.choice(scenarios)}, and I require {random.choice(['hospital', 'medical center', 'healthcare facility'])}."
    elif location_type == "around":
        query += f" I want to {random.choice(scenarios)}."
    elif location_type == "close_to":
        query += f" Tell me about {random.choice(['my appointments', 'upcoming appointments', 'scheduled visits'])}."
    elif location_type == "within":
        query += f" Check {random.choice(['my medical records', 'health records', 'medical history'])} for my review."

    return query.capitalize()

# Generate more examples with "current_loc"
examples_with_current_loc = [[generate_query_without(location_type), "current_loc"] for _ in range(600) for location_type in location_types]

# Generate examples for each city
examples = []
for location_type in location_types:
    city_examples = [generate_query(location_type, city) for city in indian_cities for _ in range(100)]
    examples.extend(city_examples)

with open('varied_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "city"])
    writer.writerows(examples + examples_with_current_loc)
