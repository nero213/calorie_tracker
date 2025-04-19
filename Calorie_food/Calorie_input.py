import json


# Load food data from JSON file
def load_food_data():
    try:
        with open("philippine_food_dataset.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ JSON file not found!")
        return []


# Calculate calories based on grams
def calculate_calories(food_name, grams, food_data):
    for food in food_data:
        if food['name'].lower() == food_name.lower():
            calories_per_100g = food['calories']
            calories = (calories_per_100g / 100) * grams
            return calories
    return None


# Main program
def main():
    Total_calories = 0
    limit = 2500
    food_data = load_food_data()
    if not food_data:
        return

    while True:
        food_name = input("🍽️ Enter the food name: ").strip()

        try:
            grams = float(input("⚖️ Enter how many grams you ate: "))
        except ValueError:
            print("❌ Please enter a valid number for grams.")
            return

        calories = calculate_calories(food_name, grams, food_data)

        if calories is not None:
            print(f"🔥 You consumed approximately {calories:.2f} calories from {grams} grams of {food_name}.")
            Total_calories += calories
        else:
            print("❌ Food not found in the dataset.")

        if Total_calories <= limit and calories is not None:
            remaining = limit - Total_calories
            print(f"Total calories Consumed this day {Total_calories} you have this much letf to consume {remaining}")
        elif Total_calories >= limit:
            print("you have consume way above you limit")


# Run only if this is the main file
if __name__ == "__main__":
    main()
