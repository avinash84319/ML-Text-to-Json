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

# More verbs, prepositions, articles, and Indian cities (including Mysore)
verbs = ["need", "want", "am looking for", "require", "seeking", "trying to find", "wish to locate", "have a query about", "looking to consult for"]
prepositions = ["near", "in", "around", "close to", "within", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Mysore"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific medical procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital chain", "specific time for appointments"]

# Function to generate a query for a given action
def generate_query(action):
    query_structure = random.choice([
        "I {verb} {article} {keyword} {preposition}.",
        "Where can I {verb} {article} {keyword} {preposition}?",
        "{verb} {article} {keyword} {preposition}.",
        "Looking for {article} {keyword} {preposition}.",
        "Can you help me {verb} {article} {keyword} {preposition}?"
    ])

    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=random.choice(actions[action]),
        preposition=random.choice(prepositions)
    )

    # Introduce additional details based on the action
    if action == "find_doctor":
        query += f" I have a concern related to {random.choice(scenarios)}."
        query += f" Preferably, I would like a {random.choice(user_preferences)}."
    elif action == "find_hospital":
        query += f" It's an {random.choice(scenarios)} situation, and I need immediate assistance."
        query += f" I prefer a hospital with {random.choice(user_preferences)}."
    elif action == "book_appointment":
        query += f" I need to {random.choice(scenarios)}."
        query += f" Can you assist in finding a suitable time for the appointment, preferably {random.choice(user_preferences)}?"
    elif action == "my_appointments":
        query += f" Can you provide information about my {random.choice(actions[action])}?"
    elif action == "my_records":
        query += f" I would like to access {random.choice(actions[action])} for a review."

    return query.capitalize()

# Generate 4000 examples
examples = [[generate_query(action), action] for _ in range(4000) for action in actions]

# Write to CSV file
with open('generated_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "action"])
    writer.writerows(examples)
