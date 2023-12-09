import csv
import random

# Define prepositions as location types and related keywords
location_types = {
    "near": ["close", "nearby", "around", "proximity"],
    "in": ["within", "inside", "within the vicinity of"],
    "around": ["surrounding", "around", "nearby", "in the area of"],
    "close_to": ["near", "close to", "adjacent to", "in proximity to"],
    "within": ["inside", "within", "in the confines of"]
}

# More verbs, articles, and expanded Indian cities (including Mysore)
verbs = ["need", "want", "am looking for", "require", "seeking", "trying to find", "wish to locate", "have a question about", "looking to consult for"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific medical procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital chain", "specific time for appointments"]

# Function to generate a query for a given location type
def generate_query(location_type):
    query_structure = random.choice([
        "I {verb} {article} {keyword} {preposition}.",
        "Where can I {verb} {article} {keyword} {preposition}?",
        "{verb} {article} {keyword} {preposition}.",
        "Looking for {article} {keyword} {preposition}.",
        "Can you help me {verb} {article} {keyword} {preposition}?",
        "{verb} {article} {preposition} {keyword}.",
        "Tell me about {keyword} {preposition}.",
        "{verb} {keyword} {preposition}.",
        "I'm {verb} {keyword} {preposition}.",
        "Looking to {verb} {keyword} {preposition}."
    ])

    keyword, preposition = random.choice(list(location_types[location_type])), location_type
    
    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword,
        preposition=preposition
    )

    # Introduce additional details based on the location type
    if location_type == "near":
        query += f" I need to see a {random.choice(['doctor', 'physician', 'healthcare provider'])} because of {random.choice(scenarios)}."
        query += f" I prefer {random.choice(user_preferences)}."
    elif location_type == "in":
        query += f" It's {random.choice(scenarios)}, and I require help from a {random.choice(['hospital', 'medical center', 'healthcare facility'])}."
        query += f" I'd like a hospital {random.choice(user_preferences)}."
    elif location_type == "around":
        query += f" I want to {random.choice(scenarios)}."
        query += f" Please find a suitable time for the appointment, {random.choice(user_preferences)}."
    elif location_type == "close_to":
        query += f" Can you tell me about {random.choice(['my appointments', 'upcoming appointments', 'scheduled visits'])}?"
    elif location_type == "within":
        query += f" I want to check {random.choice(['my medical records', 'health records', 'medical history'])} for my review."

    return query.capitalize()

# Generate 4000 examples
examples = [[generate_query(location_type), location_type] for _ in range(4000) for location_type in location_types]

# Write to CSV file
with open('generated_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "location_type"])
    writer.writerows(examples)
