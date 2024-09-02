import csv
import random

when_types = ["today", "tomorrow", "no_time"]

verbs = ["need", "want", "am looking for", "require", "seeking", "trying to find", "wish to locate", "have a question about", "looking to consult for"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "routine check-up", "second opinion", "specific medical procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital chain", "specific time for appointments"]

def generate_query():
    query_structure = random.choice([
        "I {verb} {article} {keyword} {when_type}.",
        "Where can I {verb} {article} {keyword} {when_type}?",
        "{verb} {article} {keyword} {when_type}.",
        "Looking for {article} {keyword} {when_type}.",
        "Can you help me {verb} {article} {keyword} {when_type}?",
        "{verb} {article}{keyword}  {when_type}.",
        "Tell me about {keyword} {when_type}.",
        "{verb} {keyword} {when_type}.",
        "I'm {verb} {keyword} {when_type}.",
        "Looking to {verb} {keyword} {when_type}."
    ])

    keyword, preposition = random.choice(["doctor", "medical shop", "hospital", "lab", "appointment", "my appointments", "my records"]), random.choice(when_types)

    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=keyword,
        when_type=preposition  # Assuming "preposition" corresponds to "when_type" for simplicity
    )

    if preposition == "today":
        query += f" I need to see a {random.choice(['doctor', 'physician', 'healthcare provider'])} because of {random.choice(scenarios)}."
        query += f" I prefer {random.choice(user_preferences)}."
    elif preposition == "tomorrow":
        query += f" It's {random.choice(scenarios)}, and I require help from a {random.choice(['hospital', 'medical center', 'healthcare facility'])}."
        query += f" I'd like a hospital {random.choice(user_preferences)}."

    return query.capitalize(), preposition

# Generate examples
examples = [generate_query() for _ in range(5000)]

# Shuffle the examples
random.shuffle(examples)

# Write the examples to a CSV file
with open('trail6.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "when"])
    writer.writerows(examples)

print("CSV file created successfully!")
