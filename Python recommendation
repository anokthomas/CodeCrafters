import os
import pickle
from datetime import datetime, timedelta

UPLOADS_FOLDER = 'uploads'
ITEM_DATA_FILE = 'item_data.pkl'

# Function to load or initialize data
def load_data():
    if os.path.exists(ITEM_DATA_FILE):
        with open(ITEM_DATA_FILE, "rb") as f:
            return pickle.load(f)
    else:
        return {}

# Function to save data
def save_data(data):
    with open(ITEM_DATA_FILE, "wb") as f:
        pickle.dump(data, f)

# Function to recommend items with a minimum gap of 5 days
def recommend_items(data):
    today = datetime.now()
    recommended_items = []
    for item, last_accessed in data.items():
        time_since_last_access = today - last_accessed
        if time_since_last_access.days >= 5:
            recommended_items.append(item)
    return recommended_items

# Function to update last accessed date of an item
def update_last_accessed(data, item):
    data[item] = datetime.now()
    save_data(data)

# Main function
def main():
    data = load_data()

    while True:
        print("Recommendation:")
        recommended_items = recommend_items(data)
        if recommended_items:
            for item in recommended_items:
                print(f"- {item}")
        else:
            print("No items to recommend at the moment.")
        
        item_choice = input("Enter the name of the item you're accessing (or 'quit' to exit): ")

        if item_choice.lower() == 'quit':
            break
        
        if item_choice in os.listdir(UPLOADS_FOLDER):
            update_last_accessed(data, item_choice)
            print(f"You accessed {item_choice}.")
        else:
            print("Invalid item name.")

if __name__ == "__main__":
    main()
