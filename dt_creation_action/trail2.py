import csv
import random

# Define actions with associated keywords and additional details
actions = {
    "find_doctor": ["doctor", "physician", "healthcare provider", "medical practitioner", "family doctor", "specialist", "GP",
                    "dermatologist", "cardiologist", "pediatrician", "gynecologist", "psychiatrist"],
    "find_medicalshop": ["pharmacy", "drugstore", "chemist", "medical store", "apothecary", "health supply store"],
    "find_hospital": ["hospital", "medical center", "healthcare facility", "clinic", "emergency room", "urgent care", "infirmary"],
    "find_lab": ["lab", "diagnostic center", "testing facility", "medical laboratory", "pathology lab", "clinical lab"],
    "book_appointment": ["appointment", "schedule", "book", "consultation", "meet with a doctor", "arrange a visit"],
    "my_appointments": ["my appointments", "upcoming appointments", "scheduled visits", "doctor appointments"],
    "my_records": ["my medical records", "health records", "medical history", "patient records", "health information"]
}

# Shortened verbs, prepositions, articles, and expanded Indian cities (including Mysore)
verbs = ["need", "want", "look for", "require", "seek", "try to find", "wish", "question", "consult for"]
prepositions = ["near", "in", "around", "close to", "within", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", 
                "Kolkata", "Ahmedabad", "Mysore", "Pune", "Jaipur", "Lucknow", "Nagpur", "Indore", "Visakhapatnam", 
                "Kochi", "Coimbatore", "Bhopal", "Patna", "Vadodara", "Thiruvananthapuram", "Surat", "Kanpur", "Bhubaneswar",
                "Agra", "Amritsar", "Varanasi", "Guwahati", "Jodhpur", "Raipur", "Allahabad", "Aurangabad", "Ranchi"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific medical procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital chain", "specific time for appointments"]

# Function to generate a query for a given action
def generate_query(action):
    query_structure = random.choice([
        "Need {article} {keyword} {preposition} {verb}?",
        "Where {verb} {article} find {keyword} {preposition}?",
        "{verb} {article} {keyword} {preposition}.",
        "Looking for {article} {keyword} {preposition}.",
        "Help me {verb} {article} find {keyword} {preposition}.",
        "{verb} {article} {preposition} {keyword}.",
        "Tell me about {keyword} {preposition}.",
        "{verb} {keyword} {preposition}.",
        "I'm {verb} {keyword} {preposition}.",
        "Find {article} {keyword} {preposition} {verb}.",
        "Can {verb} {article} find {keyword} {preposition}?",
    ])

    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=random.choice(actions[action]),
        preposition=random.choice(prepositions)
    )

    # Introduce additional details based on the action
    if action == "find_doctor":
        query += f" Need {random.choice(actions[action])}, {random.choice(scenarios)}."
        query += f" Prefer {random.choice(user_preferences)}."
    elif action == "find_hospital":
        query += f" It's {random.choice(scenarios)}, need {random.choice(actions[action])}."
        query += f" Prefer hospital {random.choice(user_preferences)}."
    elif action == "book_appointment":
        query += f" Want {random.choice(scenarios)}."
        query += f" Find time, {random.choice(user_preferences)}."
    elif action == "my_appointments":
        query += f" Tell about {random.choice(actions[action])}?"
    elif action == "my_records":
        query += f" Check {random.choice(actions[action])}, review."

    return query.capitalize()

# Generate 4000 examples
examples = [[generate_query(action), action] for _ in range(4000) for action in actions]

# Write to CSV file
with open('trail2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "action"])
    writer.writerows(examples)
