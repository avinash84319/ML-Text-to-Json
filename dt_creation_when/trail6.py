import csv
import random

top_10_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow"]

when_types = {
    "today": ["now", "immediately", "right away", "as soon as possible"],
    "tomorrow": ["tomorrow", "next day"],
    "time": ["this week", "next week", "soon", "as soon as possible", "next month", "in a month", "in two months", "later",
             "in 1 hour", "in 3 hours", "in 6 hours", "in 12 hours", "in 24 hours", "in 2 days", "in 3 days", "in 1 week"]
}

intent_types = {
    "find_doctor": ["doctor", "physician", "healthcare provider"],
    "find_medicalshop": ["medical shop", "pharmacy", "drugstore"],
    "find_hospital": ["hospital", "medical center", "healthcare facility"],
    "find_lab": ["lab", "diagnostic center", "testing facility"],
    "book_appointment": ["appointment", "schedule appointment", "book appointment"],
    "my_appointments": ["my appointments", "upcoming appointments", "scheduled visits"],
    "my_records": ["my medical records", "health records", "medical history"]
}

verbs = ["need", "want", "am looking for", "require", "seeking", "trying to find", "wish to locate", "have a question about", "looking to consult for"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific medical procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital chain", "specific time for appointments"]

def generate_query(when_type):
    query_structure = random.choice([
        "I {verb} {article} {keyword} {preposition} {when_type}.",
        "Where can I {verb} {article} {keyword} {preposition} {when_type}?",
        "{verb} {article} {keyword} {preposition} {when_type}.",
        "Looking for {article} {keyword} {preposition} {when_type}.",
        "Can you help me {verb} {article} {keyword} {preposition} {when_type}?",
        "{verb} {article} {preposition} {keyword} {when_type}.",
        "Tell me about {keyword} {preposition} {when_type}.",
        "{verb} {keyword} {preposition} {when_type}.",
        "I'm {verb} {keyword} {preposition} {when_type}.",
        "Looking to {verb} {keyword} {preposition} {when_type}."
    ])

    keyword, preposition = random.choice(list(when_types.keys())), random.choice(list(when_types.keys()))
    
    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword,
        preposition=preposition,
        when_type=when_type
    )

    if keyword == "today":
        query += f" I need to see a {random.choice(['doctor', 'physician', 'healthcare provider'])} because of {random.choice(scenarios)}."
        query += f" I prefer {random.choice(user_preferences)}."
    elif keyword == "tomorrow":
        query += f" It's {random.choice(scenarios)}, and I require help from a {random.choice(['hospital', 'medical center', 'healthcare facility'])}."
        query += f" I'd like a hospital {random.choice(user_preferences)}."
    elif keyword == "time":
        query += f" I want to {random.choice(scenarios)}."
        query += f" Please find a suitable time for the appointment, {random.choice(user_preferences)}."
    
    return query.capitalize(), when_type

def generate_query_without_time(intent_type):
    query_structure = random.choice([
        "I {verb} {article} {keyword}.",
        "Where can I {verb} {article} {keyword}?",
        "{verb} {article} {keyword}.",
        "Looking for {article} {keyword}.",
        "Can you help me {verb} {article} {keyword}?",
        "{verb} {article} {keyword}.",
        "Tell me about {keyword}.",
        "{verb} {keyword}.",
        "I'm {verb} {keyword}.",
        "Looking to {verb} {keyword}."
    ])

    keyword, _ = random.choice(list(intent_types.keys())), random.choice(list(intent_types.keys()))
    
    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword
    )

    if keyword == "find_doctor":
        query += f" I need to see a {random.choice(intent_types[keyword])} because of {random.choice(scenarios)}."
        query += f" I prefer {random.choice(user_preferences)}."
    elif keyword == "find_medicalshop":
        query += f" I'm looking for a {random.choice(intent_types[keyword])} to purchase {random.choice(['medications', 'prescriptions', 'health products'])}."
    elif keyword == "find_hospital":
        query += f" I require help from a {random.choice(intent_types[keyword])} because it's {random.choice(scenarios)}."
        query += f" I'd like a hospital {random.choice(user_preferences)}."
    elif keyword == "find_lab":
        query += f" I need to visit a {random.choice(intent_types[keyword])} for {random.choice(['tests', 'diagnostics', 'health screenings'])}."
    elif keyword == "book_appointment":
        query += f" I want to {random.choice(intent_types[keyword])}."
        query += f" Please find a suitable time for the appointment, {random.choice(user_preferences)}."
    elif keyword == "my_appointments":
        query += f" Can you tell me about {random.choice(intent_types[keyword])}?"
    elif keyword == "my_records":
        query += f" I want to check {random.choice(intent_types[keyword])} for my review."

    return query.capitalize(), "no_time"

# Generate examples with "when"
examples_with_time = [generate_query(when_type) for _ in range(4000) for when_type in when_types]

# Generate examples without time intent
examples_without_time = [generate_query_without_time(intent_type) for _ in range(4000) for intent_type in intent_types]

# Combine the two sets of examples
combined_examples = examples_with_time + examples_without_time

# Shuffle the combined examples
random.shuffle(combined_examples)

# Write the combined examples to a CSV file
with open('trail6.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "when"])
    writer.writerows(combined_examples)