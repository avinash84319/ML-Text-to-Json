import csv
import random

# Define actions with associated keywords and additional details
actions = {
    "find_doctor": ["doctor", "physician", "healthcare provider", "medical practitioner", "family doctor", "specialist", "GP",
                    "dermatologist", "cardiologist", "pediatrician", "gynecologist", "psychiatrist", "internal medicine", 
                    "surgeon", "oncologist", "neurologist", "urologist", "orthopedic", "endocrinologist", "ophthalmologist",
                    "otolaryngologist", "rheumatologist", "allergist", "pulmonologist", "gastroenterologist"],
    "find_medicalshop": ["medical shop","pharmacy", "drugstore", "chemist", "medical store", "apothecary", "health supply store",
                         "health shop", "pharmaceuticals", "prescription drugs", "over-the-counter", "herbal store",
                         "medical supply store", "health products store", "wellness store", "natural remedies store",
                         "vitamin store", "nutritional supplements store", "medical equipment store", "homeopathic store",
                         "online pharmacy", "local pharmacy", "community pharmacy", "neighborhood drugstore"],
    "find_hospital": ["hospital", "medical center", "healthcare facility", "clinic", "emergency room", "urgent care", 
                      "infirmary", "surgery center", "trauma center", "children's hospital", "rehabilitation center",
                      "psychiatric hospital", "cancer center", "heart institute", "eye hospital", "ENT clinic", 
                      "women's hospital", "orthopedic hospital", "diagnostic center"],
    "find_lab": ["lab", "diagnostic center", "testing facility", "medical laboratory", "pathology lab", "clinical lab",
                 "blood test lab", "urine test lab", "imaging center", "radiology lab", "genetic testing lab", 
                 "microbiology lab", "chemistry lab", "histopathology lab", "molecular diagnostics lab"],
    "book_appointment": ["appointment", "schedule", "book", "consultation", "meet with a doctor", "arrange a visit",
                         "set up a meeting", "reserve a time", "fix an appointment", "get a checkup", "schedule a check-up",
                         "make an appointment", "plan a visit", "book a slot", "request a consultation"],
    "my_appointments": ["my appointments", "upcoming appointments", "scheduled visits", "doctor appointments",
                        "medical appointments", "healthcare visits", "doctor meetings", "scheduled check-ups"],
    "my_records": ["my medical records", "health records", "medical history", "patient records", "health information",
                   "medical files", "health documents", "personal health records", "medical data", "patient information"]
}

# Shortened verbs, prepositions, articles, and expanded Indian cities (including Mysore)
verbs = ["need", "want", "look for", "require", "seek", "try", "wish", "question", "consult"]
prepositions = ["near", "in", "around", "close", "within", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", 
                "Kolkata", "Ahmedabad", "Mysore", "Pune", "Jaipur", "Lucknow", "Nagpur", "Indore", "Visakhapatnam", 
                "Kochi", "Coimbatore", "Bhopal", "Patna", "Vadodara", "Thiruvananthapuram", "Surat", "Kanpur", "Bhubaneswar",
                "Agra", "Amritsar", "Varanasi", "Guwahati", "Jodhpur", "Raipur", "Allahabad", "Aurangabad", "Ranchi"]
articles = ["a", "an", "the", "my", "this", "some"]
scenarios = ["emergency", "check-up", "second opinion", "procedure", "preventive care"]
user_preferences = ["male doctor", "female doctor", "specific hospital", "specific time"]

# Additional keywords for find_medicalshop
additional_medicalshop_keywords = ["pharmacist", "health store", "prescription medications", "first aid supplies",
                                   "medical essentials", "personal care products", "hygiene items", "wellness products",
                                   "OTC drugs", "home health supplies", "dietary supplements", "vitamins", "herbal remedies"]

# Function to generate a query for a given action
def generate_query(action, short=True):
    if short:
        query_structure = random.choice([
            "{verb} {article} {keyword} {preposition}.",
            "{verb} {article} find {keyword} {preposition}?",
            "{verb} {article} {keyword} {preposition}.",
            "Find {article} {keyword} {preposition}.",
            "{verb} {article} find {keyword} {preposition}?",
            "{verb} {article} {preposition} {keyword}.",
        ])
    else:
        query_structure = random.choice([
            "{verb} {article} {keyword} {preposition} {scenarios}.",
            "{verb} {article} {preposition} {scenarios}.",
            "Where {verb} {article} find {keyword} {preposition}?",
            "Can {verb} {article} find {keyword} {preposition}?",
            "{verb} {article} {preposition} {keyword}.",
            "{verb} {article} find {keyword} {preposition}?",
        ])

    query = query_structure.format(
        verb=random.choice(verbs),
        article=random.choice(articles),
        keyword=random.choice(actions[action] + additional_medicalshop_keywords),
        preposition=random.choice(prepositions),
        scenarios=random.choice(scenarios)
    )

    # Introduce additional details based on the action
    if not short:
        if action == "find_doctor":
            query += f" Prefer {random.choice(user_preferences)}."
        elif action == "find_hospital":
            query += f" Prefer {random.choice(user_preferences)}."
        elif action == "book_appointment":
            query += f" Find a suitable time, {random.choice(user_preferences)}."

    return query.capitalize()

# Generate 4000 examples (2000 short, 2000 long)
short_examples = [[generate_query(action, short=True), action] for _ in range(2000) for action in actions]
long_examples = [[generate_query(action, short=False), action] for _ in range(2000) for action in actions]
examples = short_examples + long_examples

# Write to CSV file
with open('generated_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "action"])
    writer.writerows(examples)
