import json
from datetime import date

# Food dataset
food_data = [
    {"name": "Adobo", "calories": 400, "date_added": str(date.today())},
    {"name": "Sinigang na Baboy", "calories": 300, "date_added": str(date.today())},
    {"name": "Lechon", "calories": 500, "date_added": str(date.today())},
    {"name": "Pancit Canton", "calories": 350, "date_added": str(date.today())},
    {"name": "Kare-Kare", "calories": 460, "date_added": str(date.today())},
    {"name": "Lumpiang Shanghai", "calories": 200, "date_added": str(date.today())},
    {"name": "Sisig", "calories": 400, "date_added": str(date.today())},
    {"name": "Bicol Express", "calories": 350, "date_added": str(date.today())},
    {"name": "Puto", "calories": 150, "date_added": str(date.today())},
    {"name": "Halo-Halo", "calories": 300, "date_added": str(date.today())},
    {"name": "Bibingka", "calories": 250, "date_added": str(date.today())},
    {"name": "Turon", "calories": 180, "date_added": str(date.today())},
    {"name": "Laing", "calories": 350, "date_added": str(date.today())},
    {"name": "Pancit Malabon", "calories": 400, "date_added": str(date.today())},
    {"name": "Tocino", "calories": 350, "date_added": str(date.today())},
    {"name": "Dinuguan", "calories": 300, "date_added": str(date.today())},
    {"name": "Bangus (Milkfish)", "calories": 200, "date_added": str(date.today())},
    {"name": "Suman", "calories": 180, "date_added": str(date.today())},
    {"name": "Chicharrón", "calories": 500, "date_added": str(date.today())},
    {"name": "Kwek-Kwek", "calories": 250, "date_added": str(date.today())}
]

# Save to a JSON file
with open("philippine_food_dataset.json", "w") as file:
    json.dump(food_data, file, indent=4)

print("✅ Dataset saved to 'philippine_food_dataset.json'.")